from datetime import time


def args_to_string(*args, **kwargs):
    import json
    return f'{json.dumps(args)}_{json.dumps(kwargs)}'


def decor_func(old_func):
    def new_func(*args, **kwargs):
        call_time = time()
        result = old_func(*args, **kwargs)
        print(call_time)
        return result
    return new_func


@decor_func
def func(*args, **kwargs):
    return args, kwargs

func(3, 4)






