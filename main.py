import telebot
from bot_token import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands = ['start'])
def start(message):
  bot.send_message(message.chat.id, '❗️ Привет, отправь видео')


@bot.message_handler(content_types=['video'])
def send_text(message):
    file_info = bot.get_file(message.video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('video.mp4', 'wb') as video:
        video.write(downloaded_file)
    bot.send_video_note(message.chat.id, open('video.mp4', 'rb'))


bot.polling(none_stop=True)