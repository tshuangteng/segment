# 均分的切割l, 每一份的大小为n
def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
