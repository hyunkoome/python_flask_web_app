# 로컬 환경에서만 사용되는 설정

from flaskbook_api.api.config.base import Config


class LocalConfig(Config):
    TESTING = True
    DEBUG = True
