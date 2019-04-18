import logging
import telebot
from utils import handle_error


class TelegramChatBot:
    def __init__(self, bot_token, chat_id):
        self.__bot = telebot.TeleBot(bot_token)
        self.__chat_id = chat_id

    @handle_error(logging.error)
    def get_last_message(self):
        return self.__bot.get_updates()[0].message.text

    @handle_error(logging.error)
    def send_message(self, message):
        self.__bot.send_message(self.__chat_id, message)

    def bind_chat(self, chat_id):
        self.__chat_id = chat_id

    def set_webhook(self, url):
        return self.__bot.set_webhook(url)
