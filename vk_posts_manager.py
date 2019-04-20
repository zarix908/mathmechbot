import json
import requests
from post import Post
from web_logging import log


class VkPostsManager:
    def __init__(self, service_token, group_id, last_posts, posts_max_count):
        self.__service_token = service_token
        self.__group_id = group_id

        self.__posts = []
        self.__last_posts = last_posts
        self.__posts_max_count = posts_max_count

    @property
    def posts(self):
        return self.__posts.copy()

    @log
    def update(self):
        posts = []
        group_id = self.__group_id
        service_token = self.__service_token
        url = 'https://api.vk.com/method/wall.get?' \
            f'owner_id={group_id}&count={self.__posts_max_count}&' \
            f'access_token={service_token}&v=5.21'

        response = json.loads(requests.get(url).text)["response"]

        for i in range(self.__posts_max_count):
            post = response["items"][i]
            post = Post(post["id"], post["text"])

            if post not in self.__last_posts:
                posts.append(post)

        posts.sort(key=lambda el: el.id)
        self.__last_posts.enqueue_range(posts)
        self.__posts = posts
