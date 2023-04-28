import pickle

from confluent_kafka import Consumer, KafkaError


conf = {
    'bootstrap.servers': '10.172.32.28:2000,10.172.32.32:2000,10.172.32.33:2000',
    'group.id': 'scan-consumer-q',
    'security.protocol': 'SASL_PLAINTEXT',
    'sasl.mechanism': 'SCRAM-SHA-512',
    'sasl.username': 'scan-consumer',
    'sasl.password': 'Mjc2YjRjYjRiZWRi',
    'default.topic.config': {
        'auto.offset.reset': 'earliest'
    }
}

consumer = Consumer(conf)

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
        original_data = pickle.loads(msg.value())
        print(original_data)

consumer.close()
