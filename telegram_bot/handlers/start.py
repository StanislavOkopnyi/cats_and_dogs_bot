from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer_animation(
        animation="https://c.tenor.com/Qer_iSfGXNQAAAAM/cats-dogs.gif",
        caption="Hello!"
    )