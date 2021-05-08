import django_filters
from rest_framework import viewsets, filters
from .models import Preset,Photo
from .serializer import PresetSerializer
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.http import Http404



class PresetViewSet(viewsets.ModelViewSet):
    queryset = Preset.objects.all()
    serializer_class = PresetSerializer

a=0
@require_POST
@csrf_exempt
def upload(request,newpreset_name):

    #同じpresetがある場合、消去する
    try:
        Preset.objects.get(title=newpreset_name)
    except (KeyError,Preset.DoesNotExist):
        print("cant find preset & create new preset")
        preset = Preset(title=newpreset_name)
        preset.save()
    else:
        Photo.objects.filter(preset=newpreset_name).delete()

    #画像を保存
    for i in range(int(request.POST.get('number'))):
        upload_file = request.FILES['file'+str(i)]
        photo = Photo(preset_id=newpreset_name,file=upload_file)
        photo.save()

    current_site = get_current_site(request)
    domain = current_site.domain
    download_url = '{0}://{1}{2}'.format(
    request.scheme,
    domain,
    photo.file.url,
    )

    return HttpResponse(download_url, content_type="text/plain")


@csrf_exempt
def download(request,preset_name):
    getset = Photo.objects.filter(preset=preset_name)
    current_site = get_current_site(request)
    domain = current_site.domain
    download_url=[]
    i=0
    for instance in getset:
        url = '{0}://{1}{2}'.format(
            request.scheme,
            domain,
            instance.file.url,
        )
        download_url.append(url)
        i+=1
    print(download_url)
    params = {'imgset':download_url}
    params = json.dumps(params)
    return HttpResponse(params, content_type="text/plain")
