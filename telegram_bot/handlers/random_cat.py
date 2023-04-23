from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from telegram_bot.requests.cat_image_and_fact import get_cat_photo_url,\
    get_cat_fact


router = Router()


@router.message(Command("random_cat"))
async def random_cat_handler(message: Message):
    return message.answer_photo(
        photo=await get_cat_photo_url(),
        caption=await get_cat_fact()
    )
