list1 = ['A', 'B', 'C', 'D']
B = ['c']
for i in list1:
    locals()[i] = []
    # globals()[i] = []
    # exec(f"{i} = []")
print(B)
print(locals())
import math

# n = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
# new = eval(n)
# print(new)
#
# print(type(...))

# for _ in range(100000):
#     with open('../a.txt', 'a', encoding='utf8') as f:
#         f.write(f'{9}')

# s1 = input("请输入a+b:")
# print(eval(s1))
