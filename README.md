# pip-pin

![Demo](demo.gif)

## Install

```bash
pip install pip-pin
# But you should pipsi
pipsi install pip-pin
```

## Usage

```bash
pip_pin <source> [files...]
```

- `source` - Package list you want to get pinned version from.  You would want
this to be the output of `pip freeze`. Use `-` for `stdin`.

- `files` - Requirement files you want to update with pinned versions.

## License

[MIT License](http://marksteve.mit-license.org)

