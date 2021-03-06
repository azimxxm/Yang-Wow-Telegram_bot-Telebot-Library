from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# KeyboardButton bu oddiy sms xabar orqali ishlovchi buttonlar


# Tilni tanlash uchun buttons lar inline
language_btn_inline = InlineKeyboardMarkup(row_width=2)
iteam1 = InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data= "🇺🇿 O'zbekcha")
iteam2 = InlineKeyboardButton(text="🇷🇺 Русский", callback_data= "🇷🇺 Русский")
iteam3 = InlineKeyboardButton(text="🇺🇸 Enlish", callback_data= "🇺🇸 Enlish")
iteam4 = InlineKeyboardButton(text="🇺🇿 Узбекча", callback_data= "🇺🇿 Узбекча")
language_btn_inline.add(iteam1, iteam2, iteam3, iteam4) 



# O'zbekcha bo'limidagi menular uchun buttonlar
menu1 = KeyboardButton("🛒 Buyurtma berish")
menu2 = KeyboardButton("📙 Biz haqimizda")
menu3 = KeyboardButton("💵 Xizmat narhlarini bilish")
menu4 = KeyboardButton("◀ Ortga")
uzbMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(menu1, menu2, menu3, menu4)
# endblock

# Krilcha bo'limidagi menular uchun buttonlar
menu1 = KeyboardButton("🛒 Буюртма бериш")
menu2 = KeyboardButton("📙 Биз ҳақимизда")
menu3 = KeyboardButton("💵 Хизмат нарҳларини билиш")
menu4 = KeyboardButton("◀ Ортга")
uzbMenu_krill = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(menu1, menu2, menu3, menu4)
# endblock


# Ruscha bo'limidagi menular uchun buttonlar
menu1 = KeyboardButton("🛒 Заказ")
menu2 = KeyboardButton("📙 О нас")
menu3 = KeyboardButton("💵 Знайте стоимость услуги")
menu4 = KeyboardButton("◀ Назад")
rusMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(menu1, menu2, menu3, menu4)
# endblock


# English bo'limidagi menular uchun buttonlar
menu1 = KeyboardButton("🛒 Order")
menu2 = KeyboardButton("📙 About Us")
menu3 = KeyboardButton("💵 Service charge")
menu4 = KeyboardButton("◀ Back")
enMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(menu1, menu2, menu3, menu4)
# endblock

# Registratsiya uzbekchada buttons 
location_uz_button = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn1 = KeyboardButton("Yangiyo'l shahar")
itembtn2 = KeyboardButton("Yangiyo'l tuman")
itembtn3 = KeyboardButton("Chinoz")
itembtn4 = KeyboardButton("Paxta")
location_uz_button.add(itembtn1, itembtn2, itembtn3, itembtn4)
# end block 

# Registratsiya uzbekchada buttons 
location_ru_button = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn1 = KeyboardButton("город Янгиюль")
itembtn2 = KeyboardButton("Янгиюльский район")
itembtn3 = KeyboardButton("Чиноз")
itembtn4 = KeyboardButton("Пахта")
location_ru_button.add(itembtn1, itembtn2, itembtn3, itembtn4)
# end block 

# Registratsiya English buttons 
location_en_button = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn1 = KeyboardButton("Yangiyul city")
itembtn2 = KeyboardButton("Yangiyul district")
itembtn3 = KeyboardButton("Chinoz")
itembtn4 = KeyboardButton("Paxta")
location_en_button.add(itembtn1, itembtn2, itembtn3, itembtn4)
# end block 

# Registratsiya Uzbek_krill buttons 
location__uz_krill_button = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn1 = KeyboardButton("Янгийўл шаҳар")
itembtn2 = KeyboardButton("Янгийўл туман")
itembtn3 = KeyboardButton("Чиноз")
itembtn4 = KeyboardButton("Пахта")
location__uz_krill_button.add(itembtn1, itembtn2, itembtn3, itembtn4)
# end block 



# Xizmatdan foydalangalik haqida so'rov uchun buttons
regular_customer_uz = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn1 = KeyboardButton("Xa")
itembtn2 = KeyboardButton("Yo'q")
regular_customer_uz.add(itembtn1, itembtn2)
# endblock 


# Xizmatdan foydalangalik haqida so'rov uchun buttons ruschadaa
regular_customer_ru = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn1 = KeyboardButton("Да")
itembtn2 = KeyboardButton("Нет")
regular_customer_ru.add(itembtn1, itembtn2)
# endblock 


# Xizmatdan foydalangalik haqida so'rov uchun buttons ruschadaa
regular_customer_en = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn1 = KeyboardButton("Yes")
itembtn2 = KeyboardButton("No")
regular_customer_en.add(itembtn1, itembtn2)
# endblock 

# Xizmatdan foydalangalik haqida so'rov uchun buttons Krilll
regular_customer_uz_krill = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn1 = KeyboardButton("Ҳа")
itembtn2 = KeyboardButton("Йўқ")
regular_customer_uz_krill.add(itembtn1, itembtn2)
# endblock 


# O'zbekcha Buyurtma berish uchun va website ga olib otadigan buttons
purchase_uz = InlineKeyboardMarkup(row_width=2)
order1 = InlineKeyboardButton(text="🛒 Telegram orqali 🚀 ",  callback_data="buy_telegram_uz")
order2 = InlineKeyboardButton(text="🌏 Website orqali 🚀 ", url="google.com", callback_data="buy_website")
order3 = InlineKeyboardButton(text="📟 Xisoblash 🚀 ",   callback_data="calculator_uz")
order4 = InlineKeyboardButton(text="📬 Izox qoldirish 🚀 ",  url="google.com", callback_data="comment")
purchase_uz.add(order1, order2, order3, order4)


# Ruscha Buyurtma berish uchun va website ga olib otadigan buttons 
purchase_ru = InlineKeyboardMarkup(row_width=2)
order1 = InlineKeyboardButton(text="🛒 Телеграммой🚀 ", callback_data="buy_telegram_ru")
order2 = InlineKeyboardButton(text="🌏 Через сайт 🚀 ", url="google.com", callback_data="buy_website")
order3 = InlineKeyboardButton(text="📟 Расчет 🚀 ",   callback_data="calculator_ru")
order4 = InlineKeyboardButton(text="📬 Оставить коментарий 🚀 ",  url="google.com", callback_data="comment")
purchase_ru.add(order1, order2, order3, order4)

# English  Buyurtma berish uchun va website ga olib otadigan buttons
purchase_en = InlineKeyboardMarkup(row_width=2)
order1 = InlineKeyboardButton(text="🛒 By telegram 🚀 ",  callback_data="buy_telegram_en")
order2 = InlineKeyboardButton(text="🌏 Through the site 🚀 ", url="google.com", callback_data="buy_website")
order3 = InlineKeyboardButton(text="📟 Calculation 🚀 ",   callback_data="calculator_en")
order4 = InlineKeyboardButton(text="📬 Leave a comment 🚀 ",  url="google.com", callback_data="comment")
purchase_en.add(order1, order2, order3, order4)


# Krilcha  Buyurtma berish uchun va website ga olib otadigan buttons
purchase_uz_krill = InlineKeyboardMarkup(row_width=2)
order1 = InlineKeyboardButton(text="🛒 Телеграм орқали 🚀 ",  callback_data="buy_telegram_uz_krill")
order2 = InlineKeyboardButton(text="🌏 Wеб-сайт орқали 🚀 ", url="google.com", callback_data="buy_website")
order3 = InlineKeyboardButton(text="📟 Хисоблаш 🚀 ",   callback_data="calculator_uz_krill")
order4 = InlineKeyboardButton(text="📬 Изох қолдириш 🚀 ",  url="google.com", callback_data="comment")
purchase_uz_krill.add(order1, order2, order3, order4)




# O'zbekcha Biz haqimizda bosilganida chiqadigan buttonslar
about_uz = InlineKeyboardMarkup(row_width=2)
order1 = InlineKeyboardButton(text="🌏 Veb-sayt 🚀", url="https://www.yangwoow.uz", callback_data="website")
order2 = InlineKeyboardButton(text="✅ Telegram gruppa 🚀 ", url="https://t.me/joinchat/pVCTtnZpvaU1MTY6",  callback_data="telegram_gruppa")
order3 = InlineKeyboardButton(text="☎️ Coll-center 🚀 ",  callback_data="call_center")
order4 = InlineKeyboardButton(text="✅ Telegram kanal 🚀 ",url="https://t.me/yang_woow" , callback_data="telegram_kanal")
order5 = InlineKeyboardButton(text="🛒 Buyurtma berish 🚀 ",  callback_data="buy_telegram")
order6 = InlineKeyboardButton(text="✅ Telegram bot 🚀 ", url="https://t.me/yang_woow_bot", callback_data="telegram_bot")
about_uz.add(order1, order2, order3, order4, order5, order6)

# Ruschada Biz haqimizda bosilganida chiqadigan buttonslar
about_ru = InlineKeyboardMarkup(row_width=2)
order1 = InlineKeyboardButton(text="🌏 Веб-сайт 🚀", url="https://www.yangwoow.uz", callback_data="website")
order2 = InlineKeyboardButton(text="✅ Telegram группа 🚀 ", url="https://t.me/joinchat/pVCTtnZpvaU1MTY6",  callback_data="telegram_gruppa")
order3 = InlineKeyboardButton(text="☎️ Колл-центр 🚀 ",  callback_data="call_center")
order4 = InlineKeyboardButton(text="✅ Telegram канал 🚀 ",url="https://t.me/yang_woow" , callback_data="telegram_kanal")
order5 = InlineKeyboardButton(text="🛒 Заказ 🚀 ",  callback_data="buy_telegram")
order6 = InlineKeyboardButton(text="✅ Telegram бот 🚀 ", url="https://t.me/yang_woow_bot", callback_data="telegram_bot")
about_ru.add(order1, order2, order3, order4, order5, order6)

# English Biz haqimizda bosilganida chiqadigan buttonslar
about_en = InlineKeyboardMarkup(row_width=2)
order1 = InlineKeyboardButton(text="🌏 Web site 🚀", url="https://www.yangwoow.uz", callback_data="website")
order2 = InlineKeyboardButton(text="✅ Telegram group 🚀 ", url="https://t.me/joinchat/pVCTtnZpvaU1MTY6",  callback_data="telegram_gruppa")
order3 = InlineKeyboardButton(text="☎️ Call center 🚀 ",  callback_data="call_center")
order4 = InlineKeyboardButton(text="✅ Telegram channel 🚀 ",url="https://t.me/yang_woow" , callback_data="telegram_kanal")
order5 = InlineKeyboardButton(text="🛒 Order 🚀 ",  callback_data="buy_telegram")
order6 = InlineKeyboardButton(text="✅ Telegram bot 🚀 ", url="https://t.me/yang_woow_bot", callback_data="telegram_bot")
about_en.add(order1, order2, order3, order4, order5, order6)

# Krilcha Biz haqimizda bosilganida chiqadigan buttonslar
about_uz_kril = InlineKeyboardMarkup(row_width=2)
order1 = InlineKeyboardButton(text="🌏 Веб-сайт 🚀", url="https://www.yangwoow.uz", callback_data="website")
order2 = InlineKeyboardButton(text="✅ Телеграм группа 🚀 ", url="https://t.me/joinchat/pVCTtnZpvaU1MTY6",  callback_data="telegram_gruppa")
order3 = InlineKeyboardButton(text="☎️ Cолл-cентер 🚀 ",  callback_data="call_center")
order4 = InlineKeyboardButton(text="✅ Телеграм канал 🚀 ",url="https://t.me/yang_woow" , callback_data="telegram_kanal")
order5 = InlineKeyboardButton(text="🛒 Буюртма бериш 🚀 ",  callback_data="buy_telegram")
order6 = InlineKeyboardButton(text="✅ Телеграм бот  🚀 ", url="https://t.me/yang_woow_bot", callback_data="telegram_bot")
about_uz_kril.add(order1, order2, order3, order4, order5, order6)


# Follow Boshqlarga yuborish guruhlarga qo'shish
follow_btn = InlineKeyboardMarkup(row_width=1)
folow = InlineKeyboardButton(text="➕ Follow ➕", url="http://t.me/yang_woow_bot?startgroup=new", callback_data="follow")
follow_btn.add(folow)