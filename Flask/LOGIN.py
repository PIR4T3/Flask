from flask import *

app = Flask(__name__)

app.secret_key = b'adggkjd$%^\]/'

def valid_login(u,p):
   if u == 'admin' and p == 'password' or u == 'user' and p == 'pswd':
      return 1
      
@app.route('/')
def home():
   return render_template('login.html')
   
@app.route('/about')
def about():
   return render_template('about.html')
   
@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      if valid_login(request.form['username'],request.form['password']):
         session['username'] = request.form['username']
         return redirect(url_for('home'))
   return render_template('login.html')      
   
@app.route('/logout')
def logout():
   session.pop('username',None)
   return redirect(url_for('home'))
   
   
if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0', port=5000)	
