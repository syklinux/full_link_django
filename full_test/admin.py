# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

admin.site.register(service)
admin.site.register(api)
admin.site.register(History)