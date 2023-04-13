import logging
from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

# 创建日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 配置日志记录格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 创建日志处理程序
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

# 添加处理程序到日志记录器
logger.addHandler(handler)


# 请求处理中间件
@app.middleware('request')
async def log_request(request):
    # 记录请求信息
    logger.info(f"\n\n=================== Request Details ===================\n"
                f"{request.method} {request.url}\n"
                f"Request headers: {request.headers}\n"
                f"Request body: {request.body.decode('utf-8')}\n"
                f"Query string: {request.query_string}\n"
                f"Remote address: {request.remote_addr}\n"
                f"User-agent: {request.headers.get('user-agent')}\n"
                f"Referer: {request.headers.get('referer')}\n"
                f"=======================================================\n")


# 路由
@app.route('/')
async def index(request):
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
