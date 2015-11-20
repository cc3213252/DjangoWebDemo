# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

import uuid
from django.db import models

def make_uuid_without_hypen():
    new_uuid = uuid.uuid4()
    return str(new_uuid).replace(u'-', u'')

class UserInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True)
    sex = models.CharField(max_length=10, blank=True)
    type = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    # class Meta:
    #     managed = False
    #     db_table = 'user_info'
