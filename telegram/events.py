from collections import defaultdict
from functools import wraps
from typing import Callable, Dict, List

class EventManager:

    def __init__(self):
        self._listeners: Dict[str, List[Callable]] = defaultdict(list)
    
    def event(self, name: str = None) -> Callable:
        def decorator(func: Callable) -> Callable:

            event_name = name or func.__name__
            if 'on_message' == event_name:
                self._listeners.setdefault('on_message', []).append(func)
                
            @wraps(func)
            async def wrapper(*args, **kwargs):
                return await func(*args, **kwargs)
            
            return wrapper
        return decorator
    

    async def dispatch(self, name: str, *args, **kwargs) -> None:
        for func in self._listeners.get(name, []):
            await func(*args, **kwargs)