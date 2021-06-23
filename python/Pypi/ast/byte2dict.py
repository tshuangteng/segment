import ast

# flask POST function: get response data
byte_data = request.get_data()

data = ast.literal_eval(byte_data.decode('utf8'))
