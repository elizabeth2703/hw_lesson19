def debug(function):
    def wrapper(*args, **kwargs):
        print("Вызывается {}({})".format(
            function.__name__,
            ", ".join(
                list(f"\"{arg}\""
                     if isinstance(arg, str) else
                     str(arg) for arg in args)
                +
                list(f"{k}=\"{v}\""
                     if isinstance(v, str) else
                     f"{k}={v}" for k, v in kwargs.items())
            )
        ))
        result = function(*args, **kwargs)
        print("'{}' вернула значение'{}'".format(
            function.__name__, result
        ))
        print(result)
        return result
    return wrapper