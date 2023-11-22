import random
import telebot
import requests
import webbrowser
from telebot import types
import logging
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import buttons as btn

#Бот
token = ('6711400532:AAFJIY-Na2gnZ089BhMd_7YykRaaLD6LaA8')
bot = telebot.TeleBot(token)
Token_Informator = ('6042582873:AAE2JruiflxyP7NF8XDNPDiNbpmw2OeNIlY')S

#Бесполезный блок
photo1 = 'https://sun9-1.userapi.com/impg/pvcRl2C3mm7SvxJoUT-TFG8fOe8g9dR1FHnzfQ/xFBnLnc2Fcg.jpg?size=682x807&quality=96&sign=93f8dd6ff850b3c772738c7fa62c7dca&c_uniq_tag=powfXx5EfmRPV_KJA1hez8BNhKHhrccYOd6saVuu0sA&type=album'
photo2 = 'https://sun9-39.userapi.com/impg/pQN4GV45YniAj3xUzbVReat4BrcJ3tCZ5K4MAw/UISTUgooQhM.jpg?size=807x313&quality=96&sign=0fb4da84da1e8949130cf8259ddb3881&c_uniq_tag=DGhkZhr6rEwmZvq_iemR4GMh-X_rT3PJNYICPHrw3IM&type=album'
photo3 = 'https://sun9-77.userapi.com/impg/sqBP91y0AKopOc9yvRUGWqRJ141fPWOo1I0lCg/0p1fxy4SCm4.jpg?size=807x573&quality=96&sign=b793105990faa9a87810467593326f20&c_uniq_tag=GcHJnzIGy_4_ABfo-sfVCANhruURSw_7GmFRImfSzoY&type=album'
photo4 = 'https://sun9-27.userapi.com/impg/pdabC6nY2QRyEluSpMxau5bMnmMnyM6pxlojUg/L3jg2c2Q748.jpg?size=807x295&quality=96&sign=0d155069a025e00c0947463e8063b96c&c_uniq_tag=FWkEUMuZQJRYteRFPj4Me612ixALGlPkcgWAoMw1_rs&type=album'
photo5 = 'https://sun9-78.userapi.com/impg/SfLBz3nlPD2SPi_5ZhVixc-AQ_NpqrJLS-MFRw/jZ-pWCPhOGA.jpg?size=807x407&quality=96&sign=66b095130efdc7a8f99a31b2bce25159&c_uniq_tag=TO3saHhZavP36ir7AdKvodSfRkL4M_bMvTPkuNc_Vig&type=album'
photo6 = 'https://sun9-78.userapi.com/impg/SfLBz3nlPD2SPi_5ZhVixc-AQ_NpqrJLS-MFRw/jZ-pWCPhOGA.jpg?size=807x407&quality=96&sign=66b095130efdc7a8f99a31b2bce25159&c_uniq_tag=TO3saHhZavP36ir7AdKvodSfRkL4M_bMvTPkuNc_Vig&type=album'
photo7 = 'https://sun9-36.userapi.com/impg/74JA5P_VQFWDdFjvi19lcSL3TmxLzoLZIOpK7g/Rez-xzQ-fZ0.jpg?size=807x300&quality=96&sign=9c574114d53ea908f0638da0a8b23807&c_uniq_tag=WIsc9lARYA-1rl-SLf6OEPvQqwZESDtvCQQ8aeouI0g&type=album'
photo8 = 'https://sun9-1.userapi.com/impg/pvcRl2C3mm7SvxJoUT-TFG8fOe8g9dR1FHnzfQ/xFBnLnc2Fcg.jpg?size=682x807&quality=96&sign=93f8dd6ff850b3c772738c7fa62c7dca&c_uniq_tag=powfXx5EfmRPV_KJA1hez8BNhKHhrccYOd6saVuu0sA&type=album'

random = random.randint(10000, 99999)

#Приветственное сообщение
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_photo(message.chat.id, f'{photo1}' , reply_markup=btn.topup, parse_mode='Markdown')
    bot.delete_message(message.chat.id, message.message_id)
    TOKEN = Token_Informator
    chat_id = "2136801842"
    message = f"Новый пользователь :D"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())  # Эта строка отсылает сообщение

#Кнопки подтверждения оплаты
truebuybutton = types.InlineKeyboardMarkup()
trueback = types.InlineKeyboardButton(text='Главное меню', callback_data='true')
truebuybutton.add(trueback)

#Одиночная кнопка назад
backbutton = types.InlineKeyboardMarkup()
qiwibutton = types.InlineKeyboardButton(text='Оплатить онлайн формой', url='https://my.qiwi.com/form/Nykolai-KPE4OA_LSm')
buybutton = types.InlineKeyboardButton(text='Оплатил', callback_data='buy')
backbut = types.InlineKeyboardButton(text='Назад', callback_data='backmenu')
backbutton.add(qiwibutton)
backbutton.add(buybutton, backbut)

#Кнопки покупка/назад
def kids():
    buybuttonskids = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='99р', callback_data='buy199')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    buybuttonskids.row(button1, button2)
    return buybuttonskids

def teenage():
    buybuttonsteenage = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='199р', callback_data='buy299')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    buybuttonsteenage.row(button1, button2)
    return buybuttonsteenage

def rape():
    buybuttonsrape = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='199р', callback_data='buy399')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    buybuttonsrape.row(button1, button2)
    return buybuttonsrape

def trash():
    buybuttonstrash = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='149р', callback_data='buy249')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    buybuttonstrash.row(button1, button2)
    return buybuttonstrash

def allpack():
    buybuttonsallpack = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='499р', callback_data='buy699')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    buybuttonsallpack.row(button1, button2)
    return buybuttonsallpack

def morepacks():
    buybuttonsmorepacks = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='back')
    buybuttonsmorepacks.row(button2)
    return buybuttonsmorepacks

#Обработчик кнопок
@bot.callback_query_handler(func=lambda c: True)
def change_photo(call):
    buybuttonkids = kids()
    buybuttonteenage = teenage()
    buybuttonrape = rape()
    buybuttontrash = trash()
    buybuttonallpack = allpack()
    buybuttonmorepacks = morepacks()
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    #Покупка kids
    if call.data == 'kids':
        photo = open('kids.png', 'rb')
        media = types.InputMediaPhoto(photo, caption='💿 *Вес архива:* 92гб\n\n📼 *Количество видео:* 202\n\n📸 *Количество фото:* 2908\n\n📔 *Описание:* архив, содержащий фото и видео со школьницами/ками 9-14 лет с разными сценариями: от простой демонстрации тела до изнасилований', parse_mode='Markdown')
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=buybuttonkids)

    #Покупка teenage
    elif call.data == 'teenage':
        photo = open('teenage.png', 'rb')
        media = types.InputMediaPhoto(photo, caption='💿 *Вес архива:* 89гб\n\n📼 *Количество видео:* 192\n\n📸 *Количество фото:* 2789\n\n📔 *Описание:* фото и видео со школьницами от 14 до 19 лет, собранные с личных переписок, взломанных акакаунтов, OnlyFans, DarkNet, взломанных облачных накопителей\n\n👀 *Предпросмотр:* https://mega.nz/folder/wjlXRaAa#jYwdoTAyhttK6pcJOQl87w', parse_mode='Markdown')
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=buybuttonteenage)

    #Покупка rape
    elif call.data == 'rape':
        photo = open('rape.png', 'rb')
        media = types.InputMediaPhoto(photo, caption='💿 *Вес архива:* 78гб\n\n📼 *Количество видео:* 174\n\n📸 *Количество фото:* 2832\n\n📔 *Описание:* фото и видео изнасилований школьниц, собранные со всех тёмных источников интернета', parse_mode='Markdown')
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=buybuttonrape)

    #Покупка trash
    elif call.data == 'trash':
        photo = open('trash.png', 'rb')
        media = types.InputMediaPhoto(photo, caption='💿 *Вес архива:* 87гб\n\n📼 *Количество видео:* 139\n\n📸 *Количество фото:* 3329\n\n📔 *Описание:* фото и видео со вписок/дней рождения/школьных пьянок, представвляющие собой любительский контент с участием девочек 14-19 лет\n\n👀 *Предпросмотр:* https://mega.nz/folder/EmURjCzQ#asPfxv1mBPbTE8qdgDSeQA', parse_mode='Markdown')
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=buybuttontrash)

    #Покупка allpack
    elif call.data == 'allpack':
        photo = open('allpack.png', 'rb')
        media = types.InputMediaPhoto(photo, caption='⚖️ После покупки товара вы получите доступ ко всем архивам, которые есть у нас в продаже. С описанием можете ознакомиться в разделе каждого из них', parse_mode='Markdown')
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=buybuttonallpack)

    #Покупка morepacks
    elif call.data == 'morepacks':
        photo = open('morepacks.png', 'rb')
        media = types.InputMediaPhoto(photo, caption='<b>Свяжитесь с продавцом для уточнения информации:</b> @TeenageStoreHelper', parse_mode='html')
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=buybuttonmorepacks)

    #Кнопка назад
    elif call.data == 'back':
        photo = open('menu.png', 'rb')
        media = types.InputMediaPhoto(photo)
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=btn.topup)
    elif call.data == 'backmenu':
        photo = open('menu.png', 'rb')
        media = types.InputMediaPhoto(photo)
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=btn.topup)

    #Кнопка покупки kids
    elif call.data == 'buy199':
        photo = open('menubuy.png', 'rb')
        media = types.InputMediaPhoto(photo, caption=f'*Цена:* 99р\n\n🔑 *Идентификатор покупки:* {random}\n*⏱ Счёт действителен:* 15мин\n\n🟠 *QIWI (СБП):* `+79588359697`\n🟠 *QIWI (СБП):* `+79789906794`', parse_mode='Markdown')
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=backbutton)

    #Кнопка покупки teenage
    elif call.data == 'buy299':
        photo = open('menubuy.png', 'rb')
        media = types.InputMediaPhoto(photo, caption=f'*Цена:* 199р\n\n🔑 *Идентификатор покупки:* {random}\n*⏱ Счёт действителен:* 15мин\n\n🟠 *QIWI (СБП):* `+79588359697`\n🟠 *QIWI (СБП):* `+79789906794`', parse_mode='Markdown')
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=backbutton)

    #Кнопка покупки rape
    elif call.data == 'buy399':
        photo = open('menubuy.png', 'rb')
        media = types.InputMediaPhoto(photo, caption=f'*Цена:* 199р\n\n🔑 *Идентификатор покупки:* {random}\n*⏱ Счёт действителен:* 15мин\n\n🟠 *QIWI (СБП):* `+79588359697`\n🟠 *QIWI (СБП):* `+79789906794`', parse_mode='Markdown')
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=backbutton)

    #Кнопка покупки trash
    elif call.data == 'buy249':
        photo = open('menubuy.png', 'rb')
        media = types.InputMediaPhoto(photo, caption=f'*Цена:* 149р\n\n🔑 *Идентификатор покупки:* {random}\n*⏱ Счёт действителен:* 15мин\n\n🟠 *QIWI (СБП):* `+79588359697`\n🟠 *QIWI (СБП):* `+79789906794`', parse_mode='Markdown')
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=backbutton)

    #Кнопка покупки allpack
    elif call.data == 'buy699':
        photo = open('menubuy.png', 'rb')
        media = types.InputMediaPhoto(photo, caption=f'*Цена: 499р*\n\n🔑 *Идентификатор покупки:* {random}\n*⏱ Счёт действителен:* 15мин\n\n🟠 *QIWI (СБП):* `+79588359697`\n🟠 *QIWI (СБП):* `+79789906794`', parse_mode='Markdown')
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=backbutton)

    #Кнопка подтверждения оплаты
    elif call.data == 'buy':
        photo = open('tyforbuy.png', 'rb')
        media = types.InputMediaPhoto(photo, caption=f'<i>Смотрите историю оплаченных товаров в профиле</i>\n\n', parse_mode='html')
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=truebuybutton)

        TOKEN = Token_Informator
        chat_id = "2136801842"
        message = f"Потенциальный лох :D"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json())  # Эта строка отсылает сообщение

    #Кнопка назад в меню
    elif call.data == 'true':
        photo = open('menu.png', 'rb')
        media = types.InputMediaPhoto(photo)
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=btn.topup)
    
    elif call.data == 'profile':
        photo = open('profile.png', 'rb')
        media = types.InputMediaPhoto(photo, caption='У вас нет оплаченных товаров\n\n<b>Поддержка:</b> @TeenageStoreHelper', parse_mode='html')
        bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id, reply_markup=truebuybutton)

bot.polling(none_stop=True)