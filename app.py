from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import requests

DATABASE = '/tmp/app.db'
DEGUB = True
SECRET_KEY = 'dev key'
USERNAME = 'Max'
PASSWORD = 'pass'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def main():
    return render_template('app.html')



if  __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')