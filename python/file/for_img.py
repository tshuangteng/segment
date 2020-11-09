import cv2
import numpy as np
import base64

img_path = ''

# 客户端请求
with open(str(img_path), 'rb') as f:
    base64_data = base64.b64encode(f.read()).decode('utf-8')
    body = {'img': base64_data}

# 服务端接收
decode_base64_data = base64.b64decode(body['img'])

img_array = np.fromstring(base64_data, np.uint8)
img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)
