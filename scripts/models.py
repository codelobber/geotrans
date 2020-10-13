from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField,
)

class Point(Document):
    meta = {'collection': 'point'}
    name = StringField()
    latitude = StringField()
    longitud = StringField()
    phone = StringField()
    due = DateTimeField(default=datetime.now)
