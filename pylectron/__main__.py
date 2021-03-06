import subprocess
import os, shutil
import sys
import platform
import json
import requests
from io import BytesIO
from zipfile import ZipFile, ZipInfo

from pylectron import config

ARCH_LOOKUP = {
    'x86_64': 'x64',
    'AMD64': 'x64'
}



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


def get_platform_prefix():
    system = sys.platform
    machine = ARCH_LOOKUP[platform.machine()]
    return "{}-{}".format(system, machine)

def uninstall():
    if os.path.isdir(config.ELECTRON_DIR): shutil.rmtree(config.ELECTRON_DIR)


def install():
    uninstall()
    url = "https://github.com/electron/electron/releases/download/v6.1.8/electron-v6.1.8-{}.zip".format(get_platform_prefix())
    print(url)
    res = requests.get(url)
    elec_bin = BytesIO(res.content)
    elec_zippy = ZipFileWithPermissions(elec_bin)
    elec_zippy.extractall(path=config.ELECTRON_DIR)
    for f in os.listdir(config.ELECTRON_DIR):
        print(f)
    build()


def build():
    with open(config.PACKAGE_JSON, "r") as pkg:
        pk_json = json.load(pkg)

    if "dependencies" in pk_json or "devDependencies" in pk_json:
        cur_path = os.getcwd()
        os.chdir(config.APPLICATION_DIR)
        subprocess.Popen(["npm", "install"], shell=True).wait()
        os.chdir(cur_path)
    print("building app.asar ..")
    subprocess.Popen(['asar', 'pack', config.APPLICATION_DIR, config.ELECTRON_ASAR_DEPLOY_PATH], shell=True).wait()
    print("copied app.asar to electron_build/resources")


def clean():
    if os.path.isdir(config.NODE_MODULES): shutil.rmtree(config.NODE_MODULES)
    if os.path.isfile(config.ELECTRON_ASAR_DEPLOY_PATH): os.remove(config.ELECTRON_ASAR_DEPLOY_PATH)



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