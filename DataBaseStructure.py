'''
C15716369
Vlad Ciobanu
Python Website hosted using Flask
'''
class DataBaseStructureException(Exception):
    pass 

class DataBaseStructure:
    '''
    classdocs
    '''
    def __init__(self):
        '''Constructor '''
        self.__entities ={}
        
        
    def save(self,entity):
        '''Add a entity to the textfile'''
        if entity.get_ident() in self.__entities:
            raise DataBaseStructureException("Id already present in the DataBaseStructure!")
        self.__entities[entity.get_ident()]=entity
    
        
    def getAll(self):
        '''Returns all data from textfile'''
        l=[]
        for x in self.__entities.values():
            l.append(x)
        return l
        
    def __add__(self,entity):
        self.save(entity)