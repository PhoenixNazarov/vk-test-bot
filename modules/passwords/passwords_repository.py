from abc import ABC, abstractmethod


class PasswordsRepository(ABC):
    @abstractmethod
    async def save_password(self, user_id: str, service: str, password: str):
        pass

    @abstractmethod
    async def get_password(self, user_id: str, service: str):
        pass

    @abstractmethod
    async def del_password(self, user_id: str, service: str):
        pass
