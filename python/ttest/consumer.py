# pip install confluent-kafka -i https://pypi.doubanio.com/simple

from confluent_kafka import Consumer, KafkaError
from confluent_kafka.serialization import IntegerDeserializer, StringDeserializer

"""
用confluent-kafka 写一个消费者,参照java代码描述如python版本的
测试环境
1、测试环境kafka地址：10.172.32.28:2000,10.172.32.32:2000,10.172.32.33:2000，topic：scan_proto_transit group_id: scan-consumer-q
2、测试环境序列化和鉴权设置：
properties.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, LongDeserializer.class); 
properties.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, ByteArrayDeserializer.class);
 properties.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SASL_PLAINTEXT");
properties.put(SaslConfigs.SASL_MECHANISM, "SCRAM-SHA-512");
properties.put("sasl.jaas.config", "org.apache.kafka.common.security.scram.ScramLoginModule required username="admin" password="NTA4YjRhZDBmYjQ3";"); 

sasl账号：scan-consumer
sasl密码：Mjc2YjRjYjRiZWRi
消费组：scan-consumer-q

properties.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, LongDeserializer.class); 
properties.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, ByteArrayDeserializer.class);
这2个配置LongDeserializer和ByteArrayDeserializer 用confluent_kafka python代码怎么写
"""

conf = {
    'bootstrap.servers': '10.172.32.28:2000,10.172.32.32:2000,10.172.32.33:2000',
    'group.id': 'scan-consumer-q',
    'security.protocol': 'SASL_PLAINTEXT',
    'sasl.mechanism': 'SCRAM-SHA-512',
    'sasl.username': 'scan-consumer',
    'sasl.password': 'Mjc2YjRjYjRiZWRi',
    # 'key.deserializer': IntegerDeserializer,
    # 'value.deserializer': StringDeserializer,
    # 'key.deserializer': int.from_bytes,
    # 'value.deserializer': bytes.decode,
    'key.deserializer': 'org.apache.kafka.common.serialization.StringDeserializer',
    'value.deserializer': 'org.apache.kafka.common.serialization.StringDeserializer',
    'default.topic.config': {
        'auto.offset.reset': 'earliest'
    }
}

consumer = Consumer(conf)

# 订阅主题
consumer.subscribe(['scan_proto_transit'])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached {}/{}'.format(msg.topic(), msg.partition()))
        else:
            print('Error occured: {}'.format(msg.error().str()))
    else:
        # 处理消息
        print('Received message: key={}, value={}'.format(msg.key(), msg.value()))

consumer.close()
