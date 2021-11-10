from tinydb import TinyDB, Query
from tinyindex import Index

class DB():
    def __init__(self):
        self.db = TinyDB('db.json')
        self.strat = Query()
    def append(self, data):
        self.db.insert(data)
    def index(self, param):
        return Index(self.db, param)
