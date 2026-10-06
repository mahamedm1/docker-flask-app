from flask import Flask

app = Flask(__name__)

@app.route('/') 

def welcome_page():
    return f'Welcome to my homepage'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

