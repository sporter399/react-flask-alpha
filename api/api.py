import time
from flask import Flask

app = Flask(__name__)

@app.route('/test')
def get_test():
    testvariables = 28
    return {'testvar': testvariables}



@app.route('/time')
def get_current_time():
    return {'time': time.time()}