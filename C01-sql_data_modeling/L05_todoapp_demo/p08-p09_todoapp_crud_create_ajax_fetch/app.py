from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import redirect, url_for
from flask import jsonify


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1121@localhost:5432/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self) -> str:
        return f'<Todo {self.id} {self.description}>'

# Syncup models with database
with app.app_context():
    db.create_all()

@app.route('/todos/create', methods=['POST', 'GET'])
def create_todo():
    """
    Let the user submit data via POST form
    """
    # Only get description key from te json object returned.
    description = request.get_json()['description']
    todo = Todo(description=description)

    db.session.add(todo)
    db.session.commit()

    # We want to return a jsonified description that comes from todo description item
    return jsonify({
        'description': todo.description
    })

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data=Todo.query.all())
