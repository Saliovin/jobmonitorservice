db_url = 'postgres://postgres:father@127.0.0.1:5432/jobmonitorservice'
class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = db_url

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = db_url

app_config = {
    'development': Development,
    'production': Production,
}