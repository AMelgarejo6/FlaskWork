from flask import Flask, render_template, redirect, request
#use redirect when dealing with a post request function
#use request to access the data
app = Flask(__name__)

@app.route('/')

def formpage():
    return render_template('form.html')

@app.route('/sundaes/post', methods=["post"]) #any route that accepts a post request we must declare that it will
#methods is how we tell the route that it will accept a post request

def sundae_submit():
    #request builds a dictionary with the form
    #do stuff with the form info
    print(request.form["name"])
    print(request.form["flavor"])
    if "whipped" in request.form: #how to deal with a checkbox in a form
        whipped = True
    else:
        whipped = False
    print(whipped)
    return redirect('/success')


@app.route('/success')

def success():
    return "you did it!"

if __name__ == "__main__":
    app.run(debug=True)