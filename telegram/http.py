import aiohttp

from typing import ClassVar

class HTTPClient:
    BASE: ClassVar[str] = 'https://api.telegram.org/bot{}/{}'

    def __init__(self, token: str):
        self._token: str = token
        self._session: aiohttp.ClientSession | None = None

    async def _ensure_session(self) -> None:
        if self._session is None:
            self._session = aiohttp.ClientSession()

    async def get(self, method: str, *args, **kwargs) -> dict:
        url = self.BASE.format(self._token, method)

        await self._ensure_session()
        
        try:
            async with self._session.get(url, params=kwargs) as response:
                return await response.json()
        except Exception as e:
            print(f'HTTP GET Error: {e}')
    

    async def post(self, method: str, *args, **kwargs) -> dict:
        url = self.BASE.format(self._token, method)

        await self._ensure_session()
        
        try:
            async with self._session.post(url, json=kwargs) as response:
                return await response.json()
        except Exception as e:
            print(f'HTTP POST Error: {e}')

    async def close(self):
        if self._session:
            await self._session.close()

