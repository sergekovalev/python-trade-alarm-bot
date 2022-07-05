from aiogram import types
from lib.Context import Context
from lib.db import Db


class MessageEvent(object):
    __message = None
    __context = None
    
    @property
    def message(self):
        return self.__message
    
    @property
    def context(self):
        return self.__context
    
    @property
    def user(self):
        return Db().get_user(self.__message.chat.id)
    
    @property
    def user_id(self):
        return self.__message.chat.id

    def __init__(self, message: types.Message):
        self.__message = message
        self.__context = Context(user_id=message.chat.id)

    def contains_context(self):
        return self.__context.payload is not None