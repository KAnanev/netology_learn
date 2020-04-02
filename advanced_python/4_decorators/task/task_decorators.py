# def decor_func(old_func):
#     def new_func(*args, **kwargs):
#         import time
#         time_call = time.strftime("%H:%M:%S %Y-%m-%d", time.localtime())
#         print(f'{time_call}, {old_func.__name__}, {args}, {kwargs}')
#
#     return new_func()
#
#
# @decor_func
# def get_habr(uri='/'):
#     import requests
#     result = requests.get(f'http://habr.com{uri}')
#     return result.text


def stability(old_function):
    def new_function(*args, **kwargs):
        import time
        time_call = time.strftime("%H:%M:%S %Y-%m-%d", time.localtime())
        print(f'{time_call}, {old_function.__name__}, {args}, {kwargs}')
        try:
            description = old_function(*args, **kwargs)
            status = 'success'
        except Exception as er:
            status = 'error'
            description = er
        result = {'status': status,
                  'description': description,
                  'action': old_function.__name__}
        return result

    return new_function()


@stability
def get_habr(uri='/'):
    result = requests.get(f'http://habr.tom{uri}')