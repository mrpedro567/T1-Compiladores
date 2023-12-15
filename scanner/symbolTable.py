from tokenClass import Token


class SymbolTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def get(self, key):
        if key in self.table:
            return self.table[key]
        else:
            return None
