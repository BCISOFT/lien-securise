import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    LINK_BASE_URL = "DBLINK"
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRETKEY'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://DBUSER:DBPASS@localhost:3306/DBNAME'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


