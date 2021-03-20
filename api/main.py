from api.utils.plotit import say_hello
from api.utils.plotit import get_random
import api.utils.matplotlib_utils as utils

print("Hello World")
print(say_hello())
print(get_random())
print(utils.get_matplotlib_version())
image_uri = utils.save_plot()
print(utils.brownian_motion())


