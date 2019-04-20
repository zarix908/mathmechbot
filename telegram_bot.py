import json
import telebot
import config
from vk_posts_manager import VkPostsManager
from web_logging import log


class TelegramBot(telebot.TeleBot):
    def __init__(self):
        super().__init__(config.TELEGRAM_BOT_TOKEN)
        self.__posted = True
        self.__posts_manager = VkPostsManager(config.VK_SERVICE_TOKEN, config.VK_GROUP_ID,
                                              config.LAST_POSTS, config.POSTS_MAX_COUNT)

    def process_update(self, update):
        try:
            message = self.parse_message(update)
            self.process_message(message)
        except Exception:
            self.send_message(config.TELEGRAM_DIALOG_ID, "Ой, ошибочка вышла")

    @log
    def process_message(self, message):
        if message == '/show':
            self.show_new_posts()
        if message == '/post':
            self.repost()

    @log
    def show_new_posts(self):
        if self.__posted:
            self.__posts_manager.update()
            self.__posted = False

        posts = self.__posts_manager.posts

        if len(posts) == 0:
            self.send_message(config.TELEGRAM_DIALOG_ID, 'Новых постов нет')

        for post in posts:
            if post.text:
                self.send_message(config.TELEGRAM_DIALOG_ID, post.text)

    @log
    def repost(self):
        posts = self.__posts_manager.posts
        posts.sort(key=lambda el: el.id)

        for post in posts:
            if post.text:
                self.send_message(config.TELEGRAM_CHANNEL_ID, post.text)

        self.__posted = True
        self.send_message(config.TELEGRAM_DIALOG_ID, 'Посты опубликованы')

    @log
    def parse_message(self, update):
        return json.loads(update)['message']['text']
