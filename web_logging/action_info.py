class ActionInfo:
    def __init__(self, is_success, result, error):
        self.__is_success = is_success
        self.__result = result
        self.__error = error

    def __str__(self):
        return f'{{success: {self.__is_success} ' \
               f'result: {self.__result} ' \
               f'error: {self.__error}}}'

