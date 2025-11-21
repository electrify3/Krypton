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
            try:
                data = await self.http.get(
                    "getUpdates", offset=self.offset, timeout=10
                )
            except Exception as e:
                print(f'Exception ignored in getUpdates: {e}')
                continue

            if not data.get('result'):
                continue

            for update in data["result"]:
                self.offset = update["update_id"] + 1

                if "message" in update:
                    msg = Message(update["message"])
                    
                    try:
                        await self.dispatch("on_message", msg)
                    except Exception as e:
                        print(f'Ignored Exception in Event Dispatcher: {e}')


    def run(self, token: str):
        self.running = True
        self.http = HTTPClient(token)
        asyncio.run(self.poll_updates())