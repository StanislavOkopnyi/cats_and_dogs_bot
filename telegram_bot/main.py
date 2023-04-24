import asyncio
import logging
from telegram_bot.handlers import random_dog, random_cat, start, quiz, help
from aiogram import Bot, Dispatcher


def get_token() -> str:
    with open("token.conf") as f:
        TOKEN = f.read()
    return TOKEN.strip()


async def main() -> None:
    dispatcher = Dispatcher()

    dispatcher.include_router(random_dog.router)
    dispatcher.include_router(random_cat.router)
    dispatcher.include_router(start.router)
    dispatcher.include_router(help.router)
    dispatcher.include_router(quiz.router)
    bot = Bot(get_token(), parse_mode="HTML")
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
