"""
推荐使用 f-string
"""

n = 12
# 整数补零 (宽度为3)
print('{:0=3d}'.format(n, n))  # (Python2.6及以上)
print(f'{n:0=3d}')  # 语法2 (Python3)


n = 3.6485926
# 保留小数点后2位（四舍五入）
print(f'{n:.2f}')
# 保留小数点后0位（四舍五入）
print(f'{n:.0f}')
# 带符号保留小数点后两位（四舍五入）
print(f'{n:+.2f}')


n = 9
# 右对齐，宽度为3，填充0
print(f'{n:0>3d}')
# 左对齐，宽度为3，填充x
print(f'{n:x<3d}')
# 居中对齐，宽度为3，填充x
print(f'{n:x^3d}')


# 千位符，以逗号分隔的数字格式
n = 100000
print(f'{n:,}')
n = 123456789
print(f'{n:,}')


# 百分比格式
n = 0.25
print(f'{n:.2%}')
n = 25
print(f'{n:.2%}')


n = 1000000000
# 指数记法
print(f'{n:.2e}')


# 附：
# round()保留小数位（四舍五入，结果为float类型）
n = 3.6485926
print(round(n, 3))  # 3.649

# 进制转换
n = 11
print(f'{n:b}')  # 1011
print(f'{n:d}')  # 11
print(f'{n:o}')  # 13
print(f'{n:x}')  # b
