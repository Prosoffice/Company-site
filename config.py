import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'prosper-dino-uche-focus-wisdom-pascal-collins'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    POST_PER_PAGE = 5
    UPLOAD_FOLDER = f'{basedir}/static/uploads/'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
