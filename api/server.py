import time
from flask import Flask
import api.utils.utility as utils
from flask import jsonify

app= Flask(__name__)


import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


@app.route('/plot')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig


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


@app.route('/img')
def get_img():
    image_uri = utils.brownian_motion()
    uri = [{"url": image_uri}]
    uri = [{"breeds":[],"id":"ry0d8xXz0","url":image_uri,"width":796,"height":652}]
    uri = [{"breeds":[],"id":"ry0d8xXz0","url":"https://cdn2.thecatapi.com/images/ry0d8xXz0.jpg","width":796,"height":652}]
    json = jsonify(uri)
    print(json)
    return json


@app.route('/cat2')
def get_cat2():
    uri = utils.get_random_image()
    uri_list = [{"breeds":[],"id":"ry0d8xXz0","url":uri,"width":796,"height":652}]
    json = jsonify(uri_list)
    print(json)
    return json


@app.route('/cat')
def get_cat():
    uri = [{"breeds":[],"id":"ry0d8xXz0","url":"https://cdn2.thecatapi.com/images/ry0d8xXz0.jpg","width":796,"height":652}]
    json = jsonify(uri)
    print(json)
    return json



print(get_current_time())



