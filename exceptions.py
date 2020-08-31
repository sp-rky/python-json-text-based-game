class InvalidCommand(Exception):
    pass

class ItemDoesNotExist(Exception):
    def __init__(self, item):
        self.item = item
        super().__init__(self.item)

class ItemNotInInventory(Exception):
    def __init__(self, item):
        self.item = item
        super().__init__(self.item)
