from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello!!'

@app.route('/login', methods=['POST'])
def login():
    rg = request.args
    he = str(request.headers).split('\r\n')
    return f'{rg}\n' + '\n'.join(he)

app.run(host="localhost", debug=True, port=5000)