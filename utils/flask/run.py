from flask import Flask, request
from api import tasks
import json

app = Flask(__name__)


@app.route('/get_addr', methods=['post'])
def get_addr():
    res_json = {
        "errorCode": -1,
        "msg": "error",
        "datas": None
    }
    res_content = json.dumps(res_json, ensure_ascii=False)
    data = request.get_json()

    if data:
        tmp_data = data.get('msg')
        if not tmp_data:
            return res_content
        r = tasks.parse_address.apply_async(args=[data])
        addr_json = r.get()
        return json.dumps(addr_json, ensure_ascii=False)
    else:
        return res_content


if __name__ == "__main__":
    app.run()
