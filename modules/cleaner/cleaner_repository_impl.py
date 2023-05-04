import json
import time
from pathlib import Path

from modules.cleaner.cleaner_repository import CleanerRepository


class CleanerRepositoryJSON(CleanerRepository):
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)

    def _load_base(self) -> dict:
        with open(self.base_path, 'r') as file:
            return json.loads(file.read())

    def _save_base(self, data: dict):
        with open(self.base_path, 'w') as file:
            return file.write(json.dumps(data))

    async def add_message(self, chat_id: int, message_id: int):
        data = self._load_base()
        data.update({f'{chat_id}_{message_id}': int(time.time())})
        self._save_base(data)

    async def remove_message(self, chat_id: int, message_id: int):
        data = self._load_base()
        if f'{chat_id}_{message_id}' in data:
            data.pop(f'{chat_id}_{message_id}')
            self._save_base(data)

    async def get_all_messages(self) -> list[tuple[int, int, int]]:
        data = self._load_base()
        return [(int(k.split('_')[0]), int(k.split('_')[1]), int(v)) for k, v in list(data.items())]
