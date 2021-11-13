#Server to Run WebBot and to make for easy user input.

import flask
from flask import request
from flask.templating import render_template

app = flask.Flask(__name__)

#Default Route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submitted', methods=['GET', 'POST'])
def submitted():
    fname=request.form['fname']
    lname=request.form['lname']
    email=request.form['email']

    print(fname)

    return render_template('submitted.html')

    

#Runs WebBot through a single cycle.
#@app.route('/run', methods=['POST'])

#Ends WebBot Cycle
#@app.route('/end', methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
