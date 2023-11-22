from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

# Кнопки главного меню
topup = types.InlineKeyboardMarkup()
profile = types.InlineKeyboardButton(text="💼 Профиль 💼", callback_data="profile")
kids = types.InlineKeyboardButton(text="👧 Дети от 9 до 14 👦", callback_data="kids")
teenage = types.InlineKeyboardButton(text="🍑 Teenage от 14 до 19 лет 🍑", callback_data="teenage")
rape = types.InlineKeyboardButton(text="🩸 Изнасилования 16+ 🩸", callback_data="rape")
trash = types.InlineKeyboardButton(text="🍷 Треш со вписок 🍷", callback_data="trash")
allpack = types.InlineKeyboardButton(text="😌 Всё сразу 😌", callback_data="allpack")
morepacks = types.InlineKeyboardButton(text="🍓 Более обширный выбор 🍓", callback_data="morepacks")
topup.add(profile)
topup.add(kids)
topup.add(teenage)
topup.add(rape)
topup.add(trash)
topup.add(allpack)
topup.add(morepacks)

#Кнопка назад
back = types.InlineKeyboardButton(text='Назад', callback_data='back')

#Меню покупки kids
buybuttonKIDS = types.InlineKeyboardMarkup()
buyKIDS = types.InlineKeyboardButton(text='99р', callback_data="buy")
buybuttonKIDS.add(buyKIDS, back)

#Меню покупки teenage
buybuttonTEENAGE = types.InlineKeyboardMarkup()
buyTEENAGE = types.InlineKeyboardButton(text='199р', callback_data="buy")
buybuttonTEENAGE.add(buyTEENAGE, back)

#Меню покупки rape
buybuttonRAPE = types.InlineKeyboardMarkup()
buyRAPE = types.InlineKeyboardButton(text='199р', callback_data="buy")
buybuttonRAPE.add(buyRAPE, back)

#Меню покупки trash
buybuttonTRASH = types.InlineKeyboardMarkup()
buyTRASH = types.InlineKeyboardButton(text='149р', callback_data="buy")
buybuttonTRASH.add(buyTRASH, back)

#Меню покупки allpack
buybuttonALLPACK = types.InlineKeyboardMarkup()
buyALLPACK = types.InlineKeyboardButton(text='499р', callback_data="buy")
buybuttonALLPACK.add(buyALLPACK, back)

#Меню morepacks
buybuttonALLPACK = types.InlineKeyboardMarkup()
buybuttonALLPACK.add(back)

