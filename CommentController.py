'''
C15716369
Vlad Ciobanu
Python Website hosted using Flask
'''
from Comment import Comment
from DataBaseStructure import DataBaseStructure,DataBaseStructureException
import datetime

class CommentController:    
    '''
    Constructor:
    '''
    def __init__(self,db,validator):
        self.__db = db
        self.__validator=validator
        
    ''' Add comment function'''
    def add_Comment(self,name,email,message,avatar,date):
        ''' Add a comment to text file'''
        if date==None:
            comment=Comment(name,message,str(datetime.datetime.now()),avatar,email)
        else:
            comment=Comment(name,message,date,avatar,email)
            
        self.__validator.validate(comment)
        try:
            self.__db+comment
            return 1
        except DataBaseStructureException as ex:
            if "already present" in str(ex):
                return 0
            else:
                raise ex
        
    '''Get all comments'''
    def getAll(self):
        """
        This returns all comments from the text file

        """
        return self.__db.getAll()
    
    '''Sort all comments in order to display them '''        
    def sortedComments(self):
        """
        Returns a list of comments ordered by date

        """
        toReturn = []
        
        for tmpCommentEnt in self.getAll():
            toReturn.append(tmpCommentEnt)
            
        toReturn.sort(reverse = True)
        return toReturn