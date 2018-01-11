'''
C15716369
Vlad Ciobanu
Python Website hosted using Flask
'''

class Comment:
    '''''''''''''''''''Constructor'''''''''''''''''''
    def __init__(self, name, message, date, avatar,email):
        self.__name = name
        self.__message = message
        self.__date = date
        self.__avatar = avatar
        self.__email = email
    '''''''''''''''''''Getters'''''''''''''''''''
    def get_ident(self):
        return self.get_name()+self.get_date()+self.get_email()
    
    def get_name(self):
        return self.__name

    def get_message(self):
        return self.__message

    def get_date(self):
        return self.__date

    def get_avatar(self):
        return self.__avatar
    
    def get_email(self):
        return self.__email
    '''''''''''''''''''Setters'''''''''''''''''''
    def set_name(self, value):
        self.__name = value

    def set_message(self, value):
        self.__message = value

    def set_date(self, value):
        self.__date = value

    def set_avatar(self, value):
        self.__avatar = value

    def set_email(self, value):
        self.__email = value
    '''Compare to'''
    def __lt__(self, otherComment):
        return self.get_date() < otherComment.get_date()
    '''Adds a ; between the entities from the string'''
    def __str__(self):
        tmpString=""
        tmpString+=str(self.__name)+";"
        tmpString+=str(self.__message)+";"
        tmpString+=str(self.__date)+";"
        tmpString+=str(self.__avatar)+";"
        tmpString+=str(self.__email)+";"
        return tmpString