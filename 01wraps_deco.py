# from functools import wraps
#
#
# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth = request.authorization
#         if not auth or not check_auth(auth.username, auth.password):
#             authenticate()
#         return f(*args, **kwargs)
#
#     return decorated

# from functools import wraps

# 讲一下执行过程
# 遇到函数，先记录一下，不会运行里面的内容，等调用的时候，再回头执行
# 传递的func是被装饰的函数名
def logit(func):
    def wrapper(*args, **kwargs):
        print(func.__name__ + " was called...")
        return func(*args, **kwargs)  # 返回给调用他的地方

    return wrapper


@logit
def addition_func(x):
    print('addition_func is execute...')  # 运行此函数显示这句
    return x + x


result = addition_func(4)
print(result)
