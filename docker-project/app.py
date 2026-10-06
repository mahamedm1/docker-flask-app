from flask import flask

app = Flask(__name__)

@app.route('/') 
    def welcome_page():
        return f'Welcome to my homepage'
