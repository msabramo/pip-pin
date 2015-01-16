import sys

from pip.operations.freeze import freeze


def __main__():
  for _file in sys.argv[1:]:
    contents = ""
    for line in freeze(requirement=_file):
      if line.startswith("#"):
        break
      contents += line + "\n"
    with open(_file, "wb") as f:
      f.write(contents)


if __name__ == "__main__":
  __main__()
