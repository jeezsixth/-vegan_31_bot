from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery

from data.database import add_user_if_not_exists
from keyboards.user_inline import get_back_menu
from config import DB_PATH

router = Router()


@router.callback_query(F.data == "check_payment")
async def check_payment_func(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    await add_user_if_not_exists(DB_PATH, user_id)
    text = "<b>Мы не нашли вашу оплату, попробуйте снова 😔</b>"

    await call.message.edit_text(
        text=text,
        parse_mode="html",
        reply_markup=await get_back_menu(),
    )
