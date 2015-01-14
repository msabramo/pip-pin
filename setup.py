from setuptools import setup

if __name__ == '__main__':
  setup(
    name="pip-pin",
    version="0.0.1",
    author="Mark Steve Samson",
    author_email="hello@marksteve.com",
    license="MIT",
    url="https://github.com/marksteve/pip-pin",
    py_modules=['pip_pin'],
    entry_points=dict(
      console_scripts=[
        'pip_pin=pip_pin:__main__',
      ],
    ),
  )
