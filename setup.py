from distutils.core import setup
import subprocess


from setuptools.command.develop import develop
from setuptools.command.install import install


def install_asarjs():
    subprocess.call(["sudo", "npm", "install", "-g", "asar"])

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        install_asarjs()

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        install_asarjs()


setup(
    name='pylectron',
    version='0.0.1',
    author='Shashank Gopikrishna',
    author_email='shashank.gopikrishna@gmail.com',
    packages=['pylectron'],
    entry_points={ 'console_scripts': ['pylectron = pylectron.__main__:main' ] },
    description='python3 electron GUI',
    package_data={
        'pylectron': ['js_app/*'],
    },
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
)