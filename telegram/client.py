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

    async def send(self, channel_id: int, text: str, *args, **kwargs) -> Message:
        data = await self.http.post('sendMessage', chat_id = channel_id, text = text, *args, **kwargs)
        return Message(self, data['result'])
    
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
                    msg = Message(self, update["message"])
                    
                    try:
                        await self.dispatch("on_message", msg)
                    except Exception as e:
                        print(f'Ignored Exception in Event Dispatcher: {e}')


    async def start(self, token: str):
        self.running = True
        self.http = HTTPClient(token)

        try:
            await self.poll_updates()
        finally:
            self.http.close()


    def run(self, token: str):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self.start(token))