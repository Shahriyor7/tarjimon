from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup


#tranlate_menu 
tranlate_menu = InlineKeyboardMarkup()
btn_ru_en = InlineKeyboardButton(text='RU ➡️ EN',callback_data='ru_en')
btn_en_ru = InlineKeyboardButton(text='EN ➡️ RU',callback_data='en_ru')
btn_uz_en = InlineKeyboardButton(text='UZ ➡️ EN',callback_data='uz_en')
btn_en_uz = InlineKeyboardButton(text='EN ➡️ UZ',callback_data='en_uz')
btn_uz_ru = InlineKeyboardButton(text='UZ ➡️ RU',callback_data='uz_ru')
btn_ru_uz = InlineKeyboardButton(text='RU ➡️ UZ',callback_data='ru_uz')
tranlate_menu.add(btn_ru_en,btn_uz_en,btn_uz_ru,btn_en_ru,btn_en_uz,btn_ru_uz)

#main_menu
main_menu = InlineKeyboardMarkup()
btnMenu = InlineKeyboardButton(text='🔄Tarjima',callback_data='trans')
main_menu.add(btnMenu)

#quit_menu
quit_menu = InlineKeyboardMarkup()
btnQuit = InlineKeyboardButton(text='❌Bekor Qilish',callback_data='quit')
btnBack = InlineKeyboardButton(text='📄Boshqa Til Tanlash',callback_data='back')
quit_menu.add(btnQuit,btnBack)