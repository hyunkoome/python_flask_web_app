## Create Python Env and Install Pytorch

```commandline
$ conda create -n flask_api python==3.10.9
$ conda activate flask_api
$ cd my_code/part3/
(flask_api) $ pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## Get Object Detection Models

```commandline
(flask_api) $ cd my_code/part3/
(flask_api) $ python get_models.py
```
