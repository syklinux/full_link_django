# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from django.shortcuts import render
from django.views.generic.base import TemplateView,View
from django.shortcuts import render, render_to_response,HttpResponseRedirect,HttpResponse
from django.db.models import Q
from .models import History,api,service
from utils.data_count import conn
from utils.data_count_v2 import connv2

# Create your views here.


class Index(View):
    def get(self,request):
        api_count = api.objects.all().count()
        history_all = History.objects.all().order_by("-time")[:api_count]
        service_all = service.objects.all()
        a = []
        all = {}
        for j in history_all:
            a.append(j)
        for i in service_all:
            b = {}
            for k in i.api_set.all():
                for y in k.history_set.all():
                    if y in a:
                        c = {}
                        c["qps"] = y.qps
                        c["rt"] = y.rt
                        b[y.api.name] = c
                all[i.name] = b
                all["all"] = y.all
        data = conn(all)
        return render(request,'canvas.html',locals())


class IndexV2(View):
    def get(self,request):
        api_count = api.objects.all().count()
        history_all = History.objects.all().order_by("-time")[:api_count]
        service_all = service.objects.all()
        a = []
        all = {}
        for j in history_all:
            a.append(j)
        for i in service_all:
            b = {}
            for k in i.api_set.all():
                for y in k.history_set.all():
                    if y in a:
                        c  = str(y.qps)
                        d = str(y.rt)
                        g = c + "," + "  "+ d + "\n"
                        b[y.api.name] = g
                all[i.name] = b
                all["all"] = y.all
        data = connv2(all)
        return render(request,'test.html',locals())