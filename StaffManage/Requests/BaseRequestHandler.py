# -*- coding: utf-8 -*-

import traceback
import json
import math
import hashlib
import warnings
from django.http import HttpResponseForbidden
from django.http import HttpResponseBadRequest
from django.http import HttpResponseNotFound
from django.http import HttpResponseServerError
from django.http import HttpResponse, Http404
from DjangoWebDemo.settings import DATABASES,DEBUG

__author__ = 'yudan.chen'


class BaseRequestHandler:
    """
    The base class to deal with common operations on updating models
    """
    def __init__(self, params, request):
        self.params = params
        self.request = request
        self.django = DATABASES[u'django'][u'NAME']
        self.test = DATABASES[u'default'][u'NAME']
        self.failed_description = u'服务器暂时未能响应,请稍候再试'

    def prepare_update_params(self):
        self.t_user_id = self.params.get(u'userId')
        self.t_password_md5 = self.params.get(u'password_md5')


    def prepare_get_params(self):
        self.t_user_id = self.params.get(u'userId')
        self.t_password_md5 = self.params.get(u'password_md5')

    def pre_verify(self):
        pass

    def get_data(self):
        return []

    def load_data(self, model_data_list):
        return []

    def operate_failed_response(self, failed_reason):
        response_data = {u'req_path': self.request.META.get(u'PATH_INFO'),
                         u'req_result': False,
                         u'failed_reason': failed_reason}
        if DEBUG:
            print response_data
        return HttpResponse(json.dumps(response_data), content_type=u'application/json')

    def operate_response(self, process_data):
        warnings.filterwarnings("error")
        response_data = {u'req_path': self.request.META.get(u'PATH_INFO'),
                         u'req_result': True}
        try:
            if process_data is not None:
                process_data()
        except Exception, e:
            response_data[u'req_result'] = False
            response_data[u'failed_description'] = self.failed_description
            traceback.print_exc()

        if DEBUG:
            print response_data
       # return response_data
        return HttpResponse(json.dumps(response_data), content_type=u'application/json')

    def get_response(self, process_data=None, load_data=None):
        print "************************* ",self.request.META.get(u'PATH_INFO')
        response_data = {u'req_path': self.request.META.get(u'PATH_INFO'),
                         u'req_result': False}
        try:
            model_data_list = self.get_data() if process_data is None else process_data()
            total_records = len(model_data_list)
            if total_records >= 0:
                response_data[u'total_records'] = str(total_records)
                response_data[u'data'] = self.load_data(model_data_list) if load_data is None else load_data(model_data_list)
                response_data[u'req_result'] = True
        except Exception, e:
            traceback.print_exc()

        if DEBUG:
            print response_data
        return response_data
     #   return HttpResponse(json.dumps(response_data), content_type=u'application/json')
