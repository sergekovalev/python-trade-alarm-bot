class Entity(object):
    __data = None
    
    def __init__(self, data):
        self.__data = data
        
    def __str__(self):
        return str(self.__data)

    def save(self):
        print(self)