#Server to Run WebBot and to make for easy user input.
#Flask Imports
import flask
from flask import request
from flask.templating import render_template

import WebBot
app = flask.Flask(__name__)

#Global Variables

#Default Route
@app.route('/')
def home():
    return render_template('index.html')

#Gets the Input Values and makes the call to run the bot
@app.route('/submitted', methods=['GET', 'POST'])
def submitted():

    runBot(request.form['fname'],request.form['lname'],request.form['email'], request.form['password'])

    return render_template('submitted.html')

def runBot(fname, lname, email, password):

    #instantiates the object
    bot = WebBot.WebBot()

    bot.login(email, password)

    print("Bot is now Running....")


    return

#default method
if __name__ == '__main__':
    app.run(debug=True)