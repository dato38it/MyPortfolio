import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router
from app.database.models import async_main
import os
from dotenv import load_dotenv
async def main():
    await async_main()
    #bot = Bot(token='7153496019:AAG0XeyOSWEf8c8-k_9USF7ZIT7QXjM1BS4')
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'))    
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot disabled')