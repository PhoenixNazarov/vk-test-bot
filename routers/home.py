from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command(commands=['start']))
async def set_password(message: Message):
    await message.answer(f"✨ Привет, я бот, который поможет тебе сохранить твои пароли от твоих сервисов."
                         f"\n\n"
                         f"📋 У бота есть такие команды:"
                         f"\n/set [название сервиса] [пароль]"
                         f"\n/get [название сервиса]"
                         f"\n/del [название сервиса]"
                         f"\n\n👮 Мы заботимся о ваших паролях. Все данные и пароли удаляется через некоторые время и хранятся в зашифрованном виде")


@router.message(Command(commands=['help']))
async def get_password(message: Message):
    await message.answer(f"✨ Привет, я бот, который поможет тебе сохранить твои пароли от твоих сервисов."
                         f"\n\n"
                         f"📋 У бота есть такие команды:"
                         f"\n/set [название сервиса] [пароль]"
                         f"\n/get [название сервиса]"
                         f"\n/del [название сервиса]"
                         f"\n\n👮 Мы заботимся о ваших паролях. Все данные и пароли удаляется через некоторые время и хранятся в зашифрованном виде")
