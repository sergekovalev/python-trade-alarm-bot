from lib.db import Db


context_types = {
    'add_wallet': {}
}


class Context(object):
    __user_id = None
    __context = None
    
    can_clear = True
    
    @property
    def root(self):
        if self.__context is not None:
            return self.__context['root']
        else:
            return {}
            
    @property
    def step(self):
        if self.__context is not None:
            return self.__context['step']
        else:
            return {}
    
    @property
    def payload(self):
        return self.__context

    def __init__(self, user_id):
        self.__user_id = user_id
        self.__context = Db().get_user_context(user_id=user_id)

    def set_context(self, context):
        Db().set_user_context(user_id=self.__user_id, context=context)

        self.__context = context

        self.can_clear = False
    
    def clear_context(self):
        Db().set_user_context(user_id=self.__user_id, context=None)
        
        self.__context = None

        self.can_clear = True
