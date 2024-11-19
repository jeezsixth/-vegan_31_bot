from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.types.input_file import FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


from data.database import (
    add_user_if_not_exists,
    check_user_exists,
    increment_invite_count,
)
from keyboards.user_inline import get_main_menu
from config import DB_PATH, get_greeting_message

router = Router()


@router.message(F.text.startswith("/start"))
async def start_func(msg: Message):
    text = get_greeting_message(msg.from_user.full_name)
    invite_id = msg.text.split("/start")[-1]
    user_id = msg.from_user.id

    try:
        is_user = await check_user_exists(DB_PATH, user_id)

        if is_user:
            pass
        else:
            if invite_id == "" or invite_id == " ":
                await add_user_if_not_exists(DB_PATH, user_id)
            else:
                try:
                    int_invited_id = int(invite_id.strip())

                    await add_user_if_not_exists(
                        DB_PATH, user_id, invited_by=int_invited_id
                    )
                    await increment_invite_count(DB_PATH, int_invited_id)

                    print(int_invited_id)
                except Exception as e:
                    print(e)
    except Exception as e:
        pass

    file = FSInputFile("start_image.jpg")
    await msg.answer_photo(
        photo=file,
        caption=text,
        parse_mode="html",
        reply_markup=await get_main_menu(),
    )


@router.callback_query(F.data == "open_main_menu")
async def open_main_menu(call: CallbackQuery, bot: Bot, state: FSMContext):
    await state.clear()

    user_id = call.from_user.id
    await add_user_if_not_exists(DB_PATH, user_id)
    text = get_greeting_message(call.from_user.full_name)

    file = FSInputFile("start_image.jpg")
    await bot.send_photo(
        chat_id=call.message.chat.id,
        photo=file,
        caption=text,
        parse_mode="html",
        reply_markup=await get_main_menu(),
    )

    await bot.delete_message(call.message.chat.id, call.message.message_id)
