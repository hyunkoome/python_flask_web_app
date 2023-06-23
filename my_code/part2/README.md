## 패키지 설치

```
$ conda create -n flask_det_app python==3.10.9
$ conda activate flask_det_app
$ cd my_code/part2
(flask_det_app) $ pip install -r requirements.txt
```

# install pytorch and opencv
```commandline
(flask_det_app) $ pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
(flask_det_app) $ pip install opencv-python==4.7.0.72
```

## DB 마이그레이트

```
(flask_det_app) $ flask db init
(flask_det_app) $ flask db migrate
(flask_det_app) $ flask db upgrade
```

## 학습 모델 취득

```
(flask_det_app) $ python
>>> import torch
>>> import torchvision
>>> model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
>>> torch.save(model, "model.pt")
```

`model.pt`를 `apps/detector`로 이동

## 앱 실행

```
(flask_det_app) $ flask run
```

## 테스트 실행

```
$ pytest tests/detector
```

