from .user import User

class Message:
    def __init__(self, data: dict):
        self.message_id = data["message_id"]
        self.text = data.get("text")
        self.date = data.get("date")

        self.from_user = User(data["from"])
        self.chat_id = data["chat"]["id"]
