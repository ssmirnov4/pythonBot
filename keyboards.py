from aiogram.filters import callback_data
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

keyOk = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Ок')]

], one_time_keyboard=True,
    input_field_placeholder="Нажмите \"Ок\", Если все понятно")


keyNext = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Следующий вопрос')], [KeyboardButton(text='Забрать выигрыш')]

], one_time_keyboard=True)
keyAgain = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Старт')], [KeyboardButton(text='Нет')]
], one_time_keyboard=True)

keyStart = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Старт')]

], one_time_keyboard=True,
    input_field_placeholder="Нажмите \"Старт\", когда вы будуете готовы")

key0 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Козла', callback_data='true')],    [InlineKeyboardButton(text='Барана', callback_data='false')],
    [InlineKeyboardButton(text='Слона', callback_data='false')], [InlineKeyboardButton(text='Орла', callback_data='false')]
], resize_keyboard=True)

key1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мастика', callback_data='false')],    [InlineKeyboardButton(text='Клей', callback_data='true')],
    [InlineKeyboardButton(text='Грунтовка', callback_data='false')], [InlineKeyboardButton(text='Пропитка', callback_data='false')]
], resize_keyboard=True)

key2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='II', callback_data='false')],    [InlineKeyboardButton(text='VI', callback_data='false')],
    [InlineKeyboardButton(text='IX', callback_data='false')], [InlineKeyboardButton(text='III', callback_data='true')]
], resize_keyboard=True, one_time_keyboard = True)

key3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='6-7 минут', callback_data='true')],    [InlineKeyboardButton(text='10-12 минут', callback_data='false')],
    [InlineKeyboardButton(text='3-5 минут', callback_data='false')], [InlineKeyboardButton(text='16-18 минут', callback_data='false')]
], resize_keyboard=True)

key4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1 месяц', callback_data='false')],    [InlineKeyboardButton(text='6 месяцев', callback_data='false')],
    [InlineKeyboardButton(text='3 месяца', callback_data='true')], [InlineKeyboardButton(text='2 месяца', callback_data='false')]
], resize_keyboard=True)

key = [key0,key1, key2, key3, key4]

