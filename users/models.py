from __future__ import unicode_literals
from django.db import models

# Create your models here.


class User(models.Model):
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.user_email

