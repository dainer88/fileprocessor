# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from mongoengine import *
from djangoMongoDB.settings import MONGO_DATABASE_NAME, MONGO_HOST, MONGO_PORT

connect(MONGO_DATABASE_NAME, host=MONGO_HOST, port=MONGO_PORT)

# Create your models here.


class Measure(Document):
    _id = StringField()
    ch1 = StringField(required=True)
    ch2 = StringField(required=True)
    ch3 = StringField(required=True)
    ch4 = StringField(required=True)
    ch5 = StringField(required=True)
    ch6 = StringField(required=True)
    ch7 = StringField(required=True)
    ch8 = StringField(required=True)
    ch9 = StringField(required=True)
    ch10 = StringField(required=True)
    ch11 = StringField(required=True)
    ch12 = StringField(required=True)
    therm = StringField(required=True)
    temp = StringField(required=True)
    excv = StringField(required=True)
    batt = StringField(required=True)
    time = StringField(required=True)
    date = StringField(required=True)

    def get_id(self):
        return str(self._id)