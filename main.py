from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello():
    user_ip= reques.remote_addr
    return 'heello from hell, tu IP es {}'.format(user_ip)

@app.route('/hi')
def hi():
    return 'Weel this is another gretting'
