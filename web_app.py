rom flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return'<h1> Hello world but bigger</h1>'

@app.route('/about')
def about_page():
    return '<h1> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Tiny_house%2C_Portland.jpg/520px-Tiny_house%2C_Portland.jpg" alt="WwW"> </h1>'
