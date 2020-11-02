from flask import Flask
from flask import flash, render_template, request
from arm_flask import app
from arm_flask.balance_checker import check_if_is_balanced

@app.route('/', methods=('GET', 'POST'))
def hello_world():
    if request.method == 'POST':
        error = None
        pattern = request.form['pattern']
        if not pattern:
            error = 'A pattern is required.'

        try:
            result = check_if_is_balanced(pattern)
        except:
            flash("There was an error, refresh the page and try again please.")
        flash(result)
        # flash(error)
    return render_template('home.html')