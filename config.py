import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TOGETHER_API_URL = os.environ.get('TOGETHER_API_URL', 'https://api.together.xyz/v1/chat/completions')
    TOGETHER_API_KEY = os.environ.get('TOGETHER_API_KEY', 'tgp_v1_grY6OqmY3fSH-exKP6W5K3-pUGqUVZVmT4-UjLHvfiQ')
    TOGETHER_MODEL = os.environ.get('TOGETHER_MODEL', 'deepseek-ai/deepseek-v3')
