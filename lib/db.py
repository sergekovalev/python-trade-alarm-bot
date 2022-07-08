from singleton_decorator import singleton
import pymongo
from entities.user import UserEntity


@singleton
class Db(object):
    __db = None
    
    def __init__(self):
        client = pymongo.MongoClient("localhost", 27017)
        self.__db = client.tradebot
        
    @staticmethod
    def objectify(collection, entity):
        return [entity(_) for _ in collection]
        
    def user_exists(self, user_id: str) -> bool:
        existing_user = self.__db.users.find_one({'id': user_id})
        
        return existing_user is not None
    
    def add_user(self, user: UserEntity):
        existing_user = self.__db.users.find_one({'id': user.id})

        if existing_user is None:
            self.__db.users.insert_one(user.raw_data)
    
    def get_users(self) -> [UserEntity]:
        return Db.objectify(self.__db.users.find(), UserEntity)
        
    def get_user(self, user_id: str) -> UserEntity:
        user = self.__db.users.find_one({'id': user_id})
        
        return Db.objectify([user], UserEntity)[0]

    def get_user_context(self, user_id: str):
        user = self.get_user(user_id)
        
        if user is None:
            return None

        return user['context'] if 'context' in user.keys() else None
    
    def set_user_context(self, user_id: str, context):
        self.__db.users.update_one({'id': user_id}, {'$set': {'context': context}})
        
    def follow_ticker(self, user_id: str, ticker: str):
        user = self.get_user(user_id)
        
        tickers = user['follow'] if 'follow' in user.keys() else []
        
        tickers.append(ticker)
        
        tickers = list(set(tickers))

        self.__db.users.update_one({'id': user_id}, {'$set': {'follow': tickers}})

    def unfollow_ticker(self, user_id: str, ticker: str):
        user = self.get_user(user_id)
        
        tickers = user['follow'] if 'follow' in user.keys() else []
        
        tickers = [t for t in tickers if t != ticker]
        
        self.__db.users.update_one({'id': user_id}, {'$set': {'follow': tickers}})
        
        return tickers

    def set_quotes(self, data):
        self.__db.quotes.delete_many({})
        self.__db.quotes.insert_many(data)
        
    def get_quotes(self):
        return self.__db.quotes.find()
    
    def get_wallet(self, user_id: str):
        return self.get_user(user_id)['wallet']
    
    def update_wallet(self, user_id: str, data):
        wallet = self.get_wallet(user_id)

        self.__db.users.update_one({'id': user_id}, {'$set': {'wallet': {**wallet, **data}}})
        
    def add_notification_to_user(self, user_id: str, notification):
        user = self.get_user(user_id)
        
        notifications = user['notifications'] if 'notifications' in user.keys() else []

        notifications.append(notification)
        
        self.__db.users.update_one({'id': user_id}, {'$set': {'notifications': notifications}})