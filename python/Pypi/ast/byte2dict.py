import ast

# Abstract Syntax Trees即抽象语法树。Ast是python源码到字节码的一种中间产物，借助ast模块可以从语法树的角度分析源码结构。
# 此外，我们不仅可以修改和执行语法树，还可以将Source生成的语法树unparse成python源码。因此ast给python源码检查、语法分析、修改代码以及代码调试等留下了足够的发挥空间。


# flask POST function: get response data
byte_data = request.get_data()

data = ast.literal_eval(byte_data.decode('utf8'))
