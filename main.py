import asyncio
from aiogram import Bot, Dispatcher

from handlers import user_commands, open_admin
from callbacks import pay, check_payment, invite_friends, get_statistic, newsletter

from data.database import initialize_db
from config import TOKEN, DB_PATH


async def main():
    await initialize_db(DB_PATH)

    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        pay.router,
        check_payment.router,
        invite_friends.router,
        open_admin.router,
        get_statistic.router,
        newsletter.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
