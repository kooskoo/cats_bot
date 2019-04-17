import os

import functools

from telegram.ext import Updater, CommandHandler
from telegram import ChatAction
import logging

import catapi


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(os.environ['TG_TOKEN'], use_context=True)

dispatcher = updater.dispatcher


def send_action(action):

    def decorator(func):
        @functools.wraps(func)
        def command_func(update, context, *args, **kwargs):
            context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)
            return func(update, context, *args, **kwargs)
        return command_func

    return decorator


def start_callback(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=f'Hello, {update.effective_user.first_name}!\nSee /help for instructions')


@send_action(ChatAction.TYPING)
def help_callback(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='To get a random catpic - just type /cat. '
                                  'To get a specific breed - type /cat <breed>. '
                                  '<breed> is four-character ID. '
                                  'Here is the mapping of breed and their IDs:\n\n'
                                  + str(catapi.get_breeds_list()))


@send_action(ChatAction.UPLOAD_PHOTO)
def cat_callback(update, context):
    context.bot.send_photo(chat_id=update.message.chat_id, photo=catapi.cat_by_breed(context.args))


dispatcher.add_handler(CommandHandler('start', start_callback))
dispatcher.add_handler(CommandHandler('help', help_callback))
dispatcher.add_handler(CommandHandler('cat', cat_callback))

updater.start_polling()
updater.idle()
