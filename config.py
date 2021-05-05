import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default sekret')
    JSON_AS_ASCII = False  # настройка нужна для представления русских букв в json
    DEBUG = os.environ.get('DEBUG', True)
    TESTING = os.environ.get('TESTING', True)
    server = os.environ.get('sqlserver', '')
    database = os.environ.get('sqldatabase', '')
    username = os.environ.get('sqlusername', '')
    password = os.environ.get('sqlpassword', '')
