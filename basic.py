from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    letters = list(name)
    userLoggedIn =False
    return render_template('page.html',name=name,letters=letters,userLoggedIn=userLoggedIn)

@app.route('/dummyPage')
def dummyPage():
    return('dummy page')

if __name__ == "__main__":
    app.run(debug=True)