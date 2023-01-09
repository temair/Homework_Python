from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from sqlighter import SQLighter
import random
import os
import datetime
import aiohttp
from config import *
from plugins.keyboard import *
from plugins.face import recognition
from plugins.state import *
from plugins.tools import get_region


db = SQLighter('db.db')
bot = Bot(token=token)
dp = Dispatcher(bot=bot)

@dp.message_handler(content_types=[types.ContentType.PHOTO])
async def _(message: types.Message):
    if db.ban_exists(message.from_user.id):
        if db.get_message_date(message.from_user.id) > datetime.datetime.now():
            await message.answer('Подождите немного!')
        else:   
            with open(f'./{message.from_user.id}/{message.photo[-1].file_id}.png', 'wb') as f:
                file_info = await bot.get_file(message.photo[-1].file_id)
                downloaded_file = await bot.download_file(file_info.file_path)
                f.write(downloaded_file.getvalue())
            db.save_photo(message.from_user.id, message.photo[-1].file_id)
            await message.reply('Выберите регион', reply_markup=keyboard_city())
    else:
        await message.reply('У вас бан!')

@dp.message_handler(CommandStart())
async def _(message: types.Message):
    if not db.subscriber_exists(message.from_user.id):
        os.mkdir(str(message.from_user.id))
        db.add_subscriber(int(message.from_user.id))
    else:
        db.update_subscription(message.from_user.id, True)
    await message.answer("Вы успешно подписались, отправьте фото человека и я покажу Вам похожих людей =)", reply_markup=keyboard_menu)

@dp.message_handler(commands=['ban'])
async def _(message: types.Message):
    if message.from_user.id in admin_id:
        id_ban = int(message.text[5:])
        try:
            db.set_ban(id_ban, False)
            await message.reply("Поставил бан!")
        except Exception as e:
            await message.reply(f"Ошибка: {e}!Попробуйте еще раз")

@dp.message_handler(commands=['unban'])
async def _(message: types.Message):
    if message.from_user.id in admin_id:
        id_ban = int(message.text[7:])
        try:
            db.set_ban(id_ban, True)
            await message.reply("Успешно убрал бан!")
        except Exception as e:
            await message.reply(f"Ошибка: {e}!Попробуйте еще раз")

@dp.message_handler(commands=['profile'])
@dp.message_handler(text='Я')
async def _(message: types.Message):
    user = db.get_profile(message.from_user.id)[0]
    id = user[0]
    count_search = user[3]
    reg_date = user[4]
    balance = db.get_balance(message.from_user.id)
    await message.reply(f"ID: {id}\n"
                       f"Кол-во поисков: {count_search}\n"
                       f"Дата регистрации: {reg_date}\n"
                       f"Баланс: {balance} Р.")

@dp.message_handler(commands=['выдать'])
async def add(message: types.Message):
    if message.from_user.id in admin_id:
        message.text = message.text.split(' ')
        id = message.text[1]
        amount = int(message.text[2])
        db.update_balance(id, amount)
        await message.answer('Готово!')

@dp.message_handler(regexp=r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
async def _(message: types.Message):
    phone = message.text.replace(')', '').replace('(', '').replace('-', '').replace(' ', '')
    if phone[0] == '+':
    	phone = phone[1:]
    if phone[0] == '8':
    	phone = f'7{phone[1:]}'
    if phone[0] == '9':
    	phone = f'7{phone}'
    phone = int(phone)
    if db.get_message_date(message.from_user.id) > datetime.datetime.now():
        await message.answer('Подождите немного!')
    else:
        db.update_count_search(message.from_user.id)
        db.update_message_date(message.from_user.id)
        region, data = get_region(phone)
        photos = os.listdir(f'D:/python/findmy/jpg/{region}/face')
        for photo in photos:
            if photo.startswith(str(phone)):
                break
        await message.answer_photo(photo=types.InputFile(path_or_bytesio=f'D:/python/findmy/jpg/{region}/face/{photo}'), caption=f"Регион: {data['region']}\nОператор: {data['carrier']}")   

@dp.message_handler(text=['Пополнить', 'пополнить'])
async def adduser(message: types.Message):
    await message.reply('Введите сумму пополнения')

@dp.callback_query_handler(Text(startswith="phone"))
async def _(message: types.CallbackQuery):
    if db.get_balance(message.from_user.id) >= 10:
        phone = message.data.split('phone', '')
        name = db.get_name_for_phone(phone)
        if bool(len(name)):
            name = name[0][0]
        else:        
            db.update_balance(message.from_user.id, -10)
            async with aiohttp.ClientSession() as session:
                async with session.get(f'{ip_viber}/?phone={phone}') as response:
                    name = await response.text()
            if name:
                db.add_phone(phone, name)
        if name:
            await message.message.answer(f'Нашел номер у {phone}!\nИмя: {name}')
        else:
            await message.message.answer(f'Не нашел номер')
    else:
        await message.message.answer(f'Недостаточно денег на балансе!')


@dp.callback_query_handler()
async def _(message: types.CallbackQuery):
    if db.get_message_date(message.from_user.id) > datetime.datetime.now():
        await message.answer('Подождите немного!')
    else:
        db.update_count_search(message.from_user.id)
        db.update_message_date(message.from_user.id)
        user = db.get_profile(message.from_user.id)[0]
        photo_id = user[5]
        photo = open(f'./{message.from_user.id}/{photo_id}.png', 'rb')
        result = recognition(photo, message.data)
        if result == 'NoFace':
            db.update_history(message.from_user.id, random.randint(-2**35, 2**35), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Без лица', photo_id)
            return await message.message.answer('Не могу распознать лицо!')
        if result == 'NoMatch':
            db.update_history(message.from_user.id, random.randint(-2**35, 2**35), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Без совпадений', photo_id)
            return await message.message.answer('Не могу найти совпадений!')
        db.update_history(message.from_user.id, random.randint(-2**35, 2**35), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Уданчно', photo_id)
        for photo in result:
            await message.message.answer_photo(photo=types.InputFile(path_or_bytesio=f"{path_jpg}/{message.data}/face/{photo['s']}.jpg"),
                                caption=f"Номер телефона - <code>{photo['s']}</code>\n"
                                f"<a href='https://api.whatsapp.com/send?phone={photo['s']}'>Whatsapp</a>\n"
                                f"Совпадение - {photo['match']}%", parse_mode='HTML', reply_markup = keyboard_phone(photo['s']))

@dp.message_handler(state=Pay.pay)
async def _(message: types.Message):
    try:
        amount = int(message.text)
        db.update_balance(message.from_user.id, amount)
        await message.reply(f'Ваш баланс пополнен на {amount}')
    except Exception:
        pass

if __name__ == '__main__':
    executor.start_polling(dp)