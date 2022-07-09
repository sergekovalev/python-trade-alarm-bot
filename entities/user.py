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

    def add_to_wallet(self, symbol: str, address: str):
        if 'wallet' not in self.schema.keys() or self.schema['wallet'] is None:
            self.schema['wallet'] = []

        self.schema['wallet'].append({
            'symbol': symbol,
            'address': address
        })

        self.save()
