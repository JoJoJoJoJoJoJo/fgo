from django.shortcuts import render
from django.conf import settings
import hashlib
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def token_handler(request):
    token = settings.TOKEN
    try:
        data = request.GET
        # print(data)
        if len(data) == 0:
            return HttpResponse('Error:No args received')
        # 发过来的请求带有4个参数
        signature = data['signature']
        timestamp = data['timestamp']
        nonce = data['nonce']
        echostr = data['echostr']
        # print(signature,timestamp,nonce,echostr)
        # 根据文档要求进行校验
        l = [token,timestamp,nonce]
        l.sort()
        s = ''.join(l).encode()
        sha1 = hashlib.sha1()
        sha1.update(s)
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            # print('success')
            return HttpResponse(echostr)

        else:
            # print('fail')
            return HttpResponse(u'校验失败')

    except Exception as e:
        # print('error')
        return HttpResponse('Internal Error,{}'.format(e))

