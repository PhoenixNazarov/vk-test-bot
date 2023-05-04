from abc import ABC, abstractmethod


class CleanerRepository(ABC):
    @abstractmethod
    async def add_message(self, chat_id: int, message_id: int):
        pass

    @abstractmethod
    async def remove_message(self, chat_id: int, message_id: int):
        pass

    @abstractmethod
    async def get_all_messages(self) -> list[(int, int, int)]:
        pass
