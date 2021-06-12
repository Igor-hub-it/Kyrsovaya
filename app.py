from flask import Flask, render_template, redirect, request
# from jinja2 import Environment
from datetime import datetime, date

app = Flask(__name__)

@app.route('/',)
def includes():
    return render_template('includes.html')

if __name__ == "__main__":
    app.run()
