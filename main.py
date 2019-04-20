from flask import Flask, request

import config
import web_logging
from telegram_bot import TelegramBot

app = Flask(__name__)

telegram_bot = TelegramBot()
telegram_bot.set_webhook(f'{config.APP_HOST}/update')


@app.route('/update', methods=['POST'])
def update():
    telegram_bot.process_update(request.data)
    return 'True'


@app.route('/logs', methods=['GET'])
def get_logs():
    return web_logging.get_logs()
