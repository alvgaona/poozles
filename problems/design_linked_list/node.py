class Node(object):
    def __init__(self, value):
        self.__value = value
        self.__next = None
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, next):
        self.__next = next
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
