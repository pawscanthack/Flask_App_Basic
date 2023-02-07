## app.py

import csv
from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_year = datetime.now().year
    return render_template('index.html', current_year=current_year)

@app.route('/this')
def this_page():
    return render_template('this.html')

@app.route('/that')
def that_page():
    return render_template('that.html')

@app.route('/data')
def show_data():
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = list(reader)
    return render_template('data.html', headers=headers, data=data)

@app.route('/test')
def test():
    return render_template('cookie_monster.html')


@app.route('/background_process')
def background_process():
    try:
        test_answer = request.args.get('test_input', 0, type=str)
        if test_answer.lower() == 'cookie monster':
            
            return jsonify(result='COOKIE COOKIE!!')
        else:
            return jsonify(result="Not the monster I was looking for!")
    except Exception as e:
        return str(e)
