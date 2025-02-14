class Config:
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/worktime_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG=False
 
class DevelopmentConfig(Config):
    SECRET_KEY = 'dev'
    DEBUG=True
    TESTING=True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/worktime_db'