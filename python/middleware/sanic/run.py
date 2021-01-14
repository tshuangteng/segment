from sanic import Sanic
from sanic.response import json
from api import tasks

app = Sanic("addr_api")


@app.route('/get_addr', methods=['POST'])
async def get_addr(request):
    res_json = {
        "errorCode": -1,
        "msg": "error",
        "datas": None
    }
    res_content = json(res_json, ensure_ascii=False)
    data = request.json

    if not data or type(data) != dict:
        return res_content
    else:
        tmp_data = data.get('msg')
        if not tmp_data:
            return res_content

        res = tasks.parse_address.apply_async(args=[data])
        addr_json = res.get()
        return json(addr_json, ensure_ascii=False)


if __name__ == "__main__":
    app.run()
