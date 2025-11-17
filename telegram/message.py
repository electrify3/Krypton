from .user import User

class Message:
    def __init__(self, data: dict):
        self.id: int = data["message_id"]
        self.text: str = data.get("text")
        self.date = data.get("date")

        self.author = User(data["from"])
        self.chat_id: int = data["chat"]["id"]
