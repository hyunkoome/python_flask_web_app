## 패키지 설치

```commandline
$ conda create -n flask_det_app python==3.10.9
$ conda activate flask_det_app
$ cd my_code/part2
(flask_det_app) $ pip install -r requirements.txt
```

## DB 마이그레이트

```commandline
(flask_det_app) $ flask db init
(flask_det_app) $ flask db migrate
(flask_det_app) $ flask db upgrade
```

## 앱 실행

```commandline
(flask_det_app) $ flask run
```

# install pytorch and opencv

```commandline
(flask_det_app) $ pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
(flask_det_app) $ pip install opencv-python==4.7.0.72
```

## 학습 모델 취득

```commandline
(flask_det_app) $ cd my_code/part2/apps/detector/dets_models
(flask_det_app) $ python get_models.py
```


## Unit 테스트 실행

```commandline
(flask_det_app) $ pip install pytest==7.4.0
```

```commandline
$ cd my_code/part2/tests
$ pytest
```

## 커버리지 테스트 실행: 테스트 코드가 얼마나 실행되었는지 비율로 나타냄

```commandline
(flask_det_app) $ pip install pytest-cov==4.1.0
```

```commandline
$ cd my_code/part2/tests
$ pytest detector --cov=../apps/detector
```

## 테스트의 커버리지를 HTML로 출력

```commandline
$ cd my_code/part2/tests
$ pytest detector --cov=../apps/detector --cov-report=html
```
