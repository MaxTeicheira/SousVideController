from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import requests, os, random

DATABASE = '/tmp/app.db'
DEGUB = True
SECRET_KEY = 'dev key'
USERNAME = 'Max'
PASSWORD = 'pass'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def main():
    rand_num = random.random()
    return render_template('app.html', rand_num=rand_num)

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/2')
def test2():
  return render_template('app2.html')


if  __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
