# # coding:utf8
# import time
# import signal
#
#
# # 自定义超时异常
# class TimeoutError(Exception):
#     def __init__(self, msg):
#         super(TimeoutError, self).__init__()
#         self.msg = msg
#
#
# def time_out(interval, callback):
#     def decorator(func):
#         def handler(signum, frame):
#             raise TimeoutError("run func timeout")
#
#         def wrapper(*args, **kwargs):
#             try:
#                 signal.signal(signal.SIGALRM, handler)
#                 signal.alarm(interval)  # interval秒后向进程发送SIGALRM信号
#                 # signal.setitimer(1, 0.1)  # interval秒后向进程发送SIGALRM信号
#                 result = func(*args, **kwargs)
#                 signal.alarm(0)  # 函数在规定时间执行完后关闭alarm闹钟
#                 return result
#             except TimeoutError as e:
#                 callback(e)
#
#         return wrapper
#
#     return decorator
#
#
# def timeout_callback(e):
#     print(e.msg)
#
#
# @time_out(2, timeout_callback)
# def task1():
#     print("task1 start")
#     time.sleep(3)
#     print("task1 end")
#
#
# @time_out(2, timeout_callback)
# def task2():
#     print("task2 start")
#     time.sleep(1)
#     print("task2 end")
#
#
# if __name__ == "__main__":
#     task1()
#     task2()


# pip install func_timeout -i https://pypi.doubanio.com/simple
from func_timeout import func_set_timeout, FunctionTimedOut
import time


@func_set_timeout(0.2)
def mytest():
    print("Start")
    for i in range(1, 10):
        print("%d seconds have passed" % i)
        time.sleep(1)


if __name__ == '__main__':
    now = time.time()

    try:
        mytest()
    except FunctionTimedOut as e:
        print('mytest2:::', e)
    print('finish test')

    print(time.time() - now)
