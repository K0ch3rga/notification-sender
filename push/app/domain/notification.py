class Notification:
    def __init__(self, notification_type: str, address: str, title: str, message: str):
        # self.id = id
        self.notification_type = notification_type
        self.address = address
        self.title = title
        self.message = message

    def __repr__(self) -> str:
        return f"<Notification {self.id}>"
