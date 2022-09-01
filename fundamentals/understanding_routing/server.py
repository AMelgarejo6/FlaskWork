from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    return "Hello World!"

@app.route('/dojo')

def print_dojo():
    return "Dojo!"

@app.route('/say/<name>')

def print_name(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:times>/<word>')

def repeating(times, word):
    return word * times

if __name__ == "__main__":
    app.run(debug=True)