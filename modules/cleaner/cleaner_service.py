import time

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message

from modules.cleaner.cleaner_repository import CleanerRepository
import asyncio
import config


class CleanerService:
    def __init__(self, bot: Bot, cleaner_repository: CleanerRepository):
        self.bot = bot
        self.cleaner_repository = cleaner_repository

    async def _delete_message(self, chat_id: int, message_id: int):
        try:
            await self.bot.delete_message(chat_id, message_id)
        except TelegramBadRequest:
            pass
        await self.cleaner_repository.remove_message(message_id, chat_id)

    async def _set_timeout_delete(self, chat_id: int, message_id: int):
        await asyncio.sleep(config.TIMEOUT_DELETE)
        await self._delete_message(chat_id, message_id)

    async def check_cache_messages(self):
        for i in await self.cleaner_repository.get_all_messages():
            if i[2] + config.TIMEOUT_DELETE + 5 < time.time():
                await self._delete_message(i[0], i[1])

    async def delete_message(self, message: Message):
        await self.cleaner_repository.add_message(message.message_id, message.chat.id)
        asyncio.get_event_loop().create_task(self._set_timeout_delete(message.chat.id, message.message_id))
