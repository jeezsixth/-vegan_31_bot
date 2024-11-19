from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.types.input_file import FSInputFile

from keyboards.admin_inline import get_admin_menu
from config import DB_PATH, ADMIN_ID

router = Router()


@router.message(F.text == "/admin")
async def start_func(msg: Message, bot: Bot):
    if msg.from_user.id == ADMIN_ID:
        await bot.send_message(
            chat_id=ADMIN_ID,
            text="Admin panel",
            parse_mode="html",
            reply_markup=await get_admin_menu(),
        )
