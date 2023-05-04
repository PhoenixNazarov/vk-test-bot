import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import config
import routers
from module_middleware import ModuleMiddleware
from modules.cleaner.cleaner_repository_impl import CleanerRepositoryJSON
from modules.cleaner.cleaner_service import CleanerService
from modules.encryption.encryption_service import EncryptionService
from modules.passwords.passwords_repository_impl import PasswordsRepositoryJSON
from modules.passwords.passwords_service import PasswordsService

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")

dp = Dispatcher(storage=MemoryStorage())

# Middleware
if not os.path.isfile(config.MESSAGES_FILE):
    with open(config.MESSAGES_FILE, 'w') as file:
        file.write("{}")

try:
    os.listdir(config.PASSWORDS_DIRECTORY)
except FileNotFoundError:
    os.mkdir(config.PASSWORDS_DIRECTORY)


cleaner_service = CleanerService(
    bot,
    CleanerRepositoryJSON(config.MESSAGES_FILE),
)

authorization_middleware = ModuleMiddleware(
    PasswordsService(
        PasswordsRepositoryJSON(config.PASSWORDS_DIRECTORY),
        EncryptionService()
    ),
    cleaner_service
)
dp.update.middleware(authorization_middleware)

# Routers
dp.include_router(routers.router)


async def main():
    await cleaner_service.check_cache_messages()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


asyncio.run(main())
