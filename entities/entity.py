from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lib.db import Db


class Entity(object):
    __collection = None
    schema = None

    @property
    def id(self):
        return self.schema['id']

    def __init__(self, collection: str, data):
        self.schema = data
        self.__collection = collection
        
    def __str__(self):
        return str(self.schema)

    def save(self):
        Db()[self.__collection].update_one({'id': self.id}, {'$set': self.schema})
