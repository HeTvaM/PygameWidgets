# import basic library
import flask
import threading
import sys

from threading import Thread
from flask import Flask

#>------------SUMMARY----------------<

#>------------SUMMARY----------------<


app = Flask(__name__)

threads = []

# route which open demo.py
# and destroy it after <time>
@app.route("/time/<time>")
def index(time):
    print(f"TIME_TO_DESTROY:{time:>3}")
    thread = RunThread(time)
    thread.start()
    thread.join()

    return "<h1>RELOAD</h1>"

# route which open demo.py
@app.route("/update")
def update():
    from demo_grid import play #Demo import play
    play()

    return "<h1>END UPDATE</h1>"

# user class to manage Thread
class RunThread(Thread):
    def __init__(self, time):
        super().__init__()
        self.time = int(time)

    def run(self):
        from demo_grid import play #Demo import play
        play(self.time)

        del()

    def __del__(self):
        del self


if __name__=="__main__":
    app.run(debug=True)
