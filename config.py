
class Config:

	SQLALCHEMY_TRACK_MODIFICATIONS=False
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://anum:cockar567@localhost/football'


class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig,"testing":TestConfig}
