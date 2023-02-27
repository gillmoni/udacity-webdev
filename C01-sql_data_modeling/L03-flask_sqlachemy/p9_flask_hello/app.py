from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "Hello, Moni!"


# This is second way to run flask
# $:python <filename>
if __name__ == "__main__":
    app.run("host=0.0.0.0", debug=True)