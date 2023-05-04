from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from modules.cleaner.cleaner_service import CleanerService
from modules.passwords.passwords_service import PasswordsService

router = Router()


@router.message(Command(commands=['set']))
async def set_password(message: Message, password_service: PasswordsService, cleaner_service: CleanerService):
    await cleaner_service.delete_message(message)
    if len(message.text.split(" ")) != 3:
        return await message.answer(f"⚙️ Для того чтобы воспользоваться командой /set, напишите через пробел название "
                                    f"сервиса и пароль, который вы хотите сохранить")

    service = message.text.split(" ")[1]
    password = message.text.split(" ")[2]
    await password_service.set_password(message.from_user.id, service, password)
    await message.answer(f"💾 Пароль для сервиса <b>{service}</b> успешно сохранён!")


@router.message(Command(commands=['get']))
async def get_password(message: Message, password_service: PasswordsService, cleaner_service: CleanerService):
    if len(message.text.split(" ")) != 2:
        return await message.answer(f"⚙️ Для того чтобы воспользоваться командой /get, напишите через пробел название "
                                    f"сервиса, для которого вы хотите получить пароль")

    service = message.text.split(" ")[1]
    password = await password_service.get_password(message.from_user.id, service)
    if password:
        message = await message.answer(f"🧑‍💻 Пароль для сервиса <b>{service}</b>: <code>{password}</code>")
        await cleaner_service.delete_message(message)
    else:
        await message.answer(f"🫗 Пароль для сервиса <b>{service}</b> не найден")


@router.message(Command(commands=['del']))
async def del_password(message: Message, password_service: PasswordsService):
    if len(message.text.split(" ")) != 2:
        return await message.answer(f"⚙️ Для того чтобы воспользоваться командой /get, напишите через пробел название "
                                    f"сервиса, для которого вы хотите удалить пароль")

    service = message.text.split(" ")[1]
    if not await password_service.del_password(message.from_user.id, service):
        await message.answer(f"🫗 Пароль для сервиса <b>{service}</b> не найден")
    else:
        await message.answer(f"🗑 Пароль для сервиса <b>{service}</b> был удалён!")
