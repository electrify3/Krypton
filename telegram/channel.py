from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .client import Client
    from .message import Message

class Channel:
    def __init__(self, client: Client, channel_json: dict):
        self._client = client
        self.id: int = channel_json['id']
    

    async def send(self, text: str, *args, **kwargs) -> Message:
        return await self._client.send(channel_id=self.id, text=text, *args, **kwargs)
    