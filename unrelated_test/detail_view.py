import json

import coreapi
from django.http import JsonResponse
from django.utils.decorators import method_decorator

from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView
from urllib import request as urllib_request

from resouces.connect.decorators import token_certify_decorator
from resouces.connect.select_conn import conn_describe_ins


class InstanceDetail(APIView):
    """
    get:
        获取回收站instance详情
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field(
                name='Authorization',
                required='True',
                location='header',
                description='Authentication header',
                type='string'),
            coreapi.Field(
                name='DcCode',
                required='True',
                location='header',
                description='dccode header'),
            coreapi.Field(
                name='instance',
                required=True,
                location="query",
                description='主机id')])
    # @method_decorator(token_certify_decorator)

    def get(self, request):
        url = 'http://10.22.29.100:8081/iaas/instance/'
        instance = request.GET.get('instance')
        token = request.META.get('HTTP_AUTHORIZATION', None)
        dc_code = request.META.get('HTTP_DCCODE', None)
        header = {
            'Authorization': token,
            'DcCode': dc_code}

        req = urllib_request.Request(url=url + instance, headers=header)

        # print (req)
        res2 = urllib_request.urlopen(req)
        res2 = res2.read()
        res2 = json.loads(res2)

        return JsonResponse(res2, safe=False)
