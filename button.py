from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# KeyboardButton bu oddiy sms xabar orqali ishlovchi buttonlar


# Tilni tanlash uchun buttons lar inline
language_btn_inline = InlineKeyboardMarkup(row_width=2)
iteam1 = InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data= "🇺🇿 O'zbekcha")
iteam2 = InlineKeyboardButton(text="🇷🇺 Русский", callback_data= "🇷🇺 Русский")
iteam3 = InlineKeyboardButton(text="🇺🇸 Enlish", callback_data= "🇺🇸 Enlish")
iteam4 = InlineKeyboardButton(text="🇺🇿 Узбекча", callback_data= "🇺🇿 Узбекча")
language_btn_inline.add(iteam1, iteam2, iteam3, iteam4) 





# Tilni tanlaganda chqadigan buttonlar
uzbekcha = KeyboardButton("🇺🇿 O'zbekcha")
russion = KeyboardButton("🇷🇺 Русский")
english = KeyboardButton("🇺🇸 English")
language_btn = ReplyKeyboardMarkup( resize_keyboard=True, row_width=3, one_time_keyboard=True).add(uzbekcha, russion, english)
# end block


# O'zbekcha bo'limidagi menular uchun buttonlar
menu1 = KeyboardButton("🛒 Buyurtma berish")
menu2 = KeyboardButton("📙 Biz haqimizda")
menu3 = KeyboardButton("💵 Xizmat narhlarini bilish")
menu4 = KeyboardButton("◀ Ortga")
uzbMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(menu1, menu2, menu3, menu4)
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

# Xizmatdan foydalangalik haqida so'rov uchun buttons
regular_customer_uz = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
itembtn1 = KeyboardButton("Xa")
itembtn2 = KeyboardButton("Yo'q")
regular_customer_uz.add(itembtn1, itembtn2)




# O'zbekcha Buyurtma berish uchun va website ga olib otadigan buttons
purchase_uz = InlineKeyboardMarkup(row_width=2)
order1 = InlineKeyboardButton(text="🛒 Telegram orqali 🚀 ",  callback_data="buy_telegram")
order2 = InlineKeyboardButton(text="🌏 Website orqali 🚀 ", url="google.com", callback_data="buy_website")
order3 = InlineKeyboardButton(text="📟 Xisoblash 🚀 ",   callback_data="calculator")
order4 = InlineKeyboardButton(text="📬 Izox qoldirish 🚀 ",  url="google.com", callback_data="comment")
purchase_uz.add(order1, order2, order3, order4)


# Ruscha Buyurtma berish uchun va website ga olib otadigan buttons 
purchase_ru = InlineKeyboardMarkup(row_width=2)
order1 = InlineKeyboardButton(text="🛒 Телеграммой🚀 ", callback_data="buy_telegram")
order2 = InlineKeyboardButton(text="🌏 Через сайт 🚀 ", url="google.com", callback_data="buy_website")
order3 = InlineKeyboardButton(text="📟 Расчет 🚀 ",   callback_data="calculator")
order4 = InlineKeyboardButton(text="📬 Оставить коментарий 🚀 ",  url="google.com", callback_data="comment")
purchase_ru.add(order1, order2, order3, order4)

# English  Buyurtma berish uchun va website ga olib otadigan buttons
purchase_en = InlineKeyboardMarkup(row_width=2)
order1 = InlineKeyboardButton(text="🛒 By telegram 🚀 ",  callback_data="buy_telegram")
order2 = InlineKeyboardButton(text="🌏 Through the site 🚀 ", url="google.com", callback_data="buy_website")
order3 = InlineKeyboardButton(text="📟 Calculation 🚀 ",   callback_data="calculator")
order4 = InlineKeyboardButton(text="📬 Leave a comment 🚀 ",  url="google.com", callback_data="comment")
purchase_en.add(order1, order2, order3, order4)




# O'zbekcha Biz haqimizda bosilganida chiqadigan buttonslar
about_uz = InlineKeyboardMarkup(row_width=2)
order1 = InlineKeyboardButton(text="🌏 Website 🚀", url="https://www.yangwoow.uz", callback_data="website")
order2 = InlineKeyboardButton(text="✅ Telegram gruppa 🚀 ", url="https://t.me/joinchat/pVCTtnZpvaU1MTY6",  callback_data="telegram_gruppa")
order3 = InlineKeyboardButton(text="☎️ Coll-center 🚀 ",  callback_data="call_center")
order4 = InlineKeyboardButton(text="✅ Telegram kanal 🚀 ",url="https://t.me/yang_woow" , callback_data="telegram_kanal")
order5 = InlineKeyboardButton(text="🛒 Buyurtma berish 🚀 ",  callback_data="buy_telegram")
order6 = InlineKeyboardButton(text="✅ Telegram bot 🚀 ", url="https://t.me/yang_woow_bot", callback_data="telegram_bot")
about_uz.add(order1, order2, order3, order4, order5, order6)

