from singleton_decorator import singleton
import pymongo


@singleton
class Db(object):
    __db = None
    
    def __init__(self):
        client = pymongo.MongoClient("localhost", 27017)
        self.__db = client.tradebot
        
    def user_exists(self, user_id):
        existing_user = self.__db.users.find_one({'id': user_id})
        
        return existing_user is not None
    
    def add_user(self, user):
        existing_user = self.__db.users.find_one({'id': user['id']})

        if existing_user is None:
            self.__db.users.insert_one(user)
    
    def get_users(self):
        return self.__db.users.find()
        
    def get_user(self, user_id):
        return self.__db.users.find_one({'id': user_id})

    def get_user_context(self, user_id):
        user = self.get_user(user_id)
        
        if user is None:
            return None

        return user['context'] if 'context' in user.keys() else None
    
    def set_user_context(self, user_id, context):
        self.__db.users.update_one({'id': user_id}, {'$set': {'context': context}})

    def set_quotes(self, data):
        self.__db.quotes.delete_many({})
        self.__db.quotes.insert_many(data)
        
    def get_quotes(self):
        return self.__db.quotes.find()
    
    def get_wallet(self, user_id):
        return self.get_user(user_id)['wallet']
    
    def update_wallet(self, user_id, data):
        wallet = self.get_wallet(user_id)

        self.__db.wallets.update_one({'user_id': user_id}, {**wallet, **data})