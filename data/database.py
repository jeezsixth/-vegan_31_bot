import aiosqlite


async def initialize_db(db_path: str):
    """
    Инициализирует базу данных и создает таблицу users, если она еще не существует.

    :param db_path: Полный путь к БД (например, 'data/database.db').
    """
    try:
        async with aiosqlite.connect(db_path) as db:
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    invite_count INTEGER, 
                    invited_by INTEGER
                )
            """
            )
            await db.commit()
    except Exception as e:
        print(f"Ошибка при инициализации базы данных: {e}")


async def add_user_if_not_exists(db_path: str, user_id: int, invited_by=0) -> bool:
    """
    Добавляет user_id в таблицу users, если его там нет.
    Возвращает True, если добавление прошло успешно, иначе False.

    :param db_path: Полный путь к БД (например, 'data/database.db').
    :param user_id: Идентификатор пользователя, который нужно добавить.
    :return: True, если user_id был добавлен, False, если он уже существует.
    """
    try:
        async with aiosqlite.connect(db_path) as db:
            async with db.execute(
                "SELECT 1 FROM users WHERE user_id = ?", (user_id,)
            ) as cursor:
                result = await cursor.fetchone()

            if result is None:
                await db.execute(
                    "INSERT INTO users (user_id, invite_count, invited_by) VALUES (?, ?, ?)",
                    (user_id, 0, invited_by),
                )
                await db.commit()
                return True
            else:
                return False
    except Exception as e:
        print(f"Ошибка при добавлении пользователя: {e}")
        return False


async def check_user_exists(db_path: str, user_id: int) -> bool:
    """
    Проверяет, существует ли пользователь с заданным user_id в таблице users.

    :param db_path: Полный путь к БД (например, 'data/database.db').
    :param user_id: Идентификатор пользователя для проверки.
    :return: True, если пользователь существует, иначе False.
    """
    try:
        async with aiosqlite.connect(db_path) as db:
            async with db.execute(
                "SELECT 1 FROM users WHERE user_id = ?", (user_id,)
            ) as cursor:
                return await cursor.fetchone() is not None
    except Exception as e:
        print(f"Ошибка при проверке существования пользователя: {e}")
        return False


async def increment_invite_count(db_path: str, user_id: int) -> bool:
    """
    Увеличивает значение invite_count на 1 для указанного user_id.

    :param db_path: Полный путь к БД (например, 'data/database.db').
    :param user_id: Идентификатор пользователя, для которого нужно увеличить invite_count.
    :return: True, если операция прошла успешно, иначе False.
    """
    try:
        async with aiosqlite.connect(db_path) as db:
            async with db.execute(
                "UPDATE users SET invite_count = invite_count + 1 WHERE user_id = ?",
                (user_id,),
            ) as cursor:
                if cursor.rowcount == 0:  # Проверяем, была ли затронута строка
                    return False
            await db.commit()
            return True
    except Exception as e:
        print(f"Ошибка при обновлении invite_count: {e}")
        return False


async def get_invite_count(db_path: str, user_id: int) -> int:
    """
    Получает значение invite_count для указанного user_id.

    :param db_path: Полный путь к БД (например, 'data/database.db').
    :param user_id: Идентификатор пользователя, для которого нужно получить invite_count.
    :return: Значение invite_count, или -1, если пользователь не найден.
    """
    try:
        async with aiosqlite.connect(db_path) as db:
            async with db.execute(
                "SELECT invite_count FROM users WHERE user_id = ?", (user_id,)
            ) as cursor:
                result = await cursor.fetchone()
                return result[0] if result else -1
    except Exception as e:
        print(f"Ошибка при получении invite_count: {e}")
        return -1


async def get_user_count(db_path: str) -> int:
    """
    Возвращает количество пользователей в таблице users.

    :param db_path: Полный путь к БД (например, 'data/database.db').
    :return: Количество пользователей в таблице, или -1 в случае ошибки.
    """
    try:
        async with aiosqlite.connect(db_path) as db:
            async with db.execute("SELECT COUNT(*) FROM users") as cursor:
                result = await cursor.fetchone()
                return result[0] if result else 0
    except Exception as e:
        print(f"Ошибка при получении количества пользователей: {e}")
        return -1


async def get_all_user_ids(db_path: str) -> list[int]:
    """
    Возвращает список user_id всех пользователей из таблицы users.

    :param db_path: Полный путь к БД (например, 'data/database.db').
    :return: Список user_id, или пустой список в случае ошибки.
    """
    try:
        async with aiosqlite.connect(db_path) as db:
            async with db.execute("SELECT user_id FROM users") as cursor:
                return [row[0] for row in await cursor.fetchall()]
    except Exception as e:
        print(f"Ошибка при получении списка user_id: {e}")
        return []
