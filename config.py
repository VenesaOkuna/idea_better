import os

class Config:

    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql://jhvcnzcpvoocug:abc2c996078b95f24f04e1952056dd35bdc3d10ed8884f78e7a42bcc8f0bd0b7@ec2-34-201-248-246.compute-1.amazonaws.com:5432/dfr1v18luggcvg'
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
    SQLALCHEMY_DATABASE_URI='postgresql://jhvcnzcpvoocug:abc2c996078b95f24f04e1952056dd35bdc3d10ed8884f78e7a42bcc8f0bd0b7@ec2-34-201-248-246.compute-1.amazonaws.com:5432/dfr1v18luggcvg'
    
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}