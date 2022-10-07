import telebot
import config
from deep_translator import GoogleTranslator
from murkups import *
bot = telebot.TeleBot(config.API_TOKEN)

# Translate Function


#en_ru translate
def en_ru(message):
    try:
        text = int(message.text)
        bot.send_message(message.chat.id, "Iltimos Matn Kiriting")
    except:
        text =  message.text
        result = GoogleTranslator(source='en',target='ru').translate(text)
        bot.send_message(message.chat.id, result)

#ru_en tranlate
def ru_en(message):
    try:
        text = int(message.text)
        bot.send_message(message.chat.id, "Iltimos Matn Kiriting")
    except:
        text =  message.text
        result = GoogleTranslator(source='ru',target='en').translate(text)
        bot.send_message(message.chat.id, result)


#en_uz tranlate
def en_uz(message):
    try:
        text = int(message.text)
        bot.send_message(message.chat.id, "Iltimos Matn Kiriting")
    except:
        text =  message.text
        result = GoogleTranslator(source='en',target='uz').translate(text)
        bot.send_message(message.chat.id, result)

#uz_en tranlate
def uz_en(message):
    try:
        text = int(message.text)
        bot.send_message(message.chat.id, "Iltimos Matn Kiriting")
    except:
        text =  message.text
        result = GoogleTranslator(source='uz',target='en').translate(text)
        bot.send_message(message.chat.id, result)

#ru_uz tranlate
def ru_uz(message):
    try:
        text = int(message.text)
        bot.send_message(message.chat.id, "Iltimos Matn Kiriting")
    except:
        text =  message.text
        result = GoogleTranslator(source='ru',target='uz').translate(text)
        bot.send_message(message.chat.id, result)

#uz_ru tranlate
def uz_ru(message):
    try:
        text = int(message.text)
        bot.send_message(message.chat.id, "Iltimos Matn Kiriting")
    except:
        text =  message.text
        result = GoogleTranslator(source='uz',target='ru').translate(text)
        bot.send_message(message.chat.id, result)




@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, f"Assalomu Aleykum {message.from_user.full_name} Translator Botga hush kelibsiz\nMatnlarni tarjima qilish uchun /transelate buyrug'ini bering")

@bot.message_handler(commands=['transelate'])
def transelate(message):
	bot.send_message(message.chat.id,"Tarjima qilishni boshlang",reply_markup=main_menu)

@bot.callback_query_handler(func=lambda call:True)
def query_hendler(call):
	bot.answer_callback_query(callback_query_id=call.id)
	if call.data == 'trans':
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Tarjima Uchun Tilni Tanlang", reply_markup = tranlate_menu)
	elif call.data == 'ru_en':
		msg = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Tarjima uchun matn kiriting", reply_markup = quit_menu)
		bot.register_next_step_handler(msg, ru_en) 
	elif call.data == 'en_ru':
		msg = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Tarjima uchun matn kiriting", reply_markup = quit_menu)
		bot.register_next_step_handler(msg, en_ru)
	elif call.data == 'uz_en':
		msg = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Tarjima uchun matn kiriting", reply_markup = quit_menu)
		bot.register_next_step_handler(msg, uz_en)
	elif call.data == 'en_uz':
		msg = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Tarjima uchun matn kiriting", reply_markup = quit_menu)
		bot.register_next_step_handler(msg, en_uz)
	elif call.data == 'uz_ru':
		msg = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Tarjima uchun matn kiriting", reply_markup = quit_menu)
		bot.register_next_step_handler(msg, uz_ru)
	elif call.data == 'ru_uz':
		msg = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Tarjima uchun matn kiriting", reply_markup = quit_menu)
		bot.register_next_step_handler(msg, ru_uz)
	elif call.data == 'quit':
		msg = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Barcha amallar bekor qilindi", reply_markup = main_menu)
	elif call.data == 'back':
		msg = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Tarjima qilish uchun boshqa tilni tanlang", reply_markup = tranlate_menu)
	
		

bot.infinity_polling()