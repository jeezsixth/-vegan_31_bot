from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from data.database import add_user_if_not_exists, get_invite_count
from keyboards.user_inline import get_back_menu
from config import DB_PATH, BOT_LINK

router = Router()


@router.callback_query(F.data == "invite_friends")
async def invite_friends_func(call: CallbackQuery, bot: Bot):
    user_id = call.from_user.id
    invite_count = await get_invite_count(DB_PATH, user_id)
    text = f"""
<b>Ваша ссылка для приглашения - </b>
<code>{BOT_LINK}?start={user_id}</code>

<b>Чтобы получить доступ к приватке, пригласите 5 друзей. ( Если у вас нету друзей, советуем оплатить 11 рублей )</b>

Приглашений: {invite_count}
Осталось пригласить {5-invite_count}.

"""

    await bot.send_message(
        chat_id=user_id,
        text=text,
        parse_mode="html",
        reply_markup=await get_back_menu(),
    )

    await bot.delete_message(call.message.chat.id, call.message.message_id)
