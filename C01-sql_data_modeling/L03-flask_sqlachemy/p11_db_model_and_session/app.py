from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

# From previous C01L02
# connection = psycopg2.connect("dbname=example user=postgres password=1121")

# Set configuration variable on FLaskApp
# TODO: Move creds out
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1121@localhost:5432/example'


# db is an interface for interacting with our database
db = SQLAlchemy(app)

# db.Model lets us create and manipulate data models
# Create a Person class with db.model
class Person(db.Model):
    __tablename__ = 'persons'
    # SQLAlchemy takes care of the __init__ method automatically.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

# db.session lets us create and manipulate database transactions
# Create the tables in database
# it won't create the same tables over and over if they exist
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    # Read first record from Persons table
    # This assumes that there's data in table
    person = Person.query.first()
    return f"Hello, {person.name}!"


# This is second way to run flask
# $:python <filename>
if __name__ == "__main__":
    app.run("host=0.0.0.0", debug=True)