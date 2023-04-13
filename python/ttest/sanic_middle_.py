import logging
import sys
from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

# 配置日志记录器
logger = logging.getLogger('sanic.access')
logger.setLevel(logging.INFO)

# 配置日志处理程序
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter(
    '{"time":"%(asctime)s", "level": "%(levelname)s", '
    '"request_id": "%(request_id)s", "method": "%(method)s", '
    '"path": "%(path)s", "status": %(status)d, "duration": %(duration)d}\n'
))

# 添加处理程序到日志记录器
logger.addHandler(handler)


# 请求处理中间件
@app.middleware('request')
async def log_request(request):
    # 将请求ID添加到日志记录器上下文中
    logging_context = {'request_id': request.ctx.request_id}
    request.ctx.logging_context = logging_context

    # 在日志记录器上下文中添加请求信息
    logger.info('Request received', extra={
        'method': request.method,
        'path': request.path
    })


# 路由
@app.route('/')
async def index(request):
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
