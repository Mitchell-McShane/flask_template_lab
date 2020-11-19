from flask import render_template
from app import app
from app.models.event_list import events

@app.route('/')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/preorder')
def preorder():
    return render_template('preorder.html', title='Preorder')
