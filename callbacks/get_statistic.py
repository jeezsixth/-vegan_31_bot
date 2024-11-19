from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from data.database import get_user_count
from keyboards.admin_inline import get_admin_menu
from config import DB_PATH

router = Router()


@router.callback_query(F.data == "get_statistic")
async def get_statistic_func(call: CallbackQuery, bot: Bot):
    user_count = await get_user_count(DB_PATH)
    user_id = call.from_user.id

    await bot.edit_message_text(
        message_id=call.message.message_id,
        chat_id=user_id,
        text=f"📊 Статистика:\n\n" f"👥 Количество пользователей: {user_count}\n\n",
        parse_mode="html",
        reply_markup=await get_admin_menu(),
    )
