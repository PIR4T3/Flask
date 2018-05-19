from flask import *
import datetime

class Index:
   def __init__(self):
      pass
   
   @staticmethod
   def show_indexpage(app):
      now = datetime.datetime.now()
      timeString = 'PIR4T3'
      templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
      return render_template('index.html',app=app,**templateData)
      
   @staticmethod
   def show_namepage(app):
      return render_template('name.html',app=app)
