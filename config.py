import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_WEB_URL='https://newsapi.org/v2/sources?/category={}&apiKey={}'
    ARTICLES_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY='af516b5c8dc64f7e8c4384aa0ccd69c8'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    pass

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
