from collections import deque


class Cache:
    def __init__(self, size=10):
        self.__queue = deque()
        self.__size = size

    def put(self, item):
        self.__queue.append(item)

        if len(self.__queue) > self.__size:
            self.__queue.popleft()

    def get_last_item(self):
        if len(self.__queue) > 0:
            return self.__queue[-1]

    def get_items(self):
        yield from self.__queue
