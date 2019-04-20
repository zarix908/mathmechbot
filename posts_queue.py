from collections import deque


class PostsQueue:
    def __init__(self, size):
        self.__size = size
        self.__queue = deque()
        self.__set = set()

    def enqueue(self, post):
        self.__queue.append(post)
        self.__set.add(post.id)

        if len(self.__queue) > self.__size:
            old_post = self.__queue.popleft()
            self.__set.remove(old_post.id)

    def __contains__(self, post):
        return post.id in self.__set

    def enqueue_range(self, iterable):
        for post in iterable:
            self.enqueue(post)
