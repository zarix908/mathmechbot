from .action_info import ActionInfo
from .cache import Cache

cache = Cache()


def log(func):
    def decorator(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            cache.put(ActionInfo(True, result, None))
            return result
        except Exception as e:
            cache.put(ActionInfo(False, None, e))
            raise e

    return decorator


def get_logs():
    return '\r\n'.join((str(i) for i in cache.get_items()))


__all__ = ['log', 'get_logs']
