import json
import logging
import ChatAI

from ChatAI import ChatAI
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters


logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
LOGGER = logging.getLogger(__name__)
NAME = None
TOKEN = None
CHATAI = None


def start(update: Update, context: CallbackContext):
    update.message.reply_text('What?')


def load_data():
    global NAME, TOKEN
    LOGGER.info('Loading BOT data...')
    file = open('res/BotINI.json')
    if file:
        text = file.read()
        if text:
            json_obj = json.loads(text)
            NAME = json_obj['Name']
            TOKEN = json_obj['Token']
    LOGGER.info('Loading complete.')


def chatting(update: Update, context: CallbackContext):
    global CHATAI
    answer = CHATAI.create_answer(update.message.text)
    update.message.reply_text(answer)


def bot_init():
    global NAME, TOKEN, CHATAI
    LOGGER.info('Starting BOT...')
    load_data()
    CHATAI = ChatAI()
    if NAME is not None and TOKEN is not None:
        updater = Updater(TOKEN)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler('start', start))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, chatting))

        updater.start_polling()
