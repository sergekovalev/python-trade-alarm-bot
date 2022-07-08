from entities.user_notification import UserNotificationEntity
from entities.entity import Entity


class UserEntity(Entity):
    __notifications = None
    
    @property
    def id(self):
        return self.__data['id']
    
    @property
    def wallet(self):
        return self.__data['wallet'] if 'wallet' in self.__data.keys() else None
    
    @property
    def notifications(self):
        return self.__notifications

    @property
    def dashboard(self):
        return self.__data['follow'] if 'follow' in self.__data.keys() else []
    
    @property
    def raw_data(self):
        return self.__data

    def __init__(self, data):
        super(data)
        
        notifications = data['notifications'] if 'notifications' in data.keys() else []
        self.__notifications = [UserNotificationEntity(n) for n in notifications]
