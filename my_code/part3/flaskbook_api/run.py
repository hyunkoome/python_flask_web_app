# 앱을 구동하는 코드
# 보통, config를 읽어들이고 create_app 함수 호출은 여기에서.

import os

from flask import Flask

from flaskbook_api.api import api
from flaskbook_api.api.config import config

config_name = os.environ.get("CONFIG", "local")

app = Flask(__name__)
app.config.from_object(config[config_name])

# blueprint를 애플리케이션에 등록
app.register_blueprint(api)
