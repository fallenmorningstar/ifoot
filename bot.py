import config
import telebot  # для работы с Telegram API
import time
import sqlite3
import markups
import db
from telebot import types

bot = telebot.TeleBot(config.token)
print(
    "-------------- iFoot bot started -------------"
)
hello = ('привет', 'приветик', 'здраствуй', 'здравствуй', 'здорова', 'здарова', 'шалом', 'hi', 'hello')
bay = ('пока', 'прощай', 'до завтра', 'до свидания генка', 'bay', 'досвидули')
sleep = ('спокойной ночи', 'сладких снов')
dela = ('как дела', 'как дела?', 'как дела?)', 'как делишки')
cool = ('клево', 'здорово', 'классно', 'здорово)', 'клево)', 'классно)', 'кайфово')


@bot.message_handler(commands=['start'])
def start_message(message):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM user WHERE chat_id=?"
    cursor.execute(sql, [(message.from_user.id)])
    user = cursor.fetchone()
    if not user:
        bot.send_message(message.chat.id, 'Здравствуйте! я бот iFoot - товары в шаговой доступности!\n'
                                          'Для работы нужно зарегестрироваться. 🤓',
                         reply_markup=markups.contact_keyboard)
    else:
        bot.send_message(message.chat.id,
                         "Мы предлагаем Вам использовать ниже перечисленные функции для поиска ближайших товаров и магазинов.\n"
                         "Вы можете искать товары по категориям и добавлять любимые места чтобы легче отслеживать информацию о товарах."
                         "\nПри желании, Вы можете оставить отзыв для разработчиков, мы обязательно учтем ваше мнение или пожелание :)",
                         reply_markup=markups.u_keyboard)


@bot.message_handler(commands=['delete'])
def delete_message(message):
    #    bot.delete_message(message.chat.id, message.message_id)
    print(message.message_id)
    for numid in range(message.message_id - 10, message.message_id - 1):
        bot.delete_message(message.chat.id, numid)


@bot.message_handler(content_types=['contact'])
def add_user(message):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    newdata = [
        (message.contact.user_id, message.contact.first_name, message.contact.last_name, message.contact.phone_number,'0')]
    cursor.executemany("INSERT INTO user VALUES (?,?,?,?,?)", newdata)
    conn.commit()
    bot.send_message(message.chat.id, 'Приятно познакомиться)', reply_markup=markups.u_keyboard)


# Ведем логи
def log(message, answer):
    print("\n---------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст = {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print("Ответ бота -", answer)


@bot.message_handler(content_types=["text"])
def send_text(message):
    try:
        text = message.text.lower()

        if text in hello:
            bot.send_message(message.chat.id,
                             'Привет,' + message.from_user.first_name + ')')

        elif text in bay:
            bot.send_message(message.chat.id, 'До встречи)')

        elif text in dela:
            bot.send_message(message.chat.id, 'Отлично')

        elif text == "🔍 поиск":
            s = "Что Вы хотите найти?"
            bot.send_message(message.chat.id, s, reply_markup=markups.search_keyboard)

        elif text == "📚 категории":
            s = "Что конкретно Вас интересует?"
            bot.send_message(message.chat.id, s, reply_markup=markups.menu_keyboard)

        elif text == "🏘 любимые места":
            s = "Какое любимое место Вам интересно?"
            bot.send_message(message.chat.id, s, reply_markup=markups.place_keyboard)

        elif text == '📝 обратная связь':
            s = "Напишите свои пожелания, мы обязательно примем к сведению Ваши мысли!"
            bot.send_message(message.chat.id, s, reply_markup=markups.feedback_keyboard)

        elif text == "главное меню":
            bot.send_message(message.chat.id, 'Вы в главном меню', reply_markup=markups.u_keyboard)
        else:
            bot.send_message(message.chat.id, 'Не понимаю, что вы имеете ввиду.')
    except Exception as e:
        print(" EERRRRROOOOOOOOOOOOOOOOOORRRRRRRRR", e)
        bot.reply_to(message, e)


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)
