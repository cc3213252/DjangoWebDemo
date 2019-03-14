from django.shortcuts import render
import datetime
from StaffManage import models
import traceback
import warnings
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from django.http import HttpResponse
from StaffManage.models import UserInfo,make_uuid_without_hypen
from DjangoWebDemo.settings import DATABASES

def index(request):
    try:
        result = models.UserInfo.objects.all()
    except:
        traceback.print_exc()
        raise Http404

    return render(request, 'StaffManage/index.html', {
        'result': json.dumps(obj_to_dict(result)),
    })

@csrf_exempt
def get_user_info_list(request):
    try:
        user_name = request.POST.get('NAME')
        user_sex = request.POST.get('SEX')
        user_type = request.POST.get('TYPE')
        result = models.UserInfo.objects.filter(name__contains=user_name, sex__contains=user_sex, type__contains=user_type)

        return HttpResponse(json.dumps(obj_to_dict(result)), content_type='application/json')
        # return render(request, 'StaffManage/index.html', {
        #     'result': json.dumps(obj_to_dict(result)),
        # })
    except:
            traceback.print_exc()
            raise Http404

@csrf_exempt
def add_user_info_list(request):
    try:
        user_name = request.POST.get('NAME')
        user_sex = request.POST.get('SEX')
        user_type = request.POST.get('TYPE')

        new_user= models.UserInfo(id=make_uuid_without_hypen(),name=user_name, sex=user_sex, type=user_type)
        new_user.save()
        print(json.dumps(model_to_dict(new_user)))
        return HttpResponse(json.dumps(model_to_dict(new_user)), content_type='application/json')

    except:
        traceback.print_exc()
        raise Http404

def obj_to_dict(obj_list):
    result = []
    for obj in obj_list:
        result.append(model_to_dict(obj))
    return result


@csrf_exempt
def delete_user_info_list(request):
    try:
        user_id = request.POST.get('ID')
        delete_user = UserInfo.objects.get(id=user_id)
        delete_user.delete()
    except:
        traceback.print_exc()
        raise Http404

    return HttpResponse(json.dumps({'ID': user_id}), content_type='application/json')

@csrf_exempt
def update_user_info_list(request):
    try:
        info = request.POST.get(u'USER_INFO_LIST')
        user_id, name, sex, type = info.split(u',')
        user_info = UserInfo.objects.get(id=user_id)
        user_info.name = name
        user_info.sex = sex
        user_info.type = type
        user_info.save()
    except:
        traceback.print_exc()
        raise Http404

    return HttpResponse(json.dumps({'ID': user_id}), content_type='application/json')