import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
import time
import os, re, os.path


image_folder = "../public/generated/"


def get_matplotlib_version():
    return matplotlib.__version__


def save_plot():
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])
    plt.plot(xpoints, ypoints)
    random.randint(100)
    ticks = time.time()
    image_path = image_folder+str(ticks)+'.png'
    plt.savefig(image_path)
    plt.close()


def clear_files():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    print(current_dir)
    generated_image_path = "../../public/generated/"
    for root, dirs, files in os.walk(generated_image_path):
        for file in files:
            os.remove(os.path.join(root, file))


if __name__ == "__main__":
    clear_files()

