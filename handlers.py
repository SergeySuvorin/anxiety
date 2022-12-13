from aiogram import types
from aiogram import asyncio
from aiogram.types import Message, CallbackQuery, MediaGroup, InputFile, LabeledPrice, PreCheckoutQuery
from aiogram.dispatcher.filters import Command
from aiogram.types.message import ContentType
from kb import *
import aioschedule as schedule
from datetime import datetime, timedelta, timezone
import random

from main import dp,bot

import sqlite3


list_lvl_1_4 = ["<b>Дневник</b>\n\nПростой и очень эффективный способ.\nВозьми бумагу и ручку. Если под рукой только телефон можно писать в нем. Поставь таймер на 15 минут. Выпиши из головы всё, что тебя тревожит и причиняет беспокойство.\n\nКак всё сделаешь 💪, жми на кнопку снизу"]
list_lvl_5_7 = ["<b>Центрирование</b>\n\nДля устойчивости и связи со своим телом. Тревога вызывает в теле напряжение и зажатость. Сегодня мы через тело будем учиться выходить из этого напряжения.\n\nПослушай аудио.","<b>Самый худший сценарий</b>\n\nТебе понадобятся листок и ручка. Если под рукой только телефон, можешь писать в заметки.\n состоит из 2 частей.\n\n1. Подумай о ситуации, которая тебя тревожит. Представь самый худший сценарий из возможных. Самый худший. Сгущай краски. Подробно запиши его.\n2. Теперь запиши свой план - что ты будешь делать в этой ситуации.\nТеперь у тебя есть план на самый худший вариант развития события. Скорее всего, он не произойдет - обычно страшные картины нашего воображения не воплощаются в жизнь. Но даже если это будет исключение - ты знаешь, что делать.\n\nКак всё сделаешь 💪, жми на кнопку снизу"]
list_lvl_8_10 = ["<b>Дыхание 3-5-2</b>\n\nНаша задача - снизить тревогу. Дыхательные техники - один из самых эффективных способов.\nПоставь таймер на 4 минуты и дыши это время по схеме: вдох на 3 счёта - выдох на 5 счетов - пауза на 2 счета.\nПослушай аудио.\n\nКак всё сделаешь 💪, жми на кнопку снизу","<b>Физическая разрядка</b>\n\nЕсли тебе есть, где уединиться и шум не вызовет вопросов – потопай ногами. Сильно, интенсивно потопай ногами 50 раз. Небольшой перерыв, отдышись и ещё потопай ещё 50 раз, часто перебирая ногами.\nЕсли такой возможности нет, сильно сожми кулаки обеих рук и подержи 3 секунды. Расслабь. Снова сожми и 3 секунды держи сжатыми. Расслабь. Сделай так 50 раз.\n\nКак всё сделаешь 💪, жми на кнопку снизу"]



@dp.message_handler(Command('start'))
async def start(message: Message):
    await message.answer('Привет!\nЯ твой союзник, я помогу тебе справится с тревогой\n\nОбрати внимание, что я не подхожу для кризисных моментов, ситуаций, в которых есть угроза твоей жизни и при панических атаках.\n\nНажимай на кнопки и вперед!\n', reply_markup=fkb)
    connect = sqlite3.connect('anxiety.db')
    cursor = connect.cursor()
    if cursor.execute("SELECT * FROM users WHERE user_id = ?", (message.chat.id,)).fetchone() == None:
        cursor.execute("INSERT INTO users (user_id, name) VALUES (?, ?)", [message.chat.id, message.chat.first_name])
        cursor.close()
        connect.commit()
        connect.close()
    else:
        cursor.close()
        connect.commit()
        connect.close()

# @dp.message_handler(Command('admin'))
# async def adm(message:Message):
#     await bot.send_message(message.chat.id,"Давай я помогу тебе!\nПожалуйста, выбери свой уровень тревожности от 1 до 10\nЖми на кнопочку снизу", reply_markup=lvl_of_anxiety)       

@dp.callback_query_handler(text='anxiety_cb')
async def anxiety_cb(call:types.callback_query):
    await call.message.edit_text("Давай я помогу тебе!\nОцени свой уровень тревожности по шкале от 1 до 10.\n\n10 - максимальный уровень тревоги, 1 - минимальная тревога.\n\nЖми на кнопку снизу", reply_markup=lvl_of_anxiety)

@dp.callback_query_handler(text='lvl1_4')
async def lvl1(call:types.callback_query):
    await call.message.edit_text(random.choice(list_lvl_1_4), reply_markup = complete)

    
@dp.callback_query_handler(text='lvl5_7')
async def lvl1(call:types.callback_query):
    t = random.choice(list_lvl_5_7)
    if t[3] == 'Ц':
        with open('center.mp3','rb') as f:
            cont1 = f.read()
            Title1 = 'Центрирование'
        await bot.send_audio(call.message.chat.id, audio=cont1, performer = 'Техника', title=Title1)
    await call.message.edit_text(t, reply_markup = complete)



@dp.callback_query_handler(text='lvl8_10')
async def lvl1(call:types.callback_query):
    a = random.choice(list_lvl_8_10)
    if a[3] == 'Д':
        with open('breath.mp3','rb') as f:
            cont = f.read()
            Title = "Дыхание 3-5-2"
    # elif a[14] == 'Ф':
    #     with open('center.mp3','rb') as f:
    #         cont = f.read()
    #         Title = 'Центрирование'
        await bot.send_audio(call.message.chat.id, audio=cont, performer = 'Техника', title=Title)
    await call.message.edit_text(a, reply_markup = complete)



@dp.callback_query_handler(text='compl')
async def compls(call:types.callback_query):
    await call.message.delete()
    await bot.send_message(call.message.chat.id,"Отлично! Ты большой молодец!\n\nКак ты?\nВажно понимать, какой урон мы нанесли тревоге.\nОцени её уровень сейчас.",reply_markup=finish)
    # await asyncio.sleep(30)
    # await bot.send_message(call.message.chat.id, "Как ты?\n\nВажно понимать, какой урон мы нанесли тревоге.\nОцени её уровень сейчас. ", reply_markup=finish)

@dp.callback_query_handler(text = 'lower')
async def  low(call:types.callback_query):
    await call.message.edit_text("Отлично, враг повержен.\nХочешь нанести ещё удар по своей тревоге?", reply_markup = lowww)
    
@dp.callback_query_handler(text = 'one_more')
async def more(call:types.callback_query):
    await call.message.edit_text("Давай я помогу тебе!\nОцени свой уровень тревожности по шкале от 1 до 10.\n\n10 - максимальный уровень тревоги, 1 - минимальная тревога.\n\nЖми на кнопку снизу", reply_markup=lvl_of_anxiety)

@dp.callback_query_handler(text = 'no_more')
async def no_more(call:types.callback_query):
    await call.message.edit_text("Отлично, враг повержен.\nCкоро вернусь и мы закончим)")
    await asyncio.sleep(30)
    await bot.send_message(call.message.chat.id,"Как ты тут?\nЕсли все прошло хорошо, то ты можешь оставить отзыв\nА если тревоге нужно ещё втащить, попробуй тренинг для более высокого уровня",reply_markup=final)

@dp.callback_query_handler(text= 'no_change')
async def no_change(call:types.callback_query):
    await call.message.edit_text("Сейчас это не сработало. Нужно что-то посильнее.\n\nХочешь сделать другое упражнение?", reply_markup=no_changes)

@dp.callback_query_handler(text= 'higher')
async def higher(call:types.callback_query):
    await call.message.edit_text("Такое случается, у нас в арсенале есть вещи посерьёзнее.\n\nПродолжаешь бой?",reply_markup = highers)

@dp.callback_query_handler(text = 'otherlvl')
async def other(call:types.callback_query):
    await call.message.edit_text("Давай я помогу тебе!\nОцени свой уровень тревожности по шкале от 1 до 10.\n\n10 - максимальный уровень тревоги, 1 - минимальная тревога.\n\nЖми на кнопку снизу", reply_markup=lvl_of_anxiety)

@dp.callback_query_handler(text = 'feedback')
async def feed(call:types.callback_query):
    await call.message.edit_text("Отлично, герой!\nНапиши свой отзыв следующим сообщением и я доставлю его Саше")
    
    @dp.message_handler()
    async def feedback(message: types.Message):
        await bot.send_message(message.chat.id,"Твой отзыв успешно доставлен.\nСпасибо за фидбек.",reply_markup=menus)
        await bot.forward_message(481608826, message.from_user.id, message.message_id)
    
@dp.callback_query_handler(text='menu')
async def menu(call:types.callback_query):
    await call.message.edit_text('Привет!\nЯ твой союзник, я помогу тебе справится с тревогой\n\nОбрати внимание, что я не подхожу для кризисных моментов, ситуаций, в которых есть угроза твоей жизни и при панических атаках.\n\nНажимай на кнопки и вперед!\n', reply_markup=fkb)