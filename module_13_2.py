from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7822078456:AAHvaw2ghYvc0MBErCXjhUqSHb_kc6o2fO0"
bot = Bot(token=api)
dp = Dispatcher(bot, storage= MemoryStorage())

@dp.message_handler()
async def all_message(message):
    print("Мы получили сообщение!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)