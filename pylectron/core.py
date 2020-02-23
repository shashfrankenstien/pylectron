import time
import subprocess
import os
import json
import signal

from pylectron import config

# import requests
# class Window(object):

#     def __init__(self, width, height, source_path):
#         self.width = width
#         self.height = height
#         self.source_path = source_path

#     def open(self):
#         return requests.get("http://localhost:3000/window/open", params={
#             "width": self.width,
#             "height": self.height,
#             "source_path": self.source_path,
#         }).text


import socket


class Communicator(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("127.0.0.1", 1234))

    def send(self, topic, msg):
        params = {"topic": topic, "msg": msg}
        self.sock.sendall(json.dumps(params).encode())




class Application(object):

    def __init__(self):
        self.proc = subprocess.Popen([os.path.join(config.ELECTRON_DIR, 'electron')])
        time.sleep(1)
        self.electron = Communicator()

    def new_window(self, width, height, source_path):
        params = {
            "width": width,
            "height": height,
            "source_path": source_path,
        }
        self.electron.send("new-window", params)

    def wait(self):
        self.proc.wait()

    def close(self):
        self.proc.send_signal(signal.SIGINT)

