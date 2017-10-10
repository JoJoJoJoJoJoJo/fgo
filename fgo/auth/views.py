from django.shortcuts import render
from django.conf import settings
import hashlib
from django.http import HttpResponse


def token_handler(request):
    token = settings.TOKEN
    try:
        data = request.GET
        # print(data)
        if len(data) == 0:
            return HttpResponse('Error:No args received')
        # 发过来的请求带有4个参数
        signature = data['signature']
        timestamp  = data['timestamp']
        nonce = data['nonce']
        echostr = data['echostr']
        # 根据文档要求进行校验
        l = [token,timestamp,nonce]
        l.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,l)
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse(u'校验失败')
    except Exception as e:
        return HttpResponse('Internal Error,{}'.format(e))

