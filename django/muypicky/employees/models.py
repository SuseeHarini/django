# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class EmployeeModel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    dob = models.DateField()
    phone = models.IntegerField()
    emp_id = models.IntegerField()
