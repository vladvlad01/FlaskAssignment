'''
C15716369
Vlad Ciobanu
Python Website hosted using Flask
'''
import os.path

'''This class manage the file handling'''
class filemanage():
    fName = "save.txt"
    '''This function write and read the data from textfile '''
    def sync(self,commentController,forceWrite):
        if os.path.isfile(self.fName) and not forceWrite:
            f = open(self.fName,"r")
                        
            line = "none"
            while line!="":
                line = f.readline().strip()
                attrs = line.split(";")
                if len(attrs)>=5:
                    commentController.add_Comment(attrs[0],attrs[4],attrs[1],attrs[3],attrs[2])    
                                                   #name   #email    #msg     #avt     #date
        else:
            f = open(self.fName,"w")
            for x in commentController.getAll():
                stringalized = str(x)
                f.write(stringalized+"\n")
            f.close()