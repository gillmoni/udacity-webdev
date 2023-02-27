from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

# From previous C01L02
# connection = psycopg2.connect("dbname=example user=postgres password=1121")

# Set configuration variable on FLaskApp
# TODO: Move creds out
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1121@localhost:5432/example'


#Link an instance with SQLAlchemy with flask App
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello, Moni!"


# This is second way to run flask
# $:python <filename>
if __name__ == "__main__":
    app.run("host=0.0.0.0", debug=True)