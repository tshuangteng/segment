from functools import partial


# def chunk_file_reader(fp, block_size=1024 * 8):
#     while 1:
#         chunk = fp.read(block_size)
#         if not chunk:
#             break
#         yield chunk
#
#
# def read_chunk_file(f_name):
#     count = 0
#     with open(f_name) as fp:
#         n = chunk_file_reader(fp)
#         for chunk in chunk_file_reader(fp):
#             count += chunk.count('9')
#     return count
#
#
# a = read_chunk_file('a.txt')
# print(a)


def chunked_file_reader(file, block_size=1024 * 8):
    for chunk in iter(partial(file.read, block_size), ''):
        yield chunk


def read_chunk_file(f_name):
    count = 0
    with open(f_name) as fp:
        for chunk in chunked_file_reader(fp):
            count += chunk.count('9')
    return count


a = read_chunk_file('a.txt')
print(a)
