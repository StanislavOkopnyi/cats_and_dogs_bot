from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State


router = Router()

RIGHT_ANSWER_URL = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.VcAMEB0WEk8J4-CeujPInQHaJ6%26pid%3DApi&f=1&ipt=5f2661f481f4552f644473256199c51d6e8ee43b3ac683d541419386fc18060a&ipo=images"
WRONG_ANSWER_URL = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi0.wp.com%2Fmrfrs.org%2Fwp-content%2Fuploads%2F2018%2F09%2FMRFRS_SadCat.jpg%3Ffit%3D1250%252C684%26ssl%3D1&f=1&nofb=1&ipt=dbcd8cf209b7fb61936e420177979b6d56c74e9414f494f5c49c59cf3c03ac82&ipo=images"


class Questions(StatesGroup):
    question1 = State()
    question2 = State()
    question3 = State()
    question4 = State()
    question5 = State()


async def _answer_checker(
        user_answer: str,
        right_answer: list[str],
        message: Message,
        state: FSMContext
):
    if user_answer in right_answer:
        await message.answer_photo(
            photo=RIGHT_ANSWER_URL,
            caption="<b>Right answer!</b>"
        )

        data = await state.get_data()
        right_answers_count = data["right_answers"]
        right_answers_count += 1
        await state.update_data(right_answers=right_answers_count)
    else:
        await message.answer_photo(
            photo=WRONG_ANSWER_URL,
            caption="Wrong answer =("
        )
        await message.answer(
            f"Right answer - \"{right_answer[0].capitalize()}\""
        )


@router.message(Command("quiz"))
async def quiz_handler(message: Message, state: FSMContext):
    await state.set_state(Questions.question1)
    await message.answer("Which human sweet treat can be fatal to dogs?")
    await message.answer("If you want to stop quiz - /stop")


@router.message(Command("stop"))
async def stop_hamdler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("The state of the bot has been reset.")


@router.message(Questions.question1)
async def first_question_handler(message: Message, state: FSMContext):
    user_answer = message.text.lower()
    await state.update_data(right_answers=0)
    await _answer_checker(user_answer, ['chocolate'], message, state)
    await state.set_state(Questions.question2)
    await message.answer(
        text=("Spaniels are presumed to have "
              "originated in which country?")
    )


@router.message(Questions.question2)
async def second_question_handler(message: Message, state: FSMContext):
    user_answer = message.text.lower()
    await _answer_checker(user_answer, ['spain'], message, state)
    await state.set_state(Questions.question3)
    await message.answer(
        text=("A cat can rotate it's ears how far in degrees?")
    )


@router.message(Questions.question3)
async def third_question_handler(message: Message, state: FSMContext):
    user_answer = message.text.lower()
    await _answer_checker(user_answer, ['180'], message, state)
    await state.set_state(Questions.question4)
    await message.answer(
        text=("The smallest dog ever recorded was just 2.5' tall. "
              "What breed was it?")
    )


@router.message(Questions.question4)
async def fourth_question_handler(message: Message, state: FSMContext):
    user_answer = message.text.lower()
    await _answer_checker(user_answer,
                          ['yorkshire terrier', 'yorkshire-terrier', "yorks"],
                          message,
                          state)
    await state.set_state(Questions.question5)
    await message.answer(
        text=("Corgis originate from which country?")
    )


@router.message(Questions.question5)
async def fifth_question_handler(message: Message, state: FSMContext):
    user_answer = message.text.lower()
    await _answer_checker(user_answer, ['wales'], message, state)

    data = await state.get_data()
    right_answers_count = data["right_answers"]
    await message.answer_animation(
        animation="https://c.tenor.com/jz-8XJAa4_YAAAAC/thats-all-folks.gif",
        caption=f"Congratulations! {right_answers_count}/5"
    )
