from aiogram.filters import CommandStart, Command, callback_data
from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
import keyboards as kb
money = [100000, 300000, 350000, 700000, 1000000]
asks = ['Продолжите пословицу: \"Любовь зла, полюбишь и .....\"', 'Чем клеят обои?', 'К какому классу опасности относится бензин при организации его перевозки?',
            'Время готовности пасты Al dente?', 'Какой срок на проведение экспертизы промышленной безопасности предусмотрен законодательством РФ?']
ask = 0
winMoney = 0
router = Router()
buttonCondition = True
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет, {message.from_user.full_name}. Добро пожаловать в урезанную версию игры \"Кто хочется стать миллионером?\"',
                        reply_markup=kb.keyStart)

@router.message(F.text == 'Старт')
async def game0(message: Message):
    global ask, winMoney, buttonCondition
    ask = 0
    winMoney = 0
    buttonCondition = True
    await message.reply('Отлично, игра состоит из пяти вопросов, подсказок не будет, чтобы было не так легко',
                        reply_markup=kb.keyOk)

@router.message(F.text == 'Ок')
async def game1(message: Message):
    await message.reply(f'Вопрос № {ask+1}: {asks[ask]}', reply_markup=kb.key0)

@router.callback_query(F.data == 'true')
async def true(callback: CallbackQuery):
    global ask, winMoney, buttonCondition
    await callback.answer()
    if buttonCondition == False:
        await callback.answer("Вы уже ответили на этот вопрос")
    if ask == 4 and buttonCondition == True:
        await callback.message.answer(
            f"Совершенно верно! Я Вас поздравляю, Ваш окончательный баланс = {money[winMoney]} рублей🤑! Вы одержали победу😲! Хотите сыграть еще раз?",reply_markup=kb.keyAgain)
    elif ask < 4 and buttonCondition == True:
        await callback.message.answer(f"Совершенно верно! Я Вас поздравляю на Вашем балансе теперь {money[winMoney]} рублей🤑! Для перехода к следующему вопросу - "
                                  "нажмите кнопку \"Следующий вопрос\", если хотите забрать выигрыш - \"Забрать выигрыш\"", reply_markup=kb.keyNext)

    if ask < 5 and buttonCondition == True:
        ask += 1
        winMoney += 1
        buttonCondition = False

@router.message(F.text == 'Следующий вопрос')
async def next(message:Message):
    global buttonCondition, ask
    buttonCondition = True
    if ask >= 5:
        await message.reply("Вы ответили на все вопросы")
    else:
        await message.reply(f'Хорошо, вопрос №{ask+1}: {asks[ask]}', reply_markup=kb.key[ask])


@router.callback_query(F.data == 'false')
async def false(callback: CallbackQuery):
    global buttonCondition
    if buttonCondition == False:
        await callback.answer("Вы уже ответили на этот вопрос")
    else:
        await callback.answer()
        await callback.message.answer("К сожалению, Вы ответили неправильно, баланс Ваш обнуляется, Вы проиграли😩. Хотите попробовать еще?",reply_markup=kb.keyAgain)
    buttonCondition = False

@router.message(F.text == 'Забрать выигрыш')
async def win(message:Message):
    global winMoney, ask
    await message.reply(f"Поздавляем с победой😊, Ваш баланс = {money[winMoney-1]} рублей 🤑! Хотите сыграть еще раз?",reply_markup=kb.keyAgain)

@router.message(F.text == 'Нет')
async def no(message:Message):
    await message.reply(f"Хорошо, {message.from_user.full_name}, ждем Вашего возвращения!🥰🥰🤗")