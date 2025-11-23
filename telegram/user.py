from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .client import Client

class User:
    def __init__(self, client: Client, user_json: dict):
        self._client = client
        self.id = user_json["id"]
        self.name = user_json["first_name"]
        self.username = user_json.get("username")
