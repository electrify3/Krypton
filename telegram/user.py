from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .client import Client

class User:
    def __init__(self, client: Client, user_json: dict):
        self._client = client
        self.id: int = user_json["id"]
        self.name: str = user_json["first_name"]
        self.username: str = user_json.get("username")
