from typing import TYPE_CHECKING

from .user import User
from .channel import Channel

if TYPE_CHECKING:
    from .client import Client

class Message:
    def __init__(self, client: Client, message_json: dict):
        self._client = client

        self.id: int = message_json["message_id"]
        self.text: str = message_json.get("text")
        self.date = message_json.get("date")

        self._author = message_json["from"]
        self._chat: dict = message_json["chat"]
    
    @property
    def channel(self) -> Channel:
        return Channel(self._client, self._chat)
    
    @property
    def author(self) -> User:
        return User(self._client, self._author)
    
    async def reply(self, text: str, *args, **kwargs) -> Message:
        reply_para = {
            'message_id': self.id
        }
        return await self._client.send(self.channel.id, text=text, reply_parameters=reply_para, *args, **kwargs)

    
    def __str__(self):
        return f'{self.author.username}: {self.text}'
