
class ClaseNodo:
    
    #constructor
    def __init__(self, data):
        self.__data__ = data
        self.__link__ = None
    
    def getData(self):
        return self.__data__
    
    def setData(self,data):
        self.__data__ = data
        
    def getLink(self):
        return self.__link__
    
    def setLink(self, link):
        self.__link__  = link