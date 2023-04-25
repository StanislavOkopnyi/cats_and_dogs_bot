from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer_animation(
        animation="https://c.tenor.com/Qer_iSfGXNQAAAAM/cats-dogs.gif",
        caption=("<b>Hello!\n</b>"
                 "There are some things this bot can do:\n"
                 "Random cat photo with fun fact - /random_cat\n"
                 "Random dog photo with fun fact - /random_dog\n"
                 "Quiz about cats and dogs - /quiz\n"
                 "All comands - /help\n")
    )
