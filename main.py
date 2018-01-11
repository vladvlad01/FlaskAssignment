'''
C15716369
Vlad Ciobanu
Python Website hosted using Flask
'''
from flask import Flask, request,render_template,url_for
from DataBaseStructure import DataBaseStructure
from CommentValidator import CommentValidator
from CommentController import CommentController
from fileman import filemanage

app = Flask(__name__, static_url_path='') 

db = DataBaseStructure()
validator = CommentValidator()
controller = CommentController(db,validator)
saveman = filemanage()
saveman.sync(controller, False)
'''Returns posts ''' 
def getPosts():
    posts = []
    for x in controller.sortedComments():
            entry = {}
            entry['name']=x.get_name()
            entry['message']=x.get_message()
            entry['date']=x.get_date()
            entry['email']=x.get_email()
            entry['avatar']=x.get_avatar()
            posts.append(entry)
    return posts
 
'''Returns last 5 posts on the index page ''' 
@app.route('/')
def root():
    posts = getPosts()
    return render_template('index.html',posts=posts[:5])
 
'''Verifies and adds post'''  
@app.route('/commentAction', methods=['POST'])
def addComment():
    username = request.form['username']
    email = request.form['email']
    message = request.form['comment']
    avatar = request.form['avatarList']+".png"
    
    try:
        controller.add_Comment(username, email, message, avatar, None)
        saveman.sync(controller, True)
        return render_template('index.html',posts=getPosts()[:5])
    except Exception as ex:
        return "Could not add comment. Check your fields. Please use your back button."
 
'''Restrict user to directly access comment action '''   
@app.route('/commentAction', methods=['GET'])
def addCommentCannotGET():
    return "You're not allowed to do this."
 
'''Show all comments '''
@app.route('/viewAllComments', methods=['GET'])
def viewAllComments():
    posts = getPosts()
    return render_template('viewcomments.html',posts=posts)
 
app.run(debug=True)