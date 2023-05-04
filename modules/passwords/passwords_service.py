from typing import Optional

from modules.encryption.encryption_service import EncryptionService
from modules.passwords.passwords_repository import PasswordsRepository


class PasswordsService:
    def __init__(self, passwords_repository: PasswordsRepository, encryption_service: EncryptionService):
        self.passwords_repository = passwords_repository
        self.encryption_service = encryption_service

    async def set_password(self, user_id: int, service: str, password: str):
        encrypt_user_id = await self.encryption_service.encrypt_user_id(user_id)
        encrypt_password = await self.encryption_service.encrypt_password(user_id, password)
        await self.passwords_repository.save_password(encrypt_user_id, service, encrypt_password)

    async def get_password(self, user_id: int, service: str) -> Optional[str]:
        encrypt_user_id = await self.encryption_service.encrypt_user_id(user_id)
        password = await self.passwords_repository.get_password(encrypt_user_id, service)
        if not password:
            return None
        return await self.encryption_service.decrypt_password(user_id, password)

    async def del_password(self, user_id: int, service: str) -> bool:
        encrypt_user_id = await self.encryption_service.encrypt_user_id(user_id)
        return await self.passwords_repository.del_password(encrypt_user_id, service)
