from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def get_admin_menu():
    kb = [
        [InlineKeyboardButton(text="📊 Статистика", callback_data="get_statistic")],
        [InlineKeyboardButton(text="💬 Рассылка", callback_data="newsletter")],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard
