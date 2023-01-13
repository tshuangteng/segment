list1 = ['A', 'B', 'C', 'D']
for i in list1:
    locals()[i] = ['a']
    # globals()[i] = ['b']
    # exec(f"{i} = ['c']")
print(A,B,C,D)
print(locals())
print(globals())

#####################################################
# 1
with open('a.txt', 'r', encoding='utf-8') as f:
    all_line_list = f.readlines()
    for line_list in all_line_list:
        ff = eval(line_list)
        print(ff)
        print(type(ff))

# 2
# s1 = input("请输入a+b:")
# print(eval(s1))

# 3
n = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
new = eval(n)
print(new)
print(type(new))
print(type(...))  # <class 'ellipsis'>

# eval()  --->   evaluate arbitrary Python expressions from a string-based or compiled-code-based input
# locals() --->  set current global scope or namespace
# globals()  --->  set current global scope or namespace
