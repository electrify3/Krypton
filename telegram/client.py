import asyncio

from .events import EventManager
from .http import HTTPClient
from .message import Message

class Client(EventManager):
    def __init__(self):
        super().__init__()
        self.http: HTTPClient | None = None
        self.running: bool = False
        self.offset: int = 0

    async def send(self, channel_id: int, text: str, *args, **kwargs) -> dict:
        return await self.http.post('sendMessage', chat_id = channel_id, text = text, *args, **kwargs)
    
    async def poll_updates(self):
        while self.running:
            data = await self.http.get(
                "getUpdates", offset=self.offset, timeout=10
            )

            if data['result']:
                for update in data["result"]:
                    self.offset = update["update_id"] + 1
                    if "message" in update:
                        msg = Message(update["message"])
                        await self.dispatch("on_message", msg)

    def run(self, token: str):
        self.running = True
        self.http = HTTPClient(token)
        asyncio.run(self.poll_updates())