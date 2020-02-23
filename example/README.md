# pylectron example

## Development Installation

```sh
git clone https://github.com/shashfrankenstien/pylectron.git
cd pylectron
python3 -m pip install -e .
```

## Basic Usage

```sh
cd example
pylectron install
python3 example.py
```


## Package with PyInstaller
Note the two includes in `example.spec` for configuration

```py
exe = EXE(pyz,
          ...,
          Tree("electron_build", prefix="electron_build"),
          Tree("static", prefix="static"),
          ...)
```

```sh
cd example
pylectron install
python3 -m PyInstaller example.spec
cd dist
./example
```