#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enviroment import env
from flask import Flask, render_template, request
from flask_cors import CORS
from flask_restful import Api
from config import app_config
from db import db
from werkzeug.utils import secure_filename

import datetime, os

#Inicializacion de flask
app = Flask(__name__, 
static_url_path='/static',
static_folder='static',
template_folder='templates')

#habilitacion de CORS
CORS(app)

#Inicializacion de configuraciónes
app.config.from_object(app_config[env])

#Inicializacion de datos de BD
db.init_app(app)

#Inicializacion de servicios api
api = Api(app)
# inicializar rutas entidades

#initialize_routes(api)

@app.route('/')
def index():
    context = {}
    context['segment'] = 'index'
    return render_template('index.html', **context, utc_dt=datetime.datetime.utcnow())
    #return "OK", 200

#Se carga host 
if __name__ == '__main__':
    app.run(host=app_config[env].HOST,port=app_config[env].PORT)
