from flask import Flask 
from celery import Celery

from flask_mongoengine import MongoEngine
import config 


app = Flask(__name__)
app.config.from_object('config')

celery = Celery(app.name, broker=config.CELERY_BROKER_URL)
celery.conf.update(app.config)

db = MongoEngine(app)

from app import views