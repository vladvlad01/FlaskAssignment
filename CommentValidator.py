'''
C15716369
Vlad Ciobanu
Python Website hosted using Flask
'''
from Comment import Comment
import re
'''This class validates the comments!!!'''
class CommentValidationException(Exception):
    pass    


'''This class verifies if the fields in the index page are valid '''    
class CommentValidator:    
    @staticmethod 
    def validate(comment):
        errors=""
        if len(comment.get_name())==0:
            errors+="Name can not be empty!\n"
        if len(comment.get_message())==0:
            errors+="Message can not be empty!\n"
        if len(comment.get_email())==0:
            errors+="Email can not be empty!\n"
        if not re.match(r"[^@]+@[^@]+\.[^@]+", comment.get_email()):
            errors+="Mail format is not valid\n"
        if len(errors)>0:
            raise CommentValidationException(errors)    