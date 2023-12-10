class UserData:
    def __init__(self, name, level=1, score=0):
        self.name = name
        self.level = level
        self.score = score

    def update_level(self, new_level):
        self.level = new_level

    def update_score(self, points):
        self.score += points

    def reset(self):
        self.level = 1
        self.score = 0

    def __str__(self):
        return f"User: {self.name}, Level: {self.level}, Score: {self.score}"
