import json
import os
from pathlib import Path

from modules.passwords.passwords_repository import PasswordsRepository


class PasswordsRepositoryJSON(PasswordsRepository):
    def __init__(self, password_dir: str):
        self.password_dir = Path(password_dir)

    def _load_user_file(self, user_id: str) -> dict:
        if user_id not in os.listdir(self.password_dir):
            return {}
        with open(self.password_dir / user_id, 'r') as file:
            return json.loads(file.read())

    def _save_user_file(self, user_id: str, data: dict):
        with open(self.password_dir / user_id, 'w') as file:
            file.write(json.dumps(data))

    async def save_password(self, user_id: str, service: str, password: str):
        data = self._load_user_file(user_id)
        data[service] = password
        self._save_user_file(user_id, data)

    async def get_password(self, user_id: str, service: str):
        return self._load_user_file(user_id).get(service)

    async def del_password(self, user_id: str, service: str) -> bool:
        data = self._load_user_file(user_id)
        if service in data:
            data.pop(service)
            self._save_user_file(user_id, data)
            return True
        return False
