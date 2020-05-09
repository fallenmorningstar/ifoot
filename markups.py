import telebot
from telebot import types

bot = telebot.TeleBot('1067190601:AAHYB0qvBpsQ9pIUiodEBI8iN5de71XM2IA')

# GET CONTACT
contact_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=1)
but = types.KeyboardButton(text='Отправить контакт', request_contact=True)
contact_keyboard.add(but)

# CHOOSE TYPE
type_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=1)
t_but1 = types.KeyboardButton(text='Пользователь')
t_but2 = types.KeyboardButton(text='Продавец')
type_keyboard.add(t_but1,t_but2)

# USER KEYBOARD
u_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=1)
u_keyboard.row('🔍 Поиск', '📚 Категории')
u_keyboard.row('🏘 Любимые места', '📝 Обратная связь')

# SEARCH
search_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=1)
search_keyboard.row('Главное меню')

# KATALOG
menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=1)
menu_keyboard.row('1', '2', '3', '4', '5')
menu_keyboard.row('Главное меню')

# FAVORITE PLACES
place_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=1)
place_keyboard.row('1', '2', '3', '4', '5')  # здесь нужен код, который при добавлении, будет индексировать места
place_keyboard.row('Добавить место')
place_keyboard.row('Удалить место')
place_keyboard.row('Главное меню')

# FEEDBACK
feedback_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=1)
feedback_keyboard.row('Главное меню')


