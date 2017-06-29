from __future__ import unicode_literals
from ..login.models import User
from django.contrib import messages
from django.db import models
from datetime import date, datetime
from dateutil.parser import parse as parse_date

class TravelManager(models.Manager):
    def ValidTravelPlanned(self, user_info, request):
        passFlag = True
        return passFlag

class Travel(models.Model):
    destination = models.TextField(max_length=100)
    description = models.TextField(max_length=150)
    travel_date_from = models.DateField()
    travel_date_to = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    travelplanner_id = models.ForeignKey(User, related_name="travelplanner")
    travelmaker_id = models.ManyToManyField(User, related_name="travelmaker")
    travelManager = TravelManager()
    objects = models.Manager()
