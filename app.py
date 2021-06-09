from flask import Flask, render_template, redirect, request
# from jinja2 import Environment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('includs.html')

if __name__ == "__main__":
    app.run()

