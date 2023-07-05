## Create Python Env and Install Pytorch

```commandline
$ conda create -n flask_api python==3.10.9
$ conda activate flask_api
$ cd my_code/part3/
(flask_api) $ pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### python requirements.txt 저장시
```commandline
(flask_api) $ pip freeze > requirements.txt
```

## Get Object Detection Models

```commandline
(flask_api) $ cd my_code/part3/
(flask_api) $ python get_models.py
```

## Run API App 
 
```commandline
(flask_api) $ cd my_code/part3/flaskbook_api
```

- `python-dotenv` 설치 되어있으면, `.env` 동작함
- 그러나, `python-dotenv` 설치 `안`했으면, 환경 변수들 세팅 해야 함 
    ```commandline
    (flask_api) $ source set_flask_run_env.sh
    ```
- flask 실행 
```commandline
(flask_api) $ flask run
```

## Detection 동작 확인하기

```commandline
(flask_api) $ curl -X POST http://127.0.0.1:5000/detect -H "Content-Type:application/json" -d '{"filename":"dog.jpg"}'
```

- 이때, `추론할 이미지`는 `flaskbook_api/data/original/` 에 위치 해야 하며
- `추론된 결과 이미지`는 `flaskbook_api/data/output/` 에 저장됨 
- 특히, `모델`은 `flaskbook_api/model.pt` 에 위치해야 함

