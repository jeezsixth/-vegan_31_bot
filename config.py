TOKEN = "7433433130:AAEt9rwLe0lA0PMPMhTwSnXsbNBLdTUg7sg"
ADMIN_ID = 1381537697

DB_PATH = "data/database.db"
PRICE_PATH = "data/prices.json"

CRYPTO_BOT_TOKEN = "192142:AAEzSv7nPDdyUiukLuXHUhz2XZtS0c70Wcn"
BOT_LINK = "http://t.me/brawl_privatka_bot"


def get_greeting_message(name):
    message = f"""
<b>Привет</b>, {name}

<b>Чтобы получить полный доступ, тебе нужно выбрать :</b>

1. Пригласить : 5 друзей
2. Оплатить подписку ( 11 рублей )

<b>Выбери из этого что то одно, по кнопке ниже 👇</b>
"""

    return message
