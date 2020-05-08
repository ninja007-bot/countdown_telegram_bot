import os

import dotenv
import pytimeparse

import ptbot


def render_progressbar(total, iteration, prefix='', suffix='', length=30,
                       fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def send_progress_message(secs, timeout, message_id, bot):
    progress_bar = render_progressbar(timeout, secs)
    message = f"Осталось секунд - {secs}\n {progress_bar}"
    bot.update_message(telegram_chat_id, message_id, message)


def reply(text, bot, telegram_chat_id):
    timeout = pytimeparse.parse(text)
    if timeout is None:
        bot.send_message(chat_id=telegram_chat_id, message="Неверное время!")
        return
    message = f"Таймер запущен на {timeout} секунд"
    message_id = bot.send_message(telegram_chat_id, message)
    bot.create_countdown(timeout, send_progress_message, timeout=timeout,
                         message_id=message_id, bot=bot)
    bot.create_timer(timeout,
                     lambda: bot.send_message(telegram_chat_id, "Времы вышло"))


if __name__ == '__main__':
    dotenv.load_dotenv()
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
    bot = ptbot.Bot(telegram_token)
    bot.send_message(telegram_chat_id,
                     "Бот запущен!\nНа сколько запустить таймер?")
    bot.reply_on_message(reply, bot, telegram_chat_id)
    bot.run_bot()
