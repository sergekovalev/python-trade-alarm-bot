from typing import TYPE_CHECKING
import copy


class Entity(object):
    __collection = None
    schema = None
    db = None
    
    @staticmethod
    def set_db(db):
        Entity.db = db

    @property
    def id(self):
        return self.schema['id']

    def __init__(self, collection: str, data):
        self.schema = copy.deepcopy(data)
        self.__collection = collection

    def __str__(self):
        return str(self.schema)

    def save(self):
        Entity.db.connection[self.__collection].update_one({'id': self.id}, {'$set': self.schema})
