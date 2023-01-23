from typing import Callable
from functools import wraps
def debug(name_function: Callable)->Callable:
    @wraps(name_function)
    def wrapper(*args, **kwargs):
        arg_kwarg_line = ''
        for arg in args:
            if isinstance(arg, str):
                arg_kwarg_line += "".join([f"'{arg}'"])
            else:
                arg_kwarg_line += str(arg)
        for key, value in kwargs.items():
            if isinstance(value, str):
                arg_kwarg_line += f"{key}='{value}'"
            else:
                arg_kwarg_line += f', {key}={value}'

        print(f'Вызывается {name_function.__name__}({arg_kwarg_line})')
        function_call = name_function(*args, **kwargs)
        print(f"{name_function.__name__} вернула значение '{function_call}'")
        return f'{function_call}\n'

    return wrapper