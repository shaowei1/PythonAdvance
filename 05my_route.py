# from functools import wraps
#
#
# def my_route1(url):
#     def set_func(func):
#         @wraps(func)
#         def wrapper():
#             router[url] = wrapper.__name__
#
#         return wrapper
#
#     return set_func
#
#
# def my_route1(url):
#     def set_func(func):
#         def func():
#             # func()已经不是index, 已经是func自己{'/login.html': 'func', '/index.html': 'func'}
#             router[url] = func.__name__
#
#         return func
#
#     return set_func

def my_route1(url):
    def set_func(func):
        def wrapper():
            router[url] = func.__name__

        return wrapper

    return set_func


@my_route1('/index.html')
def index():
    return 'index page'


@my_route1('/login.html')
def login():
    return 'login page'


if __name__ == '__main__':
    # {'/login.html': 'login',
    # '/index.html': 'index'}
    router = {}
    login()
    index()
    print(router)
