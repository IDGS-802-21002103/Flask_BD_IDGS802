from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_wtf.csrf import CSRFProtect

class Config:
    SECRET_KEY = 'CLAVE_SECRETA'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/idgs_802'

csrf = CSRFProtect()