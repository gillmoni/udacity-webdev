from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=[
        { 'description':'Dynamic item 1' },
        { 'description':'Dynamic item 2' },
        { 'description':'Dynamic item 3' },
        { 'description':'Dynamic item 4' },
        ])