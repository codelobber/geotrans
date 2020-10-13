from mongoengine import connect

from models import Point

# You can connect to a real mongo server instance by your own.
connect('graphene-mongo-example', host='mongomock://localhost', alias='default')


def init_db():
    # Create the fixtures
    point = Point(name = 'John Smith', latitude = '0', longitud = '0.1', phone = '+79000000000')
    point.save()

    point2 = Point(name = 'Anna Mark', latitude = '0', longitud = '0.1', phone = '+79000000000')
    point2.save()

    point3 = Point(name = 'Sammy Siin', latitude = '0', longitud = '0.1', phone = '+79000000000')
    point3.save()

    point4 = Point(name = 'Nicolas', latitude = '0', longitud = '0.1', phone = '+79000000000')
    point4.save()