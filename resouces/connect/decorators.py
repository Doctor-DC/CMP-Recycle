import jwt
from SDK import openstack
from django.http import JsonResponse
from jwt import DecodeError

from resouces.qingcloud.qingcloud_conn import new_connect_to_zone, connect_qing
from resouces.connect.valut import connect_valut


def token_certify_decorator(func):#验证token，zone，获取conn实例
    def wrapper(request, *args, **kwargs):

        token = request.META.get ('HTTP_AUTHORIZATION', None)
        auth = token.split()
        if len (auth) != 2:
            msg = ('token无效')
            resp = {'errorCode': 0, 'errorMessage': msg, 'content': {}, 'resultCode': 1, 'resultMessage': ''}
            return JsonResponse (resp, status=200)
        try:
            decoded = jwt.decode (auth[1], None, False)
            orgCode = decoded['orgCode']
            print (orgCode)

        except DecodeError:
            msg = ('token无效')
            resp = {'errorCode': 0, 'errorMessage': msg, 'content': {}, 'resultCode': 1, 'resultMessage': ''}
            return JsonResponse (resp, status=200)


        dc_code = request.META.get('HTTP_DCCODE',None)
        try:
            ak,sk = connect_valut(orgCode,dc_code)
        except ValueError:
            msg = ('dc_code无效')
            resp = {'errorCode': 0, 'errorMessage': msg, 'content': {}, 'resultCode': 1, 'resultMessage': ''}
            return JsonResponse (resp, status=200)

        if dc_code == "S03-HB-002":
            conn = connect_qing(ak,sk)
        else:
            conn = create_connection(ak,sk)

        kwargs.update ({
            'conn': conn
        })

        return func(request, *args, **kwargs)
    return wrapper




def create_connection(ak,sk):

    return openstack.connect(
        auth_url='http://10.19.137.110:20001/keystone/v3',
        project_name='CMP_DEV',
        username=ak,
        password=sk,
        region_name='FFFFF',
        domain_id='default',
        # domin_name='default',
        # project_domin_name='default'
        # app_name='examples',
        # app_version='1.0',
    )

# conn = create_connection(auth_url='http://10.19.137.110:20001/keystone/v3', project_name='CMP_DEV', region='FFFFF', username='cmp_dev', password='!QAZxsw2')
# print(conn)