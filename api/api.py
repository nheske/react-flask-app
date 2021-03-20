import time
from flask import Flask

app= Flask(__name__)


@app.route('/time')
def get_current_time():
    # return {'time': "hello"}
    ticks = time.time()
    print("Number of ticks since 12:00am, January 1, 1970:", ticks)
    return {'time': time.time()}


@app.route('/image')
def get_image():
    html = "<img src='/1951usaf_test_target.jpg' alt='logo'>"
    return html


@app.route('/green')
def get_green():
    html = "<img src='/green.png' alt='logo' >"
    return html


@app.route('/black')
def get_black():
    html = "<img src='/black.png' alt='logo' >"
    return html


print(get_current_time())