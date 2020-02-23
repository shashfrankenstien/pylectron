import os, sys
WORKING_DIR = path = getattr(sys, '_MEIPASS', os.getcwd())

APPLICATION_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "js_app")
NODE_MODULES = os.path.join(APPLICATION_DIR, "node_modules")
PACKAGE_JSON = os.path.join(APPLICATION_DIR, "package.json")

ELECTRON_DIR = os.path.join(WORKING_DIR, "electron_build")
ELECTRON_ASAR_DEPLOY_PATH = os.path.join(ELECTRON_DIR, "resources", "app.asar")