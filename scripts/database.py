from mongoengine import connect

from models import Point
from models import Config

# You can connect to a real mongo server instance by your own.
connect('graphene-mongo-example', host='mongomock://localhost', alias='default')


def init_db():
    # Create the fixtures
    point = Point(name = 'John Smith', latitude = '0', longitud = '0.1', phone = '+79000000000')
    point.save()

    config = Config(version = 1, allowedRadius = 1000, isDayPeriodAllowed = True)
    config.save()