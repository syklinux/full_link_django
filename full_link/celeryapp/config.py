# !/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import

CELERY_RESULT_BACKEND = 'redis://192.168.50.128:6379/5'
BROKER_URL = 'redis://192.168.50.128:6379/6'