import telebot
import logging
import requests
from telebot import types

bot = telebot.TeleBot('728948247ASHJJJSH848247HJGG376183g_xRw')

@bot.message_handler(func=lambda msg: msg.text=='start' or msg.text=='slm')
def start(msg):
    bot.send_message(msg.chat.id,'slm koka')
    
    @bot.message_handler( func=lambda msg: True)
    def other(msg):
        bot.send_message(msg.chat.id,'no info')
        
        @bot.callback_query_handler(func=lambda msg:msg=True)
        def test_callback(msg):
            logger.info(msg)
            
            photo = open('/tmp/javad/photo.pnj','rb')
            bot.send_photo(chat_id,photo)
            bot.send_photo(chat_id,"FILEID")
            
            sti = open('/fds/sti.adm','rb')
            bot.send_sticker(chat_id,sti)
            bot.send_sticker(chat_id,"FILEID")
            
            file_info=bot.get_file(file_id)
            file= requests.get('https//api.telegram.org/file/bot{0}/{1}'.format(API_token,file_info.file_path))
            
            markup = types.ReplyKeyboardMarkup(row_width=2)
            itembtn1= types.KeyboardButton('a')
            itembtn2= types.KeyboardButton('b')
            itembtn3= types.KeyboardButton('c')
            markup.add(itembtn1,itembtn2,itembtn3)
            bot.send_message(chat_id,"choose one letter:",reply_markup=markup)
            
            bot.send_location(chat_id,lat ,lon)
            logger = telebot.logger
            telebot = logger.setlevel(logging.DEBUG)
            
            
            
    
    
    
  bot.infinity_polling()  
