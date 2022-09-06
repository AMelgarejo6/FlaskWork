from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def landing_page():
    if 'counter' not in session:
        session["counter"] = 0
    return render_template('landing_page.html')

@app.route('/route')
def increment():
    session["counter"] += 1
    return redirect('/')

@app.route('/delete')
def delete():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)