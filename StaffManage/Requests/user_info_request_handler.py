#!/usr/bin/python
# -*- coding: utf-8 -*-

from StaffManage.Requests.BaseRequestHandler import BaseRequestHandler
from DjangoWebDemo.settings import DATABASES
from StaffManage.models import UserInfo,make_uuid_without_hypen

from django.core.cache import cache

import traceback
import json

__author__ = '9'

class UserInfoRequestHandler(BaseRequestHandler):
    def __init__(self, params, request):
        BaseRequestHandler.__init__(self, params, request)

    def prepare_update_params(self):
        self.USER_INFO_LIST = self.params.get(u'USER_INFO_LIST')

    def prepare_add_params(self):
        self.ID = make_uuid_without_hypen();
        self.NAME = self.params.get(u'NAME')
        self.SEX = self.params.get(u'SEX')
        self.TYPE = self.params.get(u'TYPE')

    def prepare_delete_params(self):
        self.ID = self.params.get(u'ID')

    def get_user_info_list(self):
        user_info_list = UserInfo.objects.using(DATABASES[u'django'][u'NAME'])
        return user_info_list

    def get_data(self):
        return self.get_user_info_list()

    def load_data(self, model_data_list):
        user_info_list = model_data_list
        data = []
        for user_info in user_info_list:
            each_data = {
                u'ID': user_info.id,
                u'NAME': user_info.name,
                u'SEX': user_info.sex,
                u'TYPE': user_info.type,
                }
            data.append(each_data)
        return data

    def update_data(self):
        info_list = self.USER_INFO_LIST.split(u',')
        for info in info_list:
            print(info)
            user_id, name, sex, type = info.split(u'&')
            user_info = UserInfo.objects.using(DATABASES[u'django'][u'NAME']).get(id=user_id)
            user_info.name = name
            user_info.sex = sex
            user_info.type = type
            user_info.save(using=DATABASES[u'django'][u'NAME'], force_update=True)

    def add_data(self):
        user_info = UserInfo()
        user_info.id = self.ID
        user_info.name = self.NAME
        user_info.sex = self.SEX
        user_info.type = self.TYPE
        user_info.save(using=self.django)

    def delete_data(self):
        assert(self.ID is not None)
        UserInfo.objects.using(self.django).get(id=self.ID).delete()

    def get_update_response(self):
        return self.operate_response(process_data=self.update_data)

    def get_add_response(self):
        return self.operate_response(process_data=self.add_data)

    def get_delete_response(self):
        return self.operate_response(process_data=self.delete_data)



