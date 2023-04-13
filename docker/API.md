## API接口文档

### 接口地址

| 环境 |             URL             | 请求方式 |
| :--: |:---------------------------:| :---: |
| 测试 |  http://127.0.0.1:8867/xxx  | POST |
| 生产 | http://ai.xxx.com:55423/xxx | POST |

### 请求参数

请求体是**JSON**数据结构,**UTF8**格式

| 参数名 | 类型 | 是否必须 | 示例 | 备注 |
|:----------:|:------:|:------------------------:|:--:| :----: |
| event_type | number | 必填 | 1 | 1:打电话<br>2:抽烟<br>3:打哈欠<br>4:双手脱离方向盘<br>5:未系安全带<br>6:分心驾驶<br>7:疲劳驾驶 |
| pic_path | string | 选填 | http://www.xxxx.com/1.jpg | 见说明 |
| avi_path | string | 选填 | http://www.xxxx.com/1.mp4 | 见说明 |


### 返回结果

响应结果是**JSON**格式

| 参数名 | 类型 | 是否必须 | 示例 | 备注 |
|:----------:|:------:|:------------------------:|:--:| :----: |
| code | integer | 是 | 0 | 0:请求成功;<br>-1:请求失败 |
| message | string | 是 | success | 响应描述 |
| data | object | 是 | {"algorithm_result": 11000,<br> "event_type": 2,<br> "classify_event_type": 0,<br> "probability": 0.9706} | 识别结果 |
| data["algorithm_result"] | integer | 是 | 11000 | 10000:正报;<br>11000:误报 |
| data["event_type"] | integer | 是 | 2 | 事件类型<br>1:打电话 2:抽烟 3:打哈欠<br> 4:双手脱离方向盘 5:未系安全带 6:分心驾驶 7:疲劳驾驶 |
| data["classify_event_type"] | integer | 是 | 0 | 事件类型<br>0:其他 1:打电话 2:抽烟 3:打哈欠<br> 4:双手脱离方向盘 5:未系安全带 6:分心驾驶 7:疲劳驾驶 |
| data["probability"] | number | 是 | 0.9706 | 算法返回的分值：0~1,保留4位小数 |

### CURL测试案例

```
curl --location --request POST 'http://ai.xxx.com:55423/xxx'\
  --header 'Content-Type: application/json'\
  --data-raw '{"pic_path": 
  "https://xxx.com/AlarmData/2022-04-18/14426455485/94914_00_02_6503_0_351959c536fa4c869fe235e329d3a599.jpg", 
  "event_type": 2}'
```

#### 响应结果示例

```
{
"code": 0, 
"message": "success", 
"data": {
  "algorithm_result": 11000, 
  "event_type": 2, 
  "classify_event_type": 0, 
  "probability": 0.9706
  }
} 
```
