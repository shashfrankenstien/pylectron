import subprocess
import os, shutil
import sys
import json

import requests
from io import BytesIO
from zipfile import ZipFile, ZipInfo

from pylectron import config


class ZipFileWithPermissions(ZipFile):
    """ Custom ZipFile class handling file permissions. """
    def _extract_member(self, member, targetpath, pwd):
        if not isinstance(member, ZipInfo):
            member = self.getinfo(member)

        targetpath = super()._extract_member(member, targetpath, pwd)

        attr = member.external_attr >> 16
        if attr != 0:
            os.chmod(targetpath, attr)
        return targetpath

def uninstall():
    if os.path.isdir(config.ELECTRON_DIR): shutil.rmtree(config.ELECTRON_DIR)


def install():
    uninstall()
    res = requests.get("https://github.com/electron/electron/releases/download/v6.1.8/electron-v6.1.8-linux-x64.zip")
    elec_bin = BytesIO(res.content)
    elec_zippy = ZipFileWithPermissions(elec_bin)
    elec_zippy.extractall(path=config.ELECTRON_DIR)
    for f in os.listdir(config.ELECTRON_DIR):
        print(f)


def build():
    with open(config.PACKAGE_JSON, "r") as pkg:
        pk_json = json.load(pkg)

    if "dependencies" in pk_json or "devDependencies" in pk_json:
        cur_path = os.getcwd()
        os.chdir(config.APPLICATION_DIR)
        subprocess.Popen(["npm", "install"]).wait()
        os.chdir(cur_path)
    subprocess.Popen(['asar', 'pack', config.APPLICATION_DIR, config.ELECTRON_ASAR_DEPLOY_PATH]).wait()


def clean():
    if os.path.isdir(config.NODE_MODULES): shutil.rmtree(config.NODE_MODULES)
    if os.path.isfile(config.ELECTRON_ASAR_DEPLOY_PATH): os.remove(config.ELECTRON_ASAR_DEPLOY_PATH)


# def test():
#     proc = subprocess.Popen([os.path.join(ELECTRON_DIR, 'electron')])
#     time.sleep(1)
#     print(requests.get("http://localhost:3000/window/open").text)
#     proc.wait()


def main():
    if len(sys.argv)<=1:
        raise Exception("No argument")
    else:
        if sys.argv[1].strip() in globals():
            res = globals()[sys.argv[1].strip()]()
            if res is not None:
                raise Exception(str(res))
        else:
            raise Exception("Invalid argument")


if __name__ == "__main__":
    main()