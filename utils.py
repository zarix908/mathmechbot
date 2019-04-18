def handle_error(action, return_value=None):
    def decorator(func):
        def with_args(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                action(e)

            return return_value

        return with_args
    return decorator

