import os

class Config:

    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://venesa:1234@localhost/pitch'
    SECRET_KEY = 'powerfulsecretkey'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True



class ProdConfig(Config):
    '''
    Pruduction configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://venesa:1234@localhost/pitch'

class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://venesa:1234@localhost/pitch'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}