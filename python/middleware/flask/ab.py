from flask import Flask, request
from api import tasks
import json

app = Flask(__name__)


@app.route('/get_addr', methods=['get'])
def get_addr():
    res_json = {
        "errorCode": -1,
        "msg": "error",
        "datas": None
    }
    data = request.get_json()
    data = {'msg': '张三176XXXXXXXX唐镇南曹路901弄8号201'}
    if data:
        tmp_data = data.get('msg')
        if not tmp_data:
            return json.dumps(res_json, ensure_ascii=False)
        r = tasks.parse_address.apply_async(args=[data])
        addr_json = r.get()
        return json.dumps(addr_json, ensure_ascii=False)
    else:
        return json.dumps(res_json, ensure_ascii=False)


if __name__ == "__main__":
    app.run()
