from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

fkb = InlineKeyboardMarkup(row_width=1)
anxiety = InlineKeyboardButton(text='В бой!', callback_data='anxiety_cb') 
fkb.add(anxiety)

lvl_of_anxiety = InlineKeyboardMarkup(row_width=5)

lvl_1_4 = InlineKeyboardButton(text='1-4',callback_data='lvl1_4')
lvl_5_7 = InlineKeyboardButton(text='5-7',callback_data='lvl5_7')
lvl_8_10 = InlineKeyboardButton(text='8-10',callback_data='lvl8_10')



# lvl_of_anxiety.add(lvl_1,lvl_2,lvl_3,lvl_4,lvl_5)
lvl_of_anxiety.row(lvl_1_4,lvl_5_7,lvl_8_10)
# lvl_of_anxiety.add(lvl_6,lvl_7,lvl_8,lvl_9,lvl_10)


complete = InlineKeyboardMarkup()
complete_btn = InlineKeyboardButton(text="Я выполнил тренинг 🏆", callback_data='compl')
complete.add(complete_btn)

menus = InlineKeyboardMarkup()
menus_btn = InlineKeyboardButton(text='Вернуться назад в меню',callback_data='menu')
menus.add(menus_btn)

finish = InlineKeyboardMarkup(row_width=1)
finish_btn_1 = InlineKeyboardButton(text='1-4', callback_data='lower')
finish_btn_2 = InlineKeyboardButton(text='5-7', callback_data='no_change')
finish_btn_3 = InlineKeyboardButton(text='8-10 ', callback_data='higher')
# finish_btn_4 = InlineKeyboardButton(text='Оставить отзыв💬', callback_data='feedback')
finish.add(finish_btn_1)
finish.insert(finish_btn_2)
finish.insert(finish_btn_3)

lowww = InlineKeyboardMarkup(row_width=1)
lowww_btn_1 = InlineKeyboardButton(text='Да, нужна еще техника', callback_data='one_more')
lowww_btn_2 = InlineKeyboardButton(text='Нет, все отлично!', callback_data='no_more')
lowww.add(lowww_btn_1,lowww_btn_2)

final = InlineKeyboardMarkup(row_width=1)
final_btn_1 = InlineKeyboardButton(text="Мне нужен другой уровень", callback_data='anxiety_cb')
final_btn_2 = InlineKeyboardButton(text='Оставить отзыв💬', callback_data='feedback')
final.add(final_btn_1,final_btn_2)

no_changes = InlineKeyboardMarkup(row_width=1)
no_changes_btn_1 = InlineKeyboardButton(text='Да, нужна ещё техника',callback_data='one_more')
no_changes.add(no_changes_btn_1)

highers = InlineKeyboardMarkup(row_width=1)
highers_btn1_1 = InlineKeyboardButton('Да, присылай другое упражнение',callback_data='lvl8_10')
highers.add(highers_btn1_1)