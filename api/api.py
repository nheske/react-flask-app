import time
from flask import Flask

app= Flask(__name__)

@app.route('/time')
def get_current_time():
    # return {'time': "hello"}
    ticks = time.time()
    print("Number of ticks since 12:00am, January 1, 1970:", ticks)
    return {'time': time.time()}

print(get_current_time())