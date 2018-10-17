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

from functools import wraps


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called...")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    print('addition_func is execute...')
    return x + x


result = addition_func(4)
print(result)
# output: addition_func was called...
# addition_func is execute...
# 8
