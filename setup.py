from distutils.core import setup

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
)