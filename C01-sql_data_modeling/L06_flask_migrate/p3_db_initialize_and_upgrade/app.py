from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)

# From previous C01L02
# connection = psycopg2.connect("dbname=example user=postgres password=1121")

# Set configuration variable on FLaskApp
# TODO: Move creds out
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1121@localhost:5432/todoapp'


# db is an interface for interacting with our database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# db.Model lets us create and manipulate data models
# Create a Person class with db.model
class Person(db.Model):
    __tablename__ = 'todos'
    # SQLAlchemy takes care of the __init__ method automatically.
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean(), nullable=False, default=False)

# db.session lets us create and manipulate database transactions
# Create the tables in database
# it won't create the same tables over and over if they exist
#with app.app_context():
    #db.create_all()


@app.route('/todos/create', methods=['POST'])
def index():
    # Read first record from Persons table
    # This assumes that there's data in table
    person = Person.query.first()
    return f"Hello, {person.name}!"


# This is second way to run flask
# $:python <filename>
if __name__ == "__main__":
    app.run("host=0.0.0.0", debug=True)