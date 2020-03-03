from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    title = "Hello Universe!"

    user = {'name': 'azerty', 'age': 22}

    numbers = [1, 2, 3]
    return render_template('index.html', title=title, user=user, numbers=numbers)
