

# 问题: 求任意字符的所有排列组合
# 解决思路: 分而治之
def arrangement_string(s):
    length = len(s)
    if length <= 1:
        return [s]

    all_str_combination = []
    for i in range(length):
        for j in arrangement_string(s[0:i] + s[i + 1:]):
            all_str_combination.append(s[i] + j)

    return all_str_combination


if __name__ == '__main__':
    res = arrangement_string('acvd')
    print(res)
    print(len(res))
    # 字符重复的情况,去重即可
    res2 = arrangement_string('abbcd')
    print(len(res2))
    print(res2)
    print(len(set(res2)))
    print(set(res2))
