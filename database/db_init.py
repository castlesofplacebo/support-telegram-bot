from aiogram.contrib.fsm_storage.memory import MemoryStorage
from tortoise import Tortoise

storage = MemoryStorage()


async def run_db():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['__main__']}
    )
    await Tortoise.generate_schemas()
