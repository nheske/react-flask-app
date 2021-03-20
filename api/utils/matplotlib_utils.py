import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
import time
import os
import os.path
from numpy.random import random as rng

def get_matplotlib_version():
    return matplotlib.__version__


def brownian_motion():
    steps = 50
    steps_x = rng(steps)
    steps_y = rng(steps)

    pace_x = np.ones_like(steps_x)
    idx = steps_x < 0.5
    pace_x[idx] = -1

    idy = steps_y < 0.5
    pace_y = np.ones_like(steps_y)
    pace_y[idy] = -1

    plt.plot(np.cumsum(pace_x), np.cumsum(pace_y))
    filename = str(time.time())+'.png'
    rel_path = "../public/generated/" + filename
    plt.savefig(rel_path)
    plt.close()
    return "generated/" + filename


def save_plot():
    x_points = np.array([random.randint(0, 100), 6])
    y_points = np.array([random.randint(0, 100), 250])
    plt.plot(x_points, y_points)
    filename = str(time.time())+'.png'
    rel_path = "../public/generated/" + filename
    plt.savefig(rel_path)
    plt.close()
    return "generated/" + filename


def clear_files():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    print(current_dir)
    generated_image_path = "../../public/generated/"
    for root, dirs, files in os.walk(generated_image_path):
        for file in files:
            os.remove(os.path.join(root, file))


if __name__ == "__main__":
    clear_files()

