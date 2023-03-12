from functools import wraps


# def cache3(func):
#     @wraps(func)
#     def wrapper():
#         cache = func()
#         count = 0
#         if count > 2:
#             cache = func()
#             count = 0
#         return cache
#     return wrapper

def cache3(func):
    counter = 0
    result = {}
    result = 0
    def wrapper():
        nonlocal counter
        counter += 1
        if counter<=3:
            if func() in result: 
                return result[func()]
        else:
            counter = 1
            return func()
    return wrapper


@cache3
def heavy():
    print('Сложные вычисления')
    return 1


print(heavy())
# Сложные вычисления
# 1
print(heavy())
# 1
print(heavy())
# 1

# Опять кеш устарел, надо вычислять заново
print(heavy())
# Сложные вычисления
# 1
