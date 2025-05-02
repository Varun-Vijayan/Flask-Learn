from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"
@app.route('/page')
def page():
    return "Hello Page"
@app.route('/user/<name>')
def userInfo(name):
    return f'''Hello {name[100]}'''

if __name__ == "__main__":
    app.run(debug=True)