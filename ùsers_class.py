class User:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def print_git(self):
        return f'{self.name} has git.'

    def print_another_thing(self):
        return 'fck'