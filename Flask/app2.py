from flask import *
from lib.index import Index

app = Flask(__name__)

@app.route('/')
def index():
	return Index.show_indexpage(app)

@app.route('/name')
def name():
	return Index.show_namepage(app)

if __name__ == '__main__':
	app.run('0.0.0.0',5050,True)
