# -*- coding: utf-8 -*-
# from elasticsearch import Elasticsearch
#from es_client import es_client
import time,datetime
import requests
import json
import sys
import os

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(project_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "full_link.settings")

import django
django.setup()


from full_test.models import service,api,History
from utils import es

def _import_history(qps,rt,api,all):
    history = History()
    history.qps = qps
    history.rt = rt
    history.all = all
    history.api = api
    history.save()
    return history


def get_es_qps(k):
    data = "api: {} AND host:bbs.mobileapi.hupu.com".format(k)
    a = es.post_qps(data)
    return a

def get_es_all():
    data = "*"
    a = es.post_qps(data)
    return a

def get_api():
    connent = api.objects.all()
    d = get_es_all()
    for i in connent:
         a = get_es_qps(i)
         c = api.objects.get(name=i)
         b = get_es_rt(i)
         history_obj = _import_history(a, b, c,d)


def get_es_rt(k):
    data = "api:{} AND host:bbs.mobileapi.hupu.com AND NOT hostname:zhaomin-lb-gray* AND NOT code:408".format(k)
    a = es.post_rt(data)
    return a


get_api()