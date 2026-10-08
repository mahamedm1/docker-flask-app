from flask import Flask
import redis

app = Flask(__name__)

# Connect to the Redis database
r = redis.Redis(
    host='redis',
    port=6379,
    db=0,
    decode_responses=True
)

# Welcome page
@app.route('/')
def welcome_page():
    return 'Welcome to my homepage'

# Visit counter
@app.route('/count')
def count_page():
    count = r.incr('visits')
    return f'This page has been visited {count} times'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)