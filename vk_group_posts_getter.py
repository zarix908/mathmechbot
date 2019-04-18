import json
import logging
import requests
from post import Post
from utils import handle_error


class VkGroupPostsGetter:
    def __init__(self, service_token, group_id):
        self.__service_token = service_token
        self.__group_id = group_id

    @handle_error(logging.error, range(0))
    def get(self, count=1):
        group_id = self.__group_id
        service_token = self.__service_token
        url = 'https://api.vk.com/method/wall.get?' \
              f'owner_id={group_id}&count={str(count)}&' \
              f'access_token={service_token}&v=5.21'

        response = json.loads(requests.get(url).text)["response"]

        for i in range(count):
            post = response["items"][i]
            yield Post(post["id"], post["text"])
