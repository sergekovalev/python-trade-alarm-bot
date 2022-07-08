from entities.entity import Entity


class UserEntity(Entity):
    __name = None
    
    @property
    def name(self):
        return self.__name
   
    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def wallet(self):
        return self.schema['wallet'] if 'wallet' in self.schema.keys() else None
    
    @wallet.setter
    def wallet(self, value):
        self.schema['wallet'] = value

    @property
    def follow(self):
        return self.schema['follow'] if 'follow' in self.schema.keys() else []

    @follow.setter
    def follow(self, value):
        follow = self.follow
        follow.append(value)
        
        self.schema['follow'] = follow
    
    @property
    def notifications(self):
        return self.schema['notifications'] if 'notifications' in self.schema.keys() else []

    @property
    def dashboard(self):
        return self.schema['follow'] if 'follow' in self.schema.keys() else []

    def __init__(self, data):
        super().__init__('users', data)
