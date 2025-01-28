# Mypy Exhaustive Check

This Mypy's plugin ensures exhaustive handling of enum members in dictionaries.
It helps developers catch missing enum members in dictionary keys, improving
code robustness and reducing runtime errors.

## Example

Here is an example of how to use the plugin:

```python
from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
```

Once a dict is definited that uses this enum, if not all the members are keys,
Mypy will raise an error:

```python
COLOR_TO_HEX: dict[Color, str] = {
    Color.RED: '#FF0000',
    Color.GREEN: '#00FF00',
}
```

Output:

```markdown
error: Keys within dictionary do not exhaustively handle all enum members. Unhandled members: BLUE  [dict-not-exhaustive]
```

## Usage

### Install

Install with pip as any other Python package:

```sh
pip install mypy-exhaustive-check
```

### Enable 

Add the package name to the `plugins` of your Mypy config.

For `mypy.ini`:

```ini
[mypy]
plugins = mypy_exhaustive_check
```

For `pyproject.toml`
```toml
[tool.mypy]
plugins = [
    "mypy_exhaustive_check",
]

```

### Run

Then, run Mypy as usual:

```sh
mypy your_code.py
```

## Pre-commit users

For pre-commit users, it can be used by addint the plugin as additional
dependency:

```yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: "v1.14.1"
    hooks:
      - id: mypy
        additional_dependencies:
          - "mypy-exhaustive-check"
```


## Contribute
Contributions are welcome! Please open an issue or submit a pull request.

### Prerequisite

This project relies on `pipenv`, to install it you can use `pip` or `pipx`
(preferred)

```sh
pipx install pipenv
```

or

```sh
pip install pipenv
```

### Setting Up

To install dependencies use:

```sh
pipenv install --dev
```

### Running Tests

To run the tests, use:

```sh
pipenv run test
```

### Linting and Formatting

To check linting and formatting, use:

```sh
pipenv run format
```

