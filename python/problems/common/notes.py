# 均分的切割l, 每一份的大小为n

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

express = [1,2,3,4,5]
all_chunks = list(chunks(express, 2))
for ep in all_chunks:
    print(ep)