# import basic library
import flask
import threading
import sys

from threading import Thread
from flask import Flask

#>------------SUMMARY----------------<
# This module is designed to modify code in real time.
# This is where the flask web library is used. With the help of a dynamic url,
# we can transfer the running time of the program. This helps a lot, for example,
# when you need to arrange widgets and restart the program, through the terminal
# or by pressing additional buttons, it only takes time. Here you just refresh
# the page in the browser and your program is restarted.
#
# Important! It is necessary that there are no changes in the program while it is running.
# You can make changes, however, if you want to save them, make sure that the program is not running.
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
    from Demo import play #Demo import play
    play()

    return "<h1>END UPDATE</h1>"

# user class to manage Thread
class RunThread(Thread):
    def __init__(self, time):
        super().__init__()
        self.time = int(time)

    def run(self):
        from Examples.progressbar import play #Demo import play
        play(self.time)

        del()

    def __del__(self):
        del self


if __name__=="__main__":
    app.run(debug=True)
