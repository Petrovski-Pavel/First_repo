class User:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def print_git(self):
        return f'{self.name} has git.'