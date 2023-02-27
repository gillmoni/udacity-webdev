from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

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

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())