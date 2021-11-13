#Server to Run WebBot and to make for easy user input.

from Flask import Flask

app = Flask(__name__)
#Has you enter your login information for the WebBot. Gets the actual information and saves it as a string for the webbot.
@app.route('/login', methods=['GET'])

#Runs WebBot through a single cycle.
@app.route('/run', methods=['POST'])

#Ends WebBot Cycle
@app.route('/end', methods=['POST'])

if __name__ == '__main__'
    app.run(host='0.0.0.0', port=port)