import hashlib

import cryptocode

import config


class EncryptionService:
    async def encrypt_user_id(self, user_id: int) -> str:
        return hashlib.sha256((str(user_id) + config.ENCRYPT_USER_TOKEN).encode()).hexdigest()

    async def encrypt_password(self, user_id: int, password: str) -> str:
        return cryptocode.encrypt(password, config.ENCRYPT_PASSWORD_TOKEN)

    async def decrypt_password(self, user_id: int, password: str) -> str:
        return cryptocode.decrypt(password, config.ENCRYPT_PASSWORD_TOKEN)
