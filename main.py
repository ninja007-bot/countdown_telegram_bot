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


def reply(text):
    timeout = pytimeparse.parse(text)
    if timeout is None:
        bot.send_message(chat_id=CHAT_ID, message="Неверное время!")
        return
    message = f"Таймер запущен на {timeout} секунд"
    message_id = bot.send_message(CHAT_ID, message)

    def send_progress_message(secs):
        progress_bar = render_progressbar(timeout, secs)
        message = f"Осталось секунд - {secs}\n {progress_bar}"
        bot.update_message(CHAT_ID, message_id, message)

    bot.create_countdown(timeout, send_progress_message)
    bot.create_timer(timeout, lambda: bot.send_message(CHAT_ID, "Времы вышло"))


if __name__ == '__main__':
    dotenv.load_dotenv()
    TOKEN = os.getenv("TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    bot = ptbot.Bot(TOKEN)
    bot.send_message(CHAT_ID, "Бот запущен!\nНа сколько запустить таймер?")
    bot.reply_on_message(reply)
    bot.run_bot()
