# python_flask_web_app

## conda env
```
$ conda create -n flask python==3.10
$ conda activate flask
$ cd mycode/part1/ch2
$ pip install -r requirements.txt
```

## run Flask (if installed python-dotenv)
```
$ cd mycode/part1/ch2
$ flask run
```

### Carefully !!
- if have .env:     app root == dir with 'env' file

## database init and migration

### database init
```commandline
$ cd mycode/part1/ch2
$ flask db init
$ flask db init -d apps/migrations
```
### migration: 데이터베이스의 마이그레이션 파일을 생성 
```commandline
$ cd mycode/part1/ch2
$ flask db migrate
$ flask db migrate -d apps/migrations
```

### migration update: 마이그레이션 정보를 실제로 데이터베이스에 반영 (ex, table 생성 등)
```commandline
$ cd mycode/part1/ch2
$ flask db upgrade
$ flask db upgrade -d apps/migrations
```

### migration downgrade: 마이그레이트한 데이터베이스를 적용하기 전의 상태로 되돌림
```commandline
$ cd mycode/part1/ch2
$ flask db downgrade
$ flask db downgrade -d apps/migrations
```

