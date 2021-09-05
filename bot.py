import telebot
import config
import sqlite3
from telegram import ParseMode
from string import Template
from telebot import types
import button as btn

print("Bot ishga tushdi .....")
bot = telebot.TeleBot(config.TOKEN)

user_dict = {}
class User:
    def __init__(self, city):
        self.city = city

        keys = ['first_name', 'last_name', 'phone', 'regular_customer']
        
        for key in keys:
            self.key = None

price = 12000
size_dict = {}
class Users:
    def __init__(self, name):
        self.name = name
        self.lengh = None
        self.latitude = None
        self.sex = None


# Botga start berilganidagi kamanda va uni bajaradigan fungsiyaalri
@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message):
    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    user_info = message.from_user.id
    cursor.execute(f"SELECT id FROM frontend_user_info WHERE chat_id = {user_info}")
    data = cursor.fetchone()
    if data is None:
        user_id = [message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.language_code, message.chat.id, message.date, message.text]
        cursor.execute("INSERT INTO frontend_user_info(first_name, last_name, username, language_code, chat_id,   message_date, user_text) VALUES(?, ?, ?, ?, ?, ?, ?)", user_id)
        connect.commit()
        bot.send_message(message.from_user.id, f" <b>{message.from_user.full_name}</b> <i>Siz bizning bazamizga qo'shildingiz</i> ", parse_mode=ParseMode.HTML)
    else:
        bot.send_message(message.chat.id, f" <i> Bizning hizmatimizdan yana bir bor foydalanayotganingizdan mamnunmiz </i> <b> {message.from_user.first_name}  </b>", parse_mode=ParseMode.HTML)
    bot.send_photo(message.from_user.id, config.hello_image_id, caption=f"Привет <b>{message.from_user.first_name}</b>", parse_mode=ParseMode.HTML)
    bot.send_message(message.from_user.id, " <b> 🇺🇿 O'zingizga qulay tilni tanlang, </b>\n\n"
                                                 " <b>🇷🇺 Выберите язык, который вам подходит </b>\n\n"
                                                 " <b>🇺🇸 Choose a language that suits you </b>", reply_markup=btn.language_btn_inline , parse_mode=ParseMode.HTML)

@bot.message_handler(commands=['delete'])
def delete(message: types.Message):
    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    userID = message.chat.id
    cursor.execute(f"DELETE FROM frontend_user_info WHERE chat_id = {userID}")
    connect.commit()
    bot.send_message(message.from_user.id, "Siz bazamizdan o'chirildingiz..")

@bot.message_handler(commands=["reg_uz"])
def user_reg_uz(message):
    msg = bot.send_message(message.chat.id, "📌 Qayerdansiz?", reply_markup=btn.location_uz_button)
    bot.register_next_step_handler(msg, process_city_step_uz)

def process_city_step_uz(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(chat_id, "👤 Ismingiz", reply_markup=markup)
        bot.register_next_step_handler(msg, process_first_name_step_uz)

    except Exception as e:
        bot.reply_to(message, '🤖 Xatolik yuz berdi')

def process_first_name_step_uz(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.first_name = message.text

        msg = bot.send_message(chat_id,  "👤 Familiyangiz")
        bot.register_next_step_handler(msg, process_last_name_step_uz)

    except Exception as e:
        bot.reply_to(message, '🤖 xatolik yuz berdi')

def process_last_name_step_uz(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.last_name = message.text

        msg = bot.send_message(chat_id, "📞 Telefon raqamingiz (+998)")
        bot.register_next_step_handler(msg, process_phone_step_uz)

    except Exception as e:
        bot.reply_to(message, '🤖 xatolik yuz berdi')

def process_phone_step_uz(message):
    try:
        int(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        msg = bot.send_message(chat_id, "Bizni hizmatimizdan avval ham foydalanganmisiz?", reply_markup=btn.regular_customer_uz)
        bot.register_next_step_handler(msg, process_thank_step_uz)

    except Exception as e:
        msg = bot.reply_to(message, "Iltimos telefon raqamingizni to'g'ri kiriting")
        bot.register_next_step_handler(msg, process_phone_step_uz)

def process_thank_step_uz(message):
    try:
        chat_id = message.chat.id
        if message.text == "Xa" or message.text == "Yo'q":
            user = user_dict[chat_id]
            user.regular_customer = message.text
            bot.send_photo(chat_id, photo=config.logo_id, caption=getRegData_uz(user, "🤖 Sizning buyurtmangiz: ", message.from_user.first_name), parse_mode="Markdown",reply_markup=btn.about_uz )
            bot.send_photo(config.chat_id, photo=config.logo_id,  caption=getRegData_uz(user, '🤖 Buyurtma botdan: ', bot.get_me().username), parse_mode="Markdown")
            bot.send_photo(config.gruppa_id, photo=config.logo_id,  caption=getRegData_uz(user, '🤖 Buyurtma botdan: ', bot.get_me().username), parse_mode="Markdown")
        else:
            msg = bot.send_message(chat_id, "Iltmos quyidagi javoblardan birini tanlang")
            bot.register_next_step_handler(msg, process_thank_step_uz)
    except Exception as e:
        msg = bot.send_message(chat_id, "Iltmos quyidagi javoblardan birini tanlang")
        bot.register_next_step_handler(msg, process_thank_step_uz)

def getRegData_uz(user, title, name):
    t = Template("$title *$name* \n\n📌 Manzil: *$userCity* \n\n👤 Ism: *$first_name* \n\n👤 Familiya: *$last_name* \n\n📞 Telefon: *$phone*  \n\n✅  Doimiy mijoz: *$regular_customer* ")

    return t.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone': user.phone,
        'regular_customer': user.regular_customer,
    })

# Registratsiya ruschada 
@bot.message_handler(commands=["reg_ru"])
def user_reg_ru(message):
    msg = bot.send_message(message.chat.id, "📌 Вы откуда ?", reply_markup=btn.location_uz_button)
    bot.register_next_step_handler(msg, process_city_step_ru)

def process_city_step_ru(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(chat_id, "👤 Ваше имя", reply_markup=markup)
        bot.register_next_step_handler(msg, process_first_name_step_ru)

    except Exception as e:
        bot.reply_to(message, '🤖 Произошла ошибка')

def process_first_name_step_ru(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.first_name = message.text

        msg = bot.send_message(chat_id,  "👤 Ваша фамилия")
        bot.register_next_step_handler(msg, process_last_name_step_ru)

    except Exception as e:
        bot.reply_to(message, '🤖 Произошла ошибка')

def process_last_name_step_ru(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.last_name = message.text

        msg = bot.send_message(chat_id, "📞 Ваш номер телефона (+998)")
        bot.register_next_step_handler(msg, process_phone_step_ru)

    except Exception as e:
        bot.reply_to(message, '🤖 Произошла ошибка')

def process_phone_step_ru(message):
    try:
        int(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        msg = bot.send_message(chat_id, "Вы раньше пользовались нашим сервисом?", reply_markup=btn.regular_customer_ru)
        bot.register_next_step_handler(msg, process_thank_step_ru)

    except Exception as e:
        msg = bot.reply_to(message, "Пожалуйста, введите свой номер телефона правильно")
        bot.register_next_step_handler(msg, process_phone_step_ru)

def process_thank_step_ru(message):
    try:
        chat_id = message.chat.id
        if message.text == "Да" or message.text == "Нет":
            user = user_dict[chat_id]
            user.regular_customer = message.text
            bot.send_photo(chat_id, photo=config.logo_id, caption=getRegData(user, "🤖 Твои заказ: ", message.from_user.first_name), parse_mode="Markdown",reply_markup=btn.about_ru )
            bot.send_photo(config.chat_id, photo=config.logo_id,  caption=getRegData(user, '🤖 Заказ от бота: ', bot.get_me().username), parse_mode="Markdown")
            bot.send_photo(config.gruppa_id, photo=config.logo_id,  caption=getRegData(user, '🤖 Заказ от бота: ', bot.get_me().username), parse_mode="Markdown")
        else:
            msg = bot.send_message(chat_id, "Пожалуйста, выберите один из следующих ответов")
            bot.register_next_step_handler(msg, process_thank_step_ru)
    except Exception as e:
        msg = bot.send_message(chat_id, "Пожалуйста, выберите один из следующих ответов")
        bot.register_next_step_handler(msg, process_thank_step_ru)

def getRegData(user, title, name):
    t = Template("$title *$name* \n\n📌 Адрес: *$userCity* \n\n👤 Имя: *$first_name* \n\n👤 Фамилия: *$last_name* \n\n📞 Телефон: *$phone*  \n\n✅  Постоянный клиент: *$regular_customer* ")

    return t.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone': user.phone,
        'regular_customer': user.regular_customer,
    })

# Registratsiya english
@bot.message_handler(commands=["reg_en"])
def user_reg_en(message):
    msg = bot.send_message(message.chat.id, "📌 Where are you from ?", reply_markup=btn.location_uz_button)
    bot.register_next_step_handler(msg, process_city_step_en)

def process_city_step_en(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(chat_id, "👤 Your name", reply_markup=markup)
        bot.register_next_step_handler(msg, process_first_name_step_en)

    except Exception as e:
        bot.reply_to(message, '🤖 An error has occurred')

def process_first_name_step_en(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.first_name = message.text

        msg = bot.send_message(chat_id,  "👤 Your surname")
        bot.register_next_step_handler(msg, process_last_name_step_en)

    except Exception as e:
        bot.reply_to(message, '🤖 An error has occurred')

def process_last_name_step_en(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.last_name = message.text

        msg = bot.send_message(chat_id, "📞 Your phone number (+998)")
        bot.register_next_step_handler(msg, process_phone_step_en)

    except Exception as e:
        bot.reply_to(message, '🤖 An error has occurred')

def process_phone_step_en(message):
    try:
        int(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        msg = bot.send_message(chat_id, "Have you used our service before?", reply_markup=btn.regular_customer_en)
        bot.register_next_step_handler(msg, process_thank_step_en)

    except Exception as e:
        msg = bot.reply_to(message, "Please enter your phone number correctly")
        bot.register_next_step_handler(msg, process_phone_step_en)

def process_thank_step_en(message):
    try:
        chat_id = message.chat.id
        if message.text == "Yes" or message.text == "No":
            user = user_dict[chat_id]
            user.regular_customer = message.text
            bot.send_photo(chat_id, photo=config.logo_id, caption=getRegData(user, "🤖 Your order: ", message.from_user.first_name), parse_mode="Markdown",reply_markup=btn.about_en )
            bot.send_photo(config.chat_id, photo=config.logo_id,  caption=getRegData(user, '🤖 Bot order: ', bot.get_me().username), parse_mode="Markdown")
            bot.send_photo(config.gruppa_id, photo=config.logo_id,  caption=getRegData(user, '🤖 Bot order: ', bot.get_me().username), parse_mode="Markdown")
        else:
            msg = bot.send_message(chat_id, "Please choose one of the following answers")
            bot.register_next_step_handler(msg, process_thank_step_en)
    except Exception as e:
        msg = bot.send_message(chat_id, "Please choose one of the following answers")
        bot.register_next_step_handler(msg, process_thank_step_en)

def getRegData(user, title, name):
    t = Template("$title *$name* \n\n📌 Address: *$userCity* \n\n👤 Name: *$first_name* \n\n👤 Surname: *$last_name* \n\n📞 Telephone: *$phone*  \n\n✅  Regular customer: *$regular_customer* ")

    return t.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone': user.phone,
        'regular_customer': user.regular_customer,
    })


# Registratsiya Uzbekcha Krill
@bot.message_handler(commands=["reg_uz_krill"])
def user_reg_uz_krill(message):
    msg = bot.send_message(message.chat.id, "📌 Қаердансиз?", reply_markup=btn.location__uz_krill_button)
    bot.register_next_step_handler(msg, process_city_step_uz_krill)

def process_city_step_uz_krill(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(chat_id, "👤 Исмингиз", reply_markup=markup)
        bot.register_next_step_handler(msg, process_first_name_step_uz_krill)

    except Exception as e:
        bot.reply_to(message, '🤖 Хатолик юз берди')

def process_first_name_step_uz_krill(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.first_name = message.text

        msg = bot.send_message(chat_id,  "👤 Фамилиянгиз")
        bot.register_next_step_handler(msg, process_last_name_step_uz_krill)

    except Exception as e:
        bot.reply_to(message, '🤖 Хатолик юз берди')

def process_last_name_step_uz_krill(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.last_name = message.text

        msg = bot.send_message(chat_id, "📞 Телефон рақамингиз (+998)")
        bot.register_next_step_handler(msg, process_phone_step_uz_krill)

    except Exception as e:
        bot.reply_to(message, '🤖 Хатолик юз берди')

def process_phone_step_uz_krill(message):
    try:
        int(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        msg = bot.send_message(chat_id, "Бизни ҳизматимиздан аввал ҳам фойдаланганмисиз?", reply_markup=btn.regular_customer_uz_krill)
        bot.register_next_step_handler(msg, process_thank_step_uz_krill)

    except Exception as e:
        msg = bot.reply_to(message, "Илтимос телефон рақамингизни тўғри киритинг")
        bot.register_next_step_handler(msg, process_phone_step_uz_krill)

def process_thank_step_uz_krill(message):
    try:
        chat_id = message.chat.id
        if message.text == "Ҳа" or message.text == "Йўқ":
            user = user_dict[chat_id]
            user.regular_customer = message.text
            bot.send_photo(chat_id, photo=config.logo_id, caption=getRegData(user, "🤖 Сизнинг буюртмангиз: ", message.from_user.first_name), parse_mode="Markdown",reply_markup=btn.about_uz_kril )
            bot.send_photo(config.chat_id, photo=config.logo_id,  caption=getRegData(user, '🤖 Буюртма ботдан: ', bot.get_me().username), parse_mode="Markdown")
            bot.send_photo(config.gruppa_id, photo=config.logo_id,  caption=getRegData(user, '🤖 Буюртма ботдан: ', bot.get_me().username), parse_mode="Markdown")
        else:
            msg = bot.send_message(chat_id, "Илтимос, қуйидаги жавоблардан бирини танланг")
            bot.register_next_step_handler(msg, process_thank_step_uz_krill)
    except Exception as e:
        msg = bot.send_message(chat_id, "Илтимос, қуйидаги жавоблардан бирини танланг")
        bot.register_next_step_handler(msg, process_thank_step_uz_krill)

def getRegData(user, title, name):
    t = Template("$title *$name* \n\n📌 Манзил: *$userCity* \n\n👤 Исм: *$first_name* \n\n👤 Фамилия: *$last_name* \n\n📞 Телефон: *$phone*  \n\n✅  Доимий мижоз: *$regular_customer* ")

    return t.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone': user.phone,
        'regular_customer': user.regular_customer,
    })





# Calculator_o'zbeckhada
@bot.message_handler(commands=["calculator_uz"])
def send_welcome(message):
    msg = bot.reply_to(message, "👤 Ismingiz")
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = Users(name)
        size_dict[chat_id] = user
        msg = bot.reply_to(message, '🧮 Gilam uzunligi')
        bot.register_next_step_handler(msg, process_uzunligi_step)
    except Exception as e:
        bot.reply_to(message, '🤖 xatolik yuz berdi')

def process_uzunligi_step(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        lengh = message.text
        user = size_dict[chat_id]
        user.lengh = lengh
        msg = bot.reply_to(message, "🧮 Gilam kengilgini kirting")
        bot.register_next_step_handler(msg, process_kengligi_step)
    except Exception as e:
        msg = bot.reply_to(message, '🤖 Iltmos gilam uzunligi qaytadan kiriting raqam bilan, Misol: 6')
        bot.register_next_step_handler(msg, process_uzunligi_step)

def process_kengligi_step(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        latitude = message.text
        user = size_dict[chat_id]
        user.latitude = latitude
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("Xa", "Yo'q")
        msg = bot.reply_to(message, "🤖 Natijani ko'rishni xoxlaysizmi ?", reply_markup=markup)
        bot.register_next_step_handler(msg, process_javob_step)
    except Exception as e:
        msg = bot.reply_to(message, "🤖 Iltmos gilam kengilgini qaytadan kiriting raqam bilan, Misol: 6")
        bot.register_next_step_handler(msg, process_kengligi_step)

def process_javob_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = size_dict[chat_id]
        if (sex == u"Xa") or (sex == u"Yo'q"):
            user.sex = sex
        else:
            raise Exception("Mavjud bo'lmagan javob")
        javob = int(user.lengh) * int(user.latitude)
        narxi = javob * price
        onvert = "{:,}".format(narxi)
        caption = f"🤖 Sizning gilamingiz: <b>{javob} kv.m </b> \n\n <i>💵 Narxi: </i> <b>{onvert} so'm</b>"
        bot.send_photo(chat_id, photo=config.yang_woo_image_id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=btn.about_uz)
    except Exception as e:
        bot.reply_to(message, '🤖 Xatolik yuz berdi!!!')


# Calculator_Ruschada
@bot.message_handler(commands=["calculator_ru"])
def send_welcome_ru(message):
    msg = bot.reply_to(message, "👤 Ваше имя")
    bot.register_next_step_handler(msg, process_name_step_ru)

def process_name_step_ru(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = Users(name)
        size_dict[chat_id] = user
        msg = bot.reply_to(message, '🧮 Длина ковра')
        bot.register_next_step_handler(msg, process_uzunligi_step_ru)
    except Exception as e:
        bot.reply_to(message, '🤖 Произошла ошибка')

def process_uzunligi_step_ru(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        lengh = message.text
        user = size_dict[chat_id]
        user.lengh = lengh
        msg = bot.reply_to(message, "🧮 Введите ширину ковра")
        bot.register_next_step_handler(msg, process_kengligi_step_ru)
    except Exception as e:
        msg = bot.reply_to(message, '🤖 Введите число еще раз, указав длину коврика, например: 6.')
        bot.register_next_step_handler(msg, process_uzunligi_step_ru)

def process_kengligi_step_ru(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        latitude = message.text
        user = size_dict[chat_id]
        user.latitude = latitude
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("Да", "Нет")
        msg = bot.reply_to(message, "🤖 Хотите увидеть результат?", reply_markup=markup)
        bot.register_next_step_handler(msg, process_javob_step_ru)
    except Exception as e:
        msg = bot.reply_to(message, "🤖 Введите число еще раз ширину ковра, например: 6")
        bot.register_next_step_handler(msg, process_kengligi_step_ru)

def process_javob_step_ru(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = size_dict[chat_id]
        if (sex == u"Да") or (sex == u"Нет"):
            user.sex = sex
        else:
            raise Exception("Несуществующий ответ")
        javob = int(user.lengh) * int(user.latitude)
        narxi = javob * price
        onvert = "{:,}".format(narxi)
        caption = f"🤖 Ваш ковер: <b>{javob} кв.м </b> \n\n <i>💵 Цена: </i> <b>{onvert} сум</b>"
        bot.send_photo(chat_id, photo=config.yang_woo_image_ru_id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=btn.about_ru)
    except Exception as e:
        bot.reply_to(message, '🤖 Произошла ошибка')


# Calculator_English
@bot.message_handler(commands=["calculator_en"])
def send_welcome_en(message):
    msg = bot.reply_to(message, "👤 Your name")
    bot.register_next_step_handler(msg, process_name_step_en)

def process_name_step_en(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = Users(name)
        size_dict[chat_id] = user
        msg = bot.reply_to(message, '🧮 Carpet length')
        bot.register_next_step_handler(msg, process_uzunligi_step_en)
    except Exception as e:
        bot.reply_to(message, '🤖 An error has occurred')

def process_uzunligi_step_en(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        lengh = message.text
        user = size_dict[chat_id]
        user.lengh = lengh
        msg = bot.reply_to(message, "🧮 Enter the width of the carpet")
        bot.register_next_step_handler(msg, process_kengligi_step_en)
    except Exception as e:
        msg = bot.reply_to(message, '🤖 Re-enter the number using the length of the rug, for example: 6.')
        bot.register_next_step_handler(msg, process_uzunligi_step_en)

def process_kengligi_step_en(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        latitude = message.text
        user = size_dict[chat_id]
        user.latitude = latitude
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("Yes", "No")
        msg = bot.reply_to(message, "🤖 Want to see the result?", reply_markup=markup)
        bot.register_next_step_handler(msg, process_javob_step_en)
    except Exception as e:
        msg = bot.reply_to(message, "🤖 Enter the number again the width of the carpet, for example: 6")
        bot.register_next_step_handler(msg, process_kengligi_step_en)

def process_javob_step_en(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = size_dict[chat_id]
        if (sex == u"Yes") or (sex == u"No"):
            user.sex = sex
        else:
            raise Exception("Non-existent answer")
        javob = int(user.lengh) * int(user.latitude)
        narxi = javob * price
        onvert = "{:,}".format(narxi)
        caption = f"🤖 Your carpet: <b>{javob} sq.m </b> \n\n <i>💵 Price: </i> <b>{onvert} sum</b>"
        bot.send_photo(chat_id, photo=config.yang_woo_image_en_id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=btn.about_en)
    except Exception as e:
        bot.reply_to(message, '🤖 An error has occurred')


# Calculator_O'zbeckha kirilcha
@bot.message_handler(commands=["calculator_uz_krill"])
def send_welcome_uz_krill(message):
    msg = bot.reply_to(message, "👤 Исмингиз ?")
    bot.register_next_step_handler(msg, process_name_step_uz_krill)

def process_name_step_uz_krill(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = Users(name)
        size_dict[chat_id] = user
        msg = bot.reply_to(message, '🧮 Гилам узунлиги')
        bot.register_next_step_handler(msg, process_uzunligi_step_uz_krill)
    except Exception as e:
        bot.reply_to(message, '🤖 Хатолик юз берди')

def process_uzunligi_step_uz_krill(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        lengh = message.text
        user = size_dict[chat_id]
        user.lengh = lengh
        msg = bot.reply_to(message, "🧮 Гиламнинг кенглигини киритинг")
        bot.register_next_step_handler(msg, process_kengligi_step_uz_krill)
    except Exception as e:
        msg = bot.reply_to(message, '🤖 Гилам узунлигидан фойдаланиб, рақамни қайта киритинг, масалан: 6.')
        bot.register_next_step_handler(msg, process_uzunligi_step_uz_krill)

def process_kengligi_step_uz_krill(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        latitude = message.text
        user = size_dict[chat_id]
        user.latitude = latitude
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("Ҳа", "Йўқ")
        msg = bot.reply_to(message, "🤖 Натижани кўришни хоҳлайсизми?", reply_markup=markup)
        bot.register_next_step_handler(msg, process_javob_step_uz_krill)
    except Exception as e:
        msg = bot.reply_to(message, "🤖 Гилам кенглигидаги рақамни яна киритинг, масалан: 6")
        bot.register_next_step_handler(msg, process_kengligi_step_uz_krill)

def process_javob_step_uz_krill(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = size_dict[chat_id]
        if (sex == u"Ҳа") or (sex == u"Йўқ"):
            user.sex = sex
        else:
            raise Exception("Сиз берилган жавоблардан бирини киритинг")
        javob = int(user.lengh) * int(user.latitude)
        narxi = javob * price
        onvert = "{:,}".format(narxi)
        caption = f"🤖 Сизнинг гиламингиз: <b>{javob} кв.m </b> \n\n <i>💵 Нарх: </i> <b>{onvert} сўм</b>"
        bot.send_photo(chat_id, photo=config.yang_woo_image_uz_krill_id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=btn.about_uz_kril)
    except Exception as e:
        bot.reply_to(message, '🤖 Хатолик юз берди')



@bot.message_handler(commands=["help"])
def send_welcome(message):
    caption = "<b>Biz bilan bog'lanish uchun</b>"
    bot.send_photo(message.chat.id, photo=config.hellp_image_id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=btn.about_uz)


@bot.message_handler(commands=["contact"])
def send_welcome(message):
    caption = "Qanday yordam bera olaman ?"
    bot.send_photo(message.chat.id, photo=config.gilam_yuvish_id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=btn.about_uz)

@bot.message_handler(commands=["about"])
def send_welcome(message):
    caption = "<b>Biz haqimizda ko'proq biling kuzating do'stlaringizga ulshing \n\n 👨‍✈️ Bot ishlashi  uchun ➕ FOLLOW QILIB admin berishiz kerak ✅</b>"
    bot.send_photo(message.chat.id, photo=config.folow_image_id, caption=caption, parse_mode=ParseMode.HTML, reply_markup=btn.follow_btn)



@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    if call.data == "🇺🇿 O'zbekcha":
        bot.send_message(call.message.chat.id, "Kerakli bo'limni tanlang", reply_markup=btn.uzbMenu)

    if call.data == "🇷🇺 Русский":
        bot.send_message(call.message.chat.id, "Выберите нужный раздел", reply_markup=btn.rusMenu)

    if call.data == "🇺🇸 Enlish":
        bot.send_message(call.message.chat.id, "Выберите нужный раздел", reply_markup=btn.enMenu)

    if call.data == "🇺🇿 Узбекча":
        bot.send_message(call.message.chat.id, "Ўзингиз хоҳлаган бўлимни танланг", reply_markup=btn.uzbMenu_krill)

    if call.data == "buy_telegram_uz":
        msg = bot.send_message(call.message.chat.id, "Qayerdansiz?", reply_markup=btn.location_uz_button)
        bot.register_next_step_handler(msg, process_city_step_uz)

    if call.data == "buy_telegram_ru":
        msg = bot.send_message(call.message.chat.id, "Вы откуда ?", reply_markup=btn.location_ru_button)
        bot.register_next_step_handler(msg, process_city_step_ru)

    if call.data == "buy_telegram_en":
        msg = bot.send_message(call.message.chat.id, "Where are you from ?", reply_markup=btn.location_en_button)
        bot.register_next_step_handler(msg, process_city_step_en)


    if call.data == "buy_telegram_uz_krill":
        msg = bot.send_message(call.message.chat.id, "Where are you from ?", reply_markup=btn.location__uz_krill_button)
        bot.register_next_step_handler(msg, process_city_step_uz_krill)

    if call.data == "calculator_uz":
        msg = bot.reply_to(call.message, "Ismingiz")
        bot.register_next_step_handler(msg, process_name_step)

    if call.data == "calculator_ru":
        msg = bot.reply_to(call.message, "Ваше имя")
        bot.register_next_step_handler(msg, process_name_step_ru)

    if call.data == "calculator_en":
        msg = bot.reply_to(call.message, "Your name")
        bot.register_next_step_handler(msg, process_name_step_en)

    if call.data == "calculator_uz_krill":
        msg = bot.reply_to(call.message, "Исмингиз ?")
        bot.register_next_step_handler(msg, process_name_step_uz_krill)

    if call.data == "buy_website":
        bot.send_message(call.message.chat.id, url="google.com")



back = ["◀ Ortga", "◀ Ортга", "◀ Назад", "◀ Back"]
@bot.message_handler(content_types=["text"])
def text(message):
# 🇺🇿 O'zbekcha menulardagi buttonslar fungsiyalari
    if message.text == "🛒 Buyurtma berish":
        title = "<b>Sizning gilamizngiz 30 kv dan katta bo'lsa 10 % chegirma bor, \n Agar siz bizning doimiy mijozimiz bo'lsangiz 10 % chegirma bor</b>"
        xizmat_turi = "<i>Buyurtma berish uchun o'zingizga qulay usulni tanlang! 🤖 </i>"
        convert = "{:,}".format(price)
        caption = f"{title} \n <b> Gilam yuvish narxi 1 kv: </b> <i> {convert} So'm </i> \n\n {xizmat_turi}"
        bot.send_photo(message.chat.id, config.gilam_yuvish_id, caption, parse_mode=ParseMode.HTML, reply_markup=btn.purchase_uz)

    if message.text == "📙 Biz haqimizda":
        title = "<b> Gilam yuvish firmasi haqida qisqacha ma'lumot </b>"
        website = "<a href='https://www.yangwoow.uz'>Kirish</a>"
        telegram_bot = "<a href='https://t.me/yang_woow_bot'>Bo'tni ko'rish</a>"
        telegram_channel = "<a href='https://t.me/yang_woow'>Bizga qo'shiling</a>"
        telegram_grupp = "<a href='https://t.me/joinchat/pVCTtnZpvaU1MTY6'>Guruhimizga qo'shiling</a>"
        call_number = "<a href='tel:+998955150999'>(+998) 955150999</a>"
        operator_1 = "<a href='tel:+998971130999'>(+998) 971130999</a>"
        operator_2 = "<a href='tel:+998971180999'>(+998) 971180999</a>"
        xizmat_turi = "<i>Bizning firma Yangiyo'ldagi №1 firma bo'lib. Siz azizlarga sfatli hizmat ko'rsatishdan mamnunmiz. Har bir oiladagi shinamlikda biznin hissamiz borligidan hursandmiz 😉 </i>"
        caption = f"❗️{title}❗️  \n\n {xizmat_turi} \n\n 🌏 <b>Veb -sayt:</b> {website} \n\n 🤖 <b>Telegram bot:</b> {telegram_bot} \n\n 🚀 <b>Telegram kanal:</b> {telegram_channel} \n\n 🚀 <b>Telegram gruppa:</b> {telegram_grupp} \n\n ☎️ <b>Coll-markaz:</b> {call_number} \n\n 📞 <b>Operator:</b> {operator_1} \n\n 📞 <b>Operator:</b> {operator_2}"
        bot.send_photo(message.from_user.id, config.logo_id, caption, parse_mode=ParseMode.HTML, reply_markup=btn.about_uz)

    if message.text == "💵 Xizmat narhlarini bilish":
        title = "<b> Gilamingizni o'zingiz hisoblang kv.m chiqarishni usulari ko'rsatilgan! </b>"
        xisoblash_info = "<i>Kenglikni uzunlikka ko'paytiring</i>"
        caption = f"{title} \n\n {xisoblash_info} "
        bot.send_photo(message.from_user.id, config.xisoblash_id, caption, parse_mode=ParseMode.HTML, reply_markup=btn.about_uz)

    if message.text in back:
        bot.send_message(message.chat.id, "😉", reply_markup=btn.language_btn_inline)

# 🇷🇺 Русский  menulardagi buttonslar fungsiyalari
    if message.text == "🛒 Заказ":
        title = "<b>Скидка 10 %, если ваш ковер больше 30 кв.м, \n Для постоянных клиентов действует скидка 10 %</b>"
        xizmat_turi = "<i>Выбирайте наиболее подходящий вам способ заказа! 🤖 </i>"
        convert = "{:,}".format(price)
        caption = f"{title} \n <b> Стоимость стирки ковров - 1 кв.м: </b> <i> {convert} Сум </i> \n\n {xizmat_turi}"
        bot.send_photo(message.from_user.id, config.gilam_yuvish_id, caption, parse_mode=ParseMode.HTML, reply_markup=btn.purchase_ru)
    
    if message.text == "📙 О нас":
        title = "<b> Краткая информация о компании по мойке ковров </b>"
        website = "<a href='https://www.yangwoow.uz'>Открыть</a>"
        telegram_bot = "<a href='https://t.me/yang_woow_bot'>Увидеть бота</a>"
        telegram_channel = "<a href='https://t.me/yang_woow'>Присоединяйтесь к нам</a>"
        telegram_grupp = "<a href='https://t.me/joinchat/pVCTtnZpvaU1MTY6'>Присоединяйтесь к нашей группе</a>"
        call_number = "<a href='tel:+998955150999'>(+998) 955150999</a>"
        operator_1 = "<a href='tel:+998971130999'>(+998) 971130999</a>"
        operator_2 = "<a href='tel:+998971180999'>(+998) 971180999</a>"
        xizmat_turi = "<i>Наша компания - компания №1 в Янгиюле. Мы рады предоставить вам качественный сервис. Мы рады внести свой вклад в благополучие каждой семьи.😉 </i>"
        caption = f"❗️{title}❗️  \n\n {xizmat_turi} \n\n 🌏 <b>Веб-сайт:</b> {website} \n\n 🤖 <b>Telegram бот:</b> {telegram_bot} \n\n 🚀 <b>Telegram канал:</b> {telegram_channel} \n\n 🚀 <b>Telegram группа:</b> {telegram_grupp} \n\n ☎️ <b>Колл-центр:</b> {call_number} \n\n 📞 <b>Оператор:</b> {operator_1} \n\n 📞 <b>Оператор:</b> {operator_2}"
        bot.send_photo(message.from_user.id, config.logo_id, caption, parse_mode=ParseMode.HTML, reply_markup=btn.rusMenu)

    if message.text == "💵 Знайте стоимость услуги":
        title = "<b> Рассчитайте свой ковер самостоятельно Как сделать квадратный метр показано! </b>"
        xisoblash_info = "<i>Умножьте ширину на длину</i>"
        caption = f"{title} \n\n {xisoblash_info} "
        bot.send_photo(message.from_user.id, config.xisoblash_id, caption, parse_mode=ParseMode.HTML, reply_markup=btn.about_ru)

# 🇺🇸 Enlish  menulardagi buttonslar fungsiyalari
    if message.text == "🛒 Order":
        title = "<b>10 % discount if your carpet is more than 30 sq.m., \n For regular customers there is a 10 % discount</b>"
        xizmat_turi = "<i>Choose the most suitable ordering method for you! 🤖 </i>"
        convert = "{:,}".format(price)
        caption = f"{title} \n <b> The cost of washing carpets - 1 sq. M: </b> <i> {convert} Soum </i> \n\n {xizmat_turi}"
        bot.send_photo(message.from_user.id, config.gilam_yuvish_id, caption, parse_mode=ParseMode.HTML, reply_markup=btn.purchase_en)

    if message.text == "📙 About Us":
        title = "<b> Brief information about the carpet washing company </b>"
        website = "<a href='https://www.yangwoow.uz'>Open</a>"
        telegram_bot = "<a href='https://t.me/yang_woow_bot'>See the bot</a>"
        telegram_channel = "<a href='https://t.me/yang_woow'>Join us</a>"
        telegram_grupp = "<a href='https://t.me/joinchat/pVCTtnZpvaU1MTY6'>Join our group</a>"
        call_number = "<a href='tel:+998955150999'>(+998) 955150999</a>"
        operator_1 = "<a href='tel:+998971130999'>(+998) 971130999</a>"
        operator_2 = "<a href='tel:+998971180999'>(+998) 971180999</a>"
        xizmat_turi = "<i>Our company is the number 1 company in Yangiyul. We are pleased to provide you with a quality service. We are happy to contribute to the well-being of every family.😉</i>"
        caption = f"❗️{title}❗️  \n\n {xizmat_turi} \n\n 🌏 <b>Веб-сайт:</b> {website} \n\n 🤖 <b>Telegram бот:</b> {telegram_bot} \n\n 🚀 <b>Telegram канал:</b> {telegram_channel} \n\n 🚀 <b>Telegram группа:</b> {telegram_grupp} \n\n ☎️ <b>Колл-центр:</b> {call_number} \n\n 📞 <b>Оператор:</b> {operator_1} \n\n 📞 <b>Оператор:</b> {operator_2}"
        bot.send_photo(message.from_user.id, config.logo_id, caption, parse_mode=ParseMode.HTML, reply_markup=btn.about_en)

    if message.text == "💵 Service charge":
        title = "<b> Calculate Your Rug Yourself How To Make The Square Meter Shown! </b>"
        xisoblash_info = "<i>Multiply width by length</i>"
        caption = f"{title} \n\n {xisoblash_info} "
        bot.send_photo(message.from_user.id, config.xisoblash_id, caption, parse_mode=ParseMode.HTML, reply_markup=btn.about_en)

# 🇺🇿 Узбекча  menulardagi buttonslar fungsiyalari
    if message.text == "🛒 Буюртма бериш":
        title = "<b>Сизнинг гиламизнгиз 30 кв дан катта бўлса 10 % чегирма бор, \n Агар сиз бизнинг доимий мижозимиз бўлсангиз 10 % чегирма бор</b>"
        xizmat_turi = "<i>Буюртма бериш учун ўзингизга қулай усулни танланг! 🤖 </i>"
        convert = "{:,}".format(price)
        caption = f"{title} \n <b> Гилам ювиш нархи 1 кв.м: </b> <i> {convert} Сўм </i> \n\n {xizmat_turi}"
        bot.send_photo(message.from_user.id, config.gilam_yuvish_id, caption, parse_mode=ParseMode.HTML, reply_markup=btn.purchase_uz_krill)

    if message.text == "📙 Биз ҳақимизда":
        title = "<b> Гилам ювиш фирмаси ҳақида қисқача маълумот </b>"
        website = "<a href='https://www.yangwoow.uz'>Кириш</a>"
        telegram_bot = "<a href='https://t.me/yang_woow_bot'>Бўтни кўриш</a>"
        telegram_channel = "<a href='https://t.me/yang_woow'>Бизга қўшилинг</a>"
        telegram_grupp = "<a href='https://t.me/joinchat/pVCTtnZpvaU1MTY6'>Гуруҳимизга қўшилинг</a>"
        call_number = "<a href='tel:+998955150999'>(+998) 955150999</a>"
        operator_1 = "<a href='tel:+998971130999'>(+998) 971130999</a>"
        operator_2 = "<a href='tel:+998971180999'>(+998) 971180999</a>"
        xizmat_turi = "<i>Бизнинг фирма Янгиёълдаги №1 фирма бўлиб. Сиз азизларга сфатли ҳизмат кўрсатишдан мамнунмиз. Ҳар бир оиладаги шинамликда бизнин ҳиссамиз борлигидан ҳурсандмиз 😉 </i>"
        caption = f"❗️{title}❗️  \n\n {xizmat_turi} \n\n 🌏 <b>Веб -сайт:</b> {website} \n\n 🤖 <b>Телеграм бот:</b> {telegram_bot} \n\n 🚀 <b>Телеграм канал:</b> {telegram_channel} \n\n 🚀 <b>Телеграм группа:</b> {telegram_grupp} \n\n ☎️ <b>Cолл-марказ:</b> {call_number} \n\n 📞 <b>Оператор:</b> {operator_1} \n\n 📞 <b>Оператор:</b> {operator_2}"
        bot.send_photo(message.from_user.id, config.logo_id, caption, parse_mode=ParseMode.HTML, reply_markup=btn.about_uz_kril)

    if message.text == "💵 Хизмат нарҳларини билиш":
        title = "<b> Гиламингизни ўзингиз ҳисобланг кв.м чиқаришни усулари кўрсатилган! </b>"
        xisoblash_info = "<i>Кенгликни узунликка кўпайтиринг</i>"
        caption = f"{title} \n\n {xisoblash_info} "
        bot.send_photo(message.from_user.id, config.xisoblash_id, caption, parse_mode=ParseMode.HTML, reply_markup=btn.about_uz_kril)


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
