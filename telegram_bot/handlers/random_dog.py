from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from telegram_bot.requests.dog_image_and_fact import get_dog_photo_url,\
    get_dog_fact


router = Router()


@router.message(Command("random_dog"))
async def random_dog_handler(message: Message):
    return message.answer_photo(
        photo=await get_dog_photo_url(),
        caption=await get_dog_fact()
    )
