## app.py

import csv
from flask import Flask, render_template, jsonify
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