class Config(object):
    SECRET_KEY = 'f0faa2bed03b28e48544762d760aa169'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    HOST = "0.0.0.0"
    PORT = "5051"
    BASE_URL = HOST + ':' + PORT
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:secret@ventura2_database:3306/ventura"
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:secret@64.227.98.133:6111/ventura"
    REDIS_URL = "redis://127.0.0.1:7111/0"
    SQLALCHEMY_POOL_RECYCLE = 300
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SERVICES_NOT_VERIFYABLE = {
        'welcome'
    }
    SQLALCHEMY_BINDS = {
        'master': SQLALCHEMY_DATABASE_URI,
        'ventura2': "mysql+pymysql://root:secret@ventura2_db:3306/ventura",
        'ventura3': "mysql+pymysql://root:secret@ventura3_db:3306/ventura",
    }

    PATH_UPLOAD = {
        "ventura2": "/upload/ventura2/",
        "ventura2-sueldos": "/upload/ventura2/afiliados/sueldos"
    }

class TestingConfig(Config):
    """
    Development configurations
    """
    HOST = "0.0.0.0"
    PORT = "5051"
    BASE_URL = HOST + ':' + PORT
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:secret@ventura2_database:3306/ventura"
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:secret@64.227.98.133:6111/ventura"
    SQLALCHEMY_POOL_RECYCLE = 300
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVICES_NOT_VERIFYABLE = {
        'welcome'
    }
    SQLALCHEMY_BINDS = {
        'master': SQLALCHEMY_DATABASE_URI,
        'ventura2': "mysql+pymysql://root:secret@ventura2_db:3306/ventura",
        'ventura3': "mysql+pymysql://root:secret@ventura3_db:3306/ventura",
    }



class ProductionConfig(Config):
    """
    Development configurations
    """
    HOST = "0.0.0.0"
    PORT = "5051"
    BASE_URL = HOST + ':' + PORT
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:secret@ventura2_database:3306/ventura"
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:secret@64.227.98.133:6111/ventura"
    SQLALCHEMY_POOL_RECYCLE = 300
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVICES_NOT_VERIFYABLE = {
        'welcome'
    }
    SQLALCHEMY_BINDS = {
        'master': SQLALCHEMY_DATABASE_URI,
        'ventura2': "mysql+pymysql://root:secret@ventura2_db:3306/ventura",
        'ventura3': "mysql+pymysql://root:secret@ventura3_db:3306/ventura",
    }


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
