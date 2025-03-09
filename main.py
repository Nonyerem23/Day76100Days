from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/home')  # Creates the path to the home page
def home():  # Subroutine to create the home page
    page = """"""
    # Three quotes - I'm going to write or paste my HTML code here. The HTML gets assigned to the page variable
    return page  # returns the contents of the page variable


app.run(host='0.0.0.0', port=81)
