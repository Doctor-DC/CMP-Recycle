import jwt
import SDK.openstack
from django.http import JsonResponse
from jwt import DecodeError

from resouces.connect.config_para import qing_zone, qing_host, qing_port, os_auth_url, os_project_name, os_region_name, \
    os_domain_id
# from resouces.SDK.openstack.ostack_conn import create_connection
from resouces.qingcloud.qingcloud_conn import new_connect_to_zone, connect_qing
from resouces.connect.valut import connect_valut


def token_certify_decorator(func):  # 验证token，zone，获取conn实例
    def wrapper(request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION', None)
        auth = token.split()
        if len(auth) != 2:
            msg = ('token无效')
            resp = {
                'errorCode': 0,
                'errorMessage': msg,
                'content': {},
                'resultCode': 1,
                'resultMessage': ''}
            return JsonResponse(resp, status=200)
        try:
            decoded = jwt.decode(auth[1], None, False)
            orgCode = decoded['orgCode']
            # print(orgCode)

        except DecodeError:
            msg = ('token无效')
            resp = {
                'errorCode': 0,
                'errorMessage': msg,
                'content': {},
                'resultCode': 1,
                'resultMessage': ''}
            return JsonResponse(resp, status=200)

        dc_code = request.META.get('HTTP_DCCODE', None)
        try:
            ak, sk = connect_valut(orgCode, dc_code)
        except TypeError:
            msg = ('dc_code无效')
            resp = {
                'errorCode': 0,
                'errorMessage': msg,
                'content': None,
                'resultCode': 1,
                'resultMessage': ''}
            return JsonResponse(resp, status=200)

        if dc_code == "S03-HB-002":
            conn = new_connect_to_zone(
                zone=qing_zone,  # 你的资源所在的节点ID，可在控制台切换节点的地方查看，如 'pek1', 'pek2', 'gd1' 等
                access_key_id=ak,
                secret_access_key=sk,
                host=qing_host,
                port=qing_port,
                lowercase=False,
            )
        

        else:
            conn = SDK.openstack.connect(
                auth_url=os_auth_url,
                project_name=os_project_name,
                username=ak,
                password=sk,
                region_name=os_region_name,
                domain_id=os_domain_id,
                # domin_name='default',
                # project_domin_name='default'
                # app_name='examples',
                # app_version='1.0',
            )
        kwargs.update({
            'conn': conn
        })

        return func(request, *args, **kwargs)
    return wrapper
