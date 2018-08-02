# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
