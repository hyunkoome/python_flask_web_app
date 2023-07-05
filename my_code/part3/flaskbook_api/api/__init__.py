# 앱을 초기화해서 읽어들이는 코드
# 보통, 플라스트 앱을 작성하는 create_app 함수는 여기에서 작성

from flask import Blueprint, jsonify, request
from flaskbook_api.api import calculation

api = Blueprint("api", __name__)

# API 를 로컬 서버에서 작동해서 API에 대해서 HTTP 통신으로 요청을 보내고, 응답이 돌아올때까지 구현
# 즉, 라우팅 구현, 라우팅이랑 URL과 처리를 대응시키는 것으로,
# 플라스크의 라우팅은 URL과 실행하는 함수를 연결하는 것
@api.get("/")
def index():
    return jsonify({"column": "value"}), 201


@api.post("/detect")
def detection():
    return calculation.detection(request)
