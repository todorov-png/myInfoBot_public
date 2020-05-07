import telebot
import random
from telebot import types
global PasswordSetting
PasswordSetting = 'Bot_share'
global ChatId
ChatId = id вашего чата с ботом
global TypeMessage
TypeMessage = 0
global UserNameMessage
UserNameMessage=''
global StartMessageText
StartMessageText = 'Привет, я Info-bot, пиши мне свои идеи, я их отправлю создателю'
global TOKEN
TOKEN = 'Ваш токен бота'
global bot
bot=telebot.TeleBot(TOKEN)
#Отправляем приветственное сообщение при команде старт
@bot.message_handler(commands=['start'])
def welcome(message):
   #Отправляем стикер
   bot.send_message(message.chat.id, StartMessageText)
   global TypeMessage
   TypeMessage=0


@bot.message_handler(commands=['help'])
def help(message):
   bot.send_message(message.chat.id, 'Для настройки приветственного сообщения введите: \n"/StartMessage+пароль доступа+текст приветственного сообщения"\nДля изменения целевого чата введите: \n"/bot_setup+пароль доступа"\nЗначения в командах разделяйте пробелом')
   

@bot.message_handler(commands=['StartMessage'])
def StartMessageF(message):
   #Настраиваем бота на свое сообщение
   #Если пароль верный то меняем данные
   global PasswordSetting
   global StartMessageText
   if(PasswordSetting==message.text[14:23]):
      StartMessageText=message.text[24:]
      bot.send_message(message.chat.id, 'Теперь ваше приведственное сообщение такое:\n'+StartMessageText)
   else:
      bot.send_message(message.chat.id, 'Ошибка в команде, попробуйте еще!')


@bot.message_handler(commands=['bot_setup'])
def BotSetupF(message):
   #Настраиваем бота на своего
   #Если пароль верный то меняем данные
   global PasswordSetting
   global ChatId
   global TOKEN
   global bot
   if(PasswordSetting==message.text[11:20]):
      #TOKEN=message.text[21:]
      ChatId=message.chat.id #Присвоили номер чата в который будут приходить все сообщения
      #bot=telebot.TeleBot(TOKEN)
      bot.send_message(message.chat.id, 'Теперь в этот чат будут приходить сообщения из других ботов:\n'+TOKEN)
   else:
      bot.send_message(message.chat.id, 'Ошибка в команде, попробуйте еще!')


@bot.message_handler(content_types=['text'])
def IdeamessageText(message):
   global TypeMessage
   global UserNameMessage
   global ChatId
   if((UserNameMessage!=message.from_user.username)or(TypeMessage!=1)):
      bot.send_message(ChatId, '@'+message.from_user.username+' написал: \n'+message.text)
   else:
      bot.send_message(ChatId, message.text)
   UserNameMessage=message.from_user.username
   TypeMessage=1
   print(TOKEN)
   

@bot.message_handler(content_types=['audio'])
def IdeamessageAudoi(message):
   global TypeMessage
   global UserNameMessage
   global ChatId
   if((UserNameMessage!=message.from_user.username)or(TypeMessage!=2)):
      bot.send_message(ChatId, '@'+message.from_user.username+' отправил аудио: \n')
      bot.send_audio(ChatId, message.audio.file_id, message.caption)
   else:
      bot.send_audio(ChatId, message.audio.file_id, message.caption)
   UserNameMessage=message.from_user.username
   TypeMessage=2


@bot.message_handler(content_types=['document'])
def IdeamessageDocument(message):
   global TypeMessage
   global UserNameMessage
   global ChatId
   if((UserNameMessage!=message.from_user.username)or(TypeMessage!=3)):
      bot.send_message(ChatId, '@'+message.from_user.username+' отправил документ: \n')
      bot.send_document(ChatId, message.document.file_id, message.caption)
   else:
      bot.send_document(ChatId, message.document.file_id, message.caption)
   UserNameMessage=message.from_user.username
   TypeMessage=3


@bot.message_handler(content_types=['photo'])
def IdeamessagePhoto(message):
   global TypeMessage
   global UserNameMessage
   global ChatId
   if((UserNameMessage!=message.from_user.username)or(TypeMessage!=4)):
      bot.send_message(ChatId, '@'+message.from_user.username+' отправил фото: \n')
      bot.send_photo(ChatId, message.photo[len(message.photo)-1].file_id, message.caption)
   else:
      bot.send_photo(ChatId, message.photo[len(message.photo)-1].file_id, message.caption)
   UserNameMessage=message.from_user.username
   TypeMessage=4


@bot.message_handler(content_types=['sticker'])
def IdeamessageSticker(message):
   global TypeMessage
   global UserNameMessage
   global ChatId
   #print(message)
   if((UserNameMessage!=message.from_user.username)or(TypeMessage!=5)):
      bot.send_message(ChatId, '@'+message.from_user.username+' отправил стикер: \n')
      bot.send_sticker(ChatId, message.sticker.file_id)
   else:
      bot.send_sticker(ChatId, message.sticker.file_id)
   UserNameMessage=message.from_user.username
   TypeMessage=5


@bot.message_handler(content_types=['video'])
def IdeamessageVideo(message):
   global TypeMessage
   global UserNameMessage
   global ChatId
   if((UserNameMessage!=message.from_user.username)or(TypeMessage!=6)):
      bot.send_message(ChatId, '@'+message.from_user.username+' отправил видео: \n')
      bot.send_video(ChatId, message.video.file_id, message.caption)
   else:
      bot.send_video(ChatId, message.video.file_id, message.caption)
   UserNameMessage=message.from_user.username
   TypeMessage=6


@bot.message_handler(content_types=['video_note'])
def IdeamessageVideoNote(message):
   global TypeMessage
   global UserNameMessage
   global ChatId
   if((UserNameMessage!=message.from_user.username)or(TypeMessage!=7)):
      bot.send_message(ChatId, '@'+message.from_user.username+' отправил видеосообщение: \n')
      bot.send_video_note(ChatId, message.video_note.file_id)
   else:
      bot.send_video_note(ChatId, message.video_note.file_id)
   UserNameMessage=message.from_user.username
   TypeMessage=7


@bot.message_handler(content_types=['voice'])
def IdeamessageVoice(message):
   global TypeMessage
   global UserNameMessage
   global ChatId
   if((UserNameMessage!=message.from_user.username)or(TypeMessage!=8)):
      bot.send_message(ChatId, '@'+message.from_user.username+' отправил аудиосообщение: \n')
      bot.send_voice(ChatId, message.voice.file_id, message.caption)
   else:
      bot.send_voice(ChatId, message.voice.file_id, message.caption)
   UserNameMessage=message.from_user.username
   TypeMessage=8
#RUN
bot.polling(none_stop=True)