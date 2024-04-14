import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import router
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def run():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print('Exit')
