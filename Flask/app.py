from flask import *

app = Flask(__name__)

from flask import request

def valid_login(u,p):
   if u == 'admin' and p == 'password':
      return u,p

def do_the_login():
   name = request.form['username']
   return name

def show_the_login_form():
   return render_template('login.html')

@app.route('/')
def home():
   return 'home'

@app.route('/login', methods=['GET', 'POST'])
def login():
   err = None
   if request.method == 'POST':
      if valid_login(request.form['username'], request.form['password']):
         return do_the_login()
      else:
         err = 'Invalid'
   return show_the_login_form()
   
if __name__ == "__main__":
   app.secret_key = 'sss'
   app.run(debug=True,host='0.0.0.0', port=5000)	
