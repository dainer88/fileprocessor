# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import Measure
from django.template import loader
from django.shortcuts import render
from django.urls import reverse

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


def save(request, measure_id):
    return


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