import base64
import os

from api.telno_detect_tocall import img_to_str
from celery_app import app


@app.task(name='celery_app.task1.detect_img')
def detect_img(data):
    base64_data = data['img_base64'].encode('utf-8')
    base64_data = base64.b64decode(base64_data)
    try:
        os.remove('../api/gen_temp.jpg', )
    except Exception:
        pass
    with open('../api/gen_temp.jpg', 'wb') as f:
        f.write(base64_data)
    phone_no = img_to_str('../api/gen_temp.jpg')
    os.remove('../api/gen_temp.jpg')
    return phone_no
