from functools import wraps
from sanic import Sanic
from sanic.response import json, text
from sanic.exceptions import abort

app = Sanic(__name__)

# 假设以下令牌是有效的，实际情况应该从某个安全存储中获取令牌。
VALID_TOKEN = 'abcd1234'


# 安全验证中间件
def require_token(token):
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            if 'Authorization' not in request.headers:
                abort(401, 'Authorization header is missing')
            if request.headers['Authorization'] != f'Token {token}':
                abort(401, 'Invalid or missing token')
            response = await f(request, *args, **kwargs)
            return response
        return decorated_function
    return decorator


# 路由
@app.route('/')
@require_token(VALID_TOKEN)  # 应用安全验证中间件
async def index(request):
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)



# 安全验证的中间件函数是在路由函数中直接调用的，而不是在中间件中注册的。这是因为，中间件函数和路由函数有不同的执行上下文和功能，中间件函数主要用于在请求到达路由之前对请求进行处理，而路由函数用于处理请求并返回响应。
# 在实际应用中，建议将安全验证的中间件函数注册到中间件列表中，以确保每个请求都进行安全验证。以下是如何将安全验证的中间件函数注册到sanic应用程序中：


from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

# 安全验证中间件函数
async def auth_middleware(request):
    # 在这里进行安全验证
    # 如果验证失败，则返回拒绝访问的响应
    # 如果验证成功，则让请求继续处理
    # 这里的示例代码只是一个简单的验证，您需要根据实际情况进行修改
    auth_token = request.headers.get('Authorization')
    if auth_token != 'my-secret-token':
        return json({'error': 'Access denied'}, status=401)
    return

# 将安全验证中间件函数注册到中间件列表中
app.middleware('request')(auth_middleware)

# 路由
@app.route('/')
async def index(request):
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
