from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("help"))
async def start_handler(message: Message):
    await message.answer(
        ("Random cat photo with fun fact - /random_cat\n"
         "Random dog photo with fun fact - /random_dog\n"
         "Quiz about cats and dogs - /quiz\n")
    )
