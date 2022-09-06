from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def mainpage():
    return render_template('landing_page.html')

@app.route('/form', methods=["post"])
def display():
    session["name"] = request.form["name"]
    session["dojo_location"] = request.form["dojo_location"]
    session["favorite_language"] = request.form["favorite_language"]
    session["comment"] = request.form["comment"]
    return redirect('/displaypage')

@app.route('/displaypage')
def displaypage():
    return render_template('form.html')

@app.route('/clear')
def clear_page():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)