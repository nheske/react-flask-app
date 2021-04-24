import time
import flask
from flask import Flask, render_template, request
import api.utils.utility as utils
from flask import jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)


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


@app.route('/')
def my_index():
    flask.render_template("index.html", token="hello flask-react")


@app.route('/uploader')
def upload_html():
    return render_template('upload.html')


@app.route('/files')
def list_files():
    return ""


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        folder = "../uploads/"
        f.save(folder+secure_filename(f.filename))
        return 'file uploaded successfully'


@app.route('/api/time')
def get_current_time():
    # return {'time': "hello"}
    ticks = time.time()
    print("Number of ticks since 12:00am, January 1, 1970:", ticks)
    return {'time': time.time()}


@app.route('/api/img_json')
def get_img_json():
    uri = utils.get_random_image()
    uri_list = [{"breeds":[],"id":"ry0d8xXz0","url":uri,"width":796,"height":652}]
    uri_list = [{"url": uri}]
    json = jsonify(uri_list)
    print(json)
    return json


print(get_current_time())



