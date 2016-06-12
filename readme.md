## Fresh Tomatoes

This is a simple website showing a few games, shows, and movies that I like.

You can visit the site [here](https://abustamam.github.io/Fresh-Tomatoes/)

To build the site, please make sure that you have IMDBPy installed. 

The easiest way for me to do it without messing with the global system environment was to use a virtual environment.

## Installing virtualenv

To install virtualenv, run the following command:

```
pip install virtualenv
```

When it is finished installing, go into the project directory, then run:

```
virtualenv venv
```

This will create a `venv` directory.

Then, run:

```
source venv/bin/activate
```

This will put you into the virtual env.

## Install dependencies

```
pip install -r requirements.txt
```

This will allow you to run the build command:

```
python entertainment.py
```

Pull requests accepted! 