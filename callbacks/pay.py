from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery

from data.database import add_user_if_not_exists
from keyboards.user_inline import get_pay_menu
from config import DB_PATH

router = Router()


@router.callback_query(F.data == "pay_rub")
async def pay_rub_func(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    await add_user_if_not_exists(DB_PATH, user_id)
    text = "<b>При оплате введите свою почту, чтобы мы открыли для вас доступ.</b>"

    await bot.send_message(
        chat_id=user_id,
        text=text,
        parse_mode="html",
        reply_markup=await get_pay_menu(),
    )

    await bot.delete_message(call.message.chat.id, call.message.message_id)

    # await call.message.edit_text(
    #     text=text,
    #     parse_mode="html",
    #     reply_markup=await get_pay_menu(),
    # )
