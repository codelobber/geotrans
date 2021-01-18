from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField, BooleanField, IntField,
)

class Point(Document):
    meta = {'collection': 'point'}
    name = StringField()
    latitude = StringField()
    longitud = StringField()
    phone = StringField()
    due = DateTimeField(default=datetime.now)

class Config(Document):
    meta = {'collection': 'config'}
    version = IntField()
    allowedRadius = IntField()
    isDayPeriodAllowed = BooleanField()
