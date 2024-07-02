from enviroment import env
from config import app_config
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

settings = app_config[env]
Session = sessionmaker()
db = SQLAlchemy()