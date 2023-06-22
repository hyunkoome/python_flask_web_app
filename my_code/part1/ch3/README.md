# python_flask_web_app

## conda env
```
$ conda create -n flask python==3.10
$ conda activate flask
$ cd mycode/part1/ch3
$ pip install -r requirements.txt
```

## run Flask (if installed python-dotenv)
```
$ cd mycode/part1/ch3
$ flask run
```

### Carefully !!
- if have .env:     app root == dir with 'env' file

## database init and migration

### database init
```commandline
$ cd mycode/part1/ch3
$ flask db init
```
### migration: 데이터베이스의 마이그레이션 파일을 생성 
```commandline
$ cd mycode/part1/ch3
$ flask db migrate
```

### migration update: 마이그레이션 정보를 실제로 데이터베이스에 반영 (ex, table 생성 등)
```commandline
$ cd mycode/part1/ch3
$ flask db upgrade
```

### migration downgrade: 마이그레이트한 데이터베이스를 적용하기 전의 상태로 되돌림
```commandline
$ cd mycode/part1/ch3
$ flask db downgrade
```

