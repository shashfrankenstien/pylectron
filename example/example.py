from pylectron.core import Application
import os, sys
import time

WORKING_DIR = getattr(sys, '_MEIPASS', os.getcwd()) # Check first for PyInstaller temp directory

if __name__ == "__main__":

    app = Application()

    app.new_window(500, 300, os.path.join(WORKING_DIR, "static", "example.html"))

    app.wait()