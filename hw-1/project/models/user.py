import uuid


class User:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.comments_count = 0
        self.rate = 0
        self.is_banned = False

    def edit_name(self, new_name):
        self.name = new_name
        return self.name

    def increment_rate(self):
        self.rate += 1
        return self.rate

    def ban_user(self):
        self.is_banned = True
        return self.is_banned

    def unban_user(self):
        self.is_banned = False
        return self.is_banned

    def __repr__(self):
        pass
