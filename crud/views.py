# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import Measure
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from mongoengine import *

# Create your views here.


def index(request):
    if request.method == 'POST':
        measure = Measure()
        measure.ch1 = request.POST['ch1']
        measure.ch2 = request.POST['ch2']
        measure.ch3 = request.POST['ch3']
        measure.ch4 = request.POST['ch4']
        measure.ch5 = request.POST['ch5']
        measure.ch6 = request.POST['ch6']
        measure.ch7 = request.POST['ch7']
        measure.ch8 = request.POST['ch8']
        measure.ch9 = request.POST['ch9']
        measure.ch10 = request.POST['ch10']
        measure.ch11 = request.POST['ch11']
        measure.ch12 = request.POST['ch12']
        measure.therm = request.POST['therm']
        measure.temp = request.POST['temp']
        measure.excv = request.POST['excv']
        measure.batt = request.POST['batt']
        measure.time = request.POST['time']
        measure.date = request.POST['date']
        measure.save()
    list = Measure.objects
    listOfMeasure = []
    for m in list:
        listOfMeasure.append(m)
    context = {
        'listOfMeasure': listOfMeasure,
    }
    return render(request, 'crud/index.html', context)


def edit(request, measure_id):
    listOfMeasure = Measure.objects
    context = {}
    for measure in listOfMeasure:
        if str(measure._id) == measure_id:
            context = {
                'measure': measure,
            }
    return render(request, 'crud/edit.html', context)


def savemeasure(request, measure_id):
    from pymongo import MongoClient
    from bson import ObjectId
    client = MongoClient('mongodb://127.0.0.1', 27017)
    db = client.crud
    col = db.measure
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'ch1': request.POST['ch1']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'ch2': request.POST['ch2']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'ch3': request.POST['ch3']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'ch4': request.POST['ch4']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'ch5': request.POST['ch5']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'ch6': request.POST['ch6']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'ch7': request.POST['ch7']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'ch8': request.POST['ch8']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'ch9': request.POST['ch9']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'ch10': request.POST['ch10']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'ch11': request.POST['ch11']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'ch12': request.POST['ch12']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'therm': request.POST['therm']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'temp': request.POST['temp']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'excv': request.POST['excv']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'batt': request.POST['batt']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'time': request.POST['time']}})
    col.update_one({"_id": ObjectId(str(measure_id))},
                   {'$set': {'date': request.POST['date']}})
    return HttpResponseRedirect(reverse('crud:index'))


def load(request):
    import os
    fh = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'crud\L4286F08.txt'), "r")
    fh.readline()
    p = fh.readline()
    while p != '':
        p = p.split('\t')
        p[-1] = p[-1].split('\n')[0]
        measure = Measure()
        measure.ch1 = p[0]
        measure.ch2 = p[1]
        measure.ch3 = p[2]
        measure.ch4 = p[3]
        measure.ch5 = p[4]
        measure.ch6 = p[5]
        measure.ch7 = p[6]
        measure.ch8 = p[7]
        measure.ch9 = p[8]
        measure.ch10 = p[9]
        measure.ch11 = p[10]
        measure.ch12 = p[11]
        measure.therm = p[12]
        measure.temp = p[13]
        measure.excv = p[14]
        measure.batt = p[15]
        measure.time = p[16]
        measure.date = p[17]
        measure.save()
        p = fh.readline()
    return HttpResponseRedirect(reverse('crud:index'))


def deletemeasure(request, measure_id):
    from pymongo import MongoClient
    from bson import ObjectId
    client = MongoClient('mongodb://127.0.0.1', 27017)
    db = client.crud
    col = db.measure
    col.delete_one({"_id": ObjectId(str(measure_id))})
    return HttpResponseRedirect(reverse('crud:index'))


def selectbydateandtime(request):
    listOfMeasure = []
    if request.method == 'POST':
        import datetime
        import time
        p = request.POST['date1'].split('/')
        date1 = datetime.date(int(p[2]), int(p[1]), int(p[0]))
        p = request.POST['time1'].split(':')
        time1 = datetime.time(int(p[0]), int(p[1]), int(p[2]))
        p = request.POST['date2'].split('/')
        date2 = datetime.date(int(p[2]), int(p[1]), int(p[0]))
        p = request.POST['time2'].split(':')
        time2 = datetime.time(int(p[0]), int(p[1]), int(p[2]))
        listOfMeasure3 = Measure.objects
        for measure in listOfMeasure3:
            p = str(measure.date).split('/')
            datecmp = datetime.date(int(p[2]), int(p[1]), int(p[0]))
            p = str(measure.time).split(':')
            timecmp = datetime.time(int(p[0]), int(p[1]), int(p[2]))
            if date1 <= datecmp <= date2:
                if time1 <= timecmp <= time2:
                    listOfMeasure.append(measure)
    context = {
        'listOfMeasure': listOfMeasure,
    }
    return render(request, 'crud/selectivedashboard.html', context)