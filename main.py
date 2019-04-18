from flask import Flask
import config
from telegram_chat_bot import TelegramChatBot
from vk_group_posts_getter import VkGroupPostsGetter

app = Flask(__name__)

vk_posts_getter = VkGroupPostsGetter(config.VK_SERVICE_TOKEN, config.VK_GROUP_ID)
telegram_bot = TelegramChatBot(config.TELEGRAM_BOT_TOKEN, config.TELEGRAM_CHANNEL_ID)

last_post_id = '9018'


@app.route('/webhook', methods=['POST'])
def webhook():
    global last_post_id

    last_post = next(iter(vk_posts_getter.get()))
    count = int(last_post.id) - int(last_post_id)
    last_post_id = last_post.id

    posts = reversed(list(vk_posts_getter.get(count)))
    for post in posts:
        telegram_bot.send_message(post.text)

    return 'Ok'


@app.route('/init', methods=['GET'])
def set_webhook():
    url = f'{config.GOOGLE_ENGINE_HOST}/webhook'
    success = telegram_bot.set_webhook(url)
    if success:
        return url


#if __name__ == '__main__':
#    app.run()

