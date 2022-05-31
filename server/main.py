from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def home():
    with open('test.png') as fp:
        return Response(fp, mimetype='image/png')


app.run(debug=True)