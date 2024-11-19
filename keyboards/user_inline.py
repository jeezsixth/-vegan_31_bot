from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def get_main_menu():
    kb = [
        [
            InlineKeyboardButton(text="Оплатить 11 рублей 💰", callback_data="pay_rub"),
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


async def get_pay_menu():
    kb = [
        [
            InlineKeyboardButton(
                text="Оплатить 💰", url="https://go-site.fun?invite=50v9uyv"
            )
        ],
        [
            InlineKeyboardButton(
                text="Проверить оплату 🔥", callback_data="check_payment"
            )
        ],
        [
            InlineKeyboardButton(
                text="Возврат в меню 🤖", callback_data="open_main_menu"
            )
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


async def get_back_menu():
    kb = [
        [
            InlineKeyboardButton(
                text="Возврат в меню 🤖", callback_data="open_main_menu"
            )
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard
