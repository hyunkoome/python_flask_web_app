# python_flask_web_app



## conda env
```
$ conda create -n flask python==3.10
```

## run Flask (if not installed python-dotenv)
```
$ cd apps/minimalapp
$ export FLASK_APP=app.py
$ export FLASK_DEBUG=1
$ flask run
```

## run Flask (if installed python-dotenv)
```
$ cd apps/minimalapp
$ flask run
```

### Carefully !!
- if not have .env: app root == dir on the 'flask run'
- if have .env:     app root == dir with 'env' file

