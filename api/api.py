import time
from flask import flask

app= flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}