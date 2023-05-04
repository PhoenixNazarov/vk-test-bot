from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Update


class ModuleMiddleware(BaseMiddleware):
    def __init__(self, password_service, cleaner_service):
        self.password_service = password_service
        self.cleaner_service = cleaner_service

    async def __call__(
            self,
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any]
    ) -> Any:
        if not event.message:
            return
        if event.message.chat.type != 'private':
            return

        data['password_service'] = self.password_service
        data['cleaner_service'] = self.cleaner_service

        return await handler(event, data)
