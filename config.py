import os


class Config:
    '''
    General configuration parent class
    '''

    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://anum:cockar567@localhost/football'



    LIVESCORE_API_KEY = os.environ.get('LIVESCORE_API_KEY')
    LIVESCORE_API_SECRET = os.environ.get('LIVESCORE_API_SECRET')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:database@localhost/fantasy'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

