import asyncio
import logging
from telegram_bot.handlers import random_dog, random_cat, start, quiz
from aiogram import Bot, Dispatcher


async def main() -> None:
    dispatcher = Dispatcher()

    dispatcher.include_router(random_dog.router)
    dispatcher.include_router(random_cat.router)
    dispatcher.include_router(start.router)
    dispatcher.include_router(quiz.router)
    bot = Bot("Token",
              parse_mode="HTML")
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
