class Cow():
    def __init__(self, name,feeds):
        self.name=name
        self.feeds=feeds
    def write(self):
        print(self.name.title())
