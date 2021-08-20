import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    IMDB_KEY = os.environ.get('IMDB_KEY')
    OMDB_KEY = os.environ.get('OMDB_KEY')