from pylectron.core import Application
import os
import time


if __name__ == "__main__":

    app = Application()

    app.new_window(500, 300, os.path.join(os.getcwd(), "example.html"))

    # win = Window(200, 200, None)
    # win.open()
    time.sleep(10)
    app.close()