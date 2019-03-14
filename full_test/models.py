# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class service(models.Model):
    name = models.CharField("应用名",max_length=255)
    remark = models.CharField("备注说明", max_length=255, null=True, blank=True, help_text="备注说明")

    class Meta:
        verbose_name = "应用"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class api(models.Model):
    name = models.CharField("api接口名",max_length=255)
    service = models.ForeignKey(service,u"所属应用",)
    remark = models.CharField("备注说明", max_length=255, null=True, blank=True, help_text="备注说明")

    class Meta:
        verbose_name = "api接口"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class History(models.Model):
    qps = models.IntegerField("qps值")
    rt = models.FloatField("rt值")
    api = models.ForeignKey(api,u"所属接口")
    all = models.IntegerField("全站qps",default=1222)
    time = models.DateTimeField('时间', auto_now_add=True)

    class Meta:
        verbose_name = "历史数据"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.qps
