import time


# 3.0
def display_time(func):
    def wrapper():
        # 计时
        t1 = time.time()
        # 逻辑
        func()
        t2 = time.time()
        print(t2 - t1)

    return wrapper


# 1.O(n)
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


# 2.有一堆这样的代码，分离
# def prime_nums():
#     # 计时
#     t1 = time.time()
#     # 逻辑
#     for i in range(2, 10000):
#         if is_prime(i):
#             print(i)
#     t2 = time.time()
#     print(t2 - t1)

@display_time
def prime_nums():
    for i in range(2, 10000):
        if is_prime(i):
            print(i)


prime_nums()
