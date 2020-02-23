# pylectron
![Python 3.6](https://img.shields.io/badge/python-3.6+-blue.svg)

### Python interface to build electron apps


### Depends on [NodeJS](https://nodejs.org/en/download/)


## Installation

```sh
pip install -U git+https://github.com/shashfrankenstien/pylectron.git
```

## Usage
Create a new project

```sh
mkdir my_project
cd my_project
pylectron install
touch index.html
touch myapp.py
```

The following goes in `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Example</title>
</head>
<body>
    HELLO WORLD
</body>
</html>
```

The following goes in `myapp.py`
```py
from pylectron import Application
app = Application()
app.new_window(width=300, height=200, source_path="path/to/index.html")
app.wait()
```

Finally
```sh
python3 myapp.py
```