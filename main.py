from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
import asyncio
from data.config import TOKEN
from handlers import commands, addsite, usersites
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging
from utils.database import DataBase as db
from utils.checksites import check

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log', mode='a', encoding='utf-8')  # Додаємо FileHandler
    ]
)

async def main():
    bot = Bot(token = TOKEN, parse_mode = 'html')
    dp = Dispatcher(storage=RedisStorage.from_url('redis://localhost:6379/0'))
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(commands.router, addsite.router, usersites.router)
    db.create_db()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(check, 'interval', seconds=60*30, args=[bot])  # Викликаємо кожні 30 хвилин
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())