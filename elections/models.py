# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    area = models.CharField(max_length=15)
    party_number = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name