import logging
from time import sleep

from flask import Flask

app = Flask(__name__)


class VkTelegramReposter:
    def __init__(self, telegram_chat_bot, vk_group_posts_getter):
        self.__telegram_chat_bot = telegram_chat_bot
        self.__vk_group_posts_getter = vk_group_posts_getter

    def run(self):
        last_post_id = None

        while True:
            last_post = self.__vk_group_posts_getter.get()

            if last_post.id != last_post_id:
                self.__telegram_chat_bot.send_message(last_post.text)
                logging.info(f'last repost id: {last_post.id}')
                last_post_id = last_post.id

            sleep(1)
