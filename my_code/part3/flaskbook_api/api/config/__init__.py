# 환경별로 준비한 config 를 읽어 들이는 코드

from flask import Flask, jsonify, request
from . import base, local
# from flaskbook_api.api.config import base, local

config = {
    "base": base.Config,
    "local": local.LocalConfig,
}
