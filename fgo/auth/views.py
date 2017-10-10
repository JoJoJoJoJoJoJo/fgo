from django.shortcuts import render
from django.conf import settings
import hashlib


def token_handler(request):
    token = settings.TOKEN
    try:
        data = request.GET
        if len(data) == 0:
            return 'Error:No args received'
        # 发过来的请求带有4个参数
        signature = data.get('signature')
        timestamp  = data.get('timestamp')
        nonce = data.get('nonce')
        echostr = data.get('echostr')
        #根据文档要求进行校验
        l = [token,timestamp,nonce]
        l.sort()
        sha1 = hashlib.sha1()
        map(sha1.update,l)
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            return echostr
    except Exception as e:
        return e

