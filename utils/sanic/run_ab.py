from sanic import Sanic
from sanic.response import json
from api import tasks

app = Sanic("addr_api")


@app.route('/get_addr', methods=['GET'])
async def get_addr(request):
    res_json = {
        "errorCode": -1,
        "msg": "error",
        "datas": None
    }
    res_content = json(res_json, ensure_ascii=False)
    data = request.json
    data = {'msg': '张三176XXXXXXXX唐镇南曹路901弄8号201'}

    if data:
        tmp_data = data.get('msg')
        if not tmp_data:
            return res_content
        r = tasks.parse_address.apply_async(args=[data])
        addr_json = r.get()
        return json(addr_json, ensure_ascii=False)
    else:
        return res_content


if __name__ == "__main__":
    app.run()
