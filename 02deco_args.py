# from functools import wraps
#
#
# def logit(logfile='out.log'):
#     def logging_decorator(func):
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             log_string = func.__name__ + "was called"
#             print(log_string)
#             # open the logfile and append
#             with open(logfile, 'a') as opened_file:
#                 # Now we log to the specified logfile
#                 opened_file.write(log_string + '\n')
#
#         return wrapped_function
#
#     return logging_decorator
#
#
# # 只要有括号不论括号里面有没有都是装饰器传参，一定有三层
# @logit(logfile='func2.log')
# def myfunc2():
#     pass
#
#
# myfunc2()

