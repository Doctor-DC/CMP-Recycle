import coreapi
import coreschema
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.schemas import AutoSchema
from rest_framework.utils import json
from rest_framework.views import APIView
# from json_schema_generator import SchemaGenerator
# from asyn.tasks import task_response
from resouces.connect.select_conn import snapshot_unity, ins_unity, end_response, image_unity, volume_unity, \
    rdb_unity, conn_describe_ins, conn_cease_instanses
from resouces.connect.decorators import token_certify_decorator

conn = None


class InstancesList(APIView):
    """
    get:
        获取回收站instances列表
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
                description='dccode header')])

    @method_decorator(token_certify_decorator)
    def get(self, request, conn):
        ins = conn_describe_ins(request, conn)
        # ins = conn.describe_instances(status=["terminated"],owner="usr-zHHGDyko")
        # res = InsUnity(request,ins)
        end = end_response(ins, '获取回收站列表成功')
        print(type(end))
        return JsonResponse(end, safe=False)


class CeaseInstances(APIView):
    """
    delete:
    彻底删除instances
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
                name='instances',
                required=True,
                location="query",
                description='主机id')])
    # schema.get_link(method='delete')

    @method_decorator(token_certify_decorator)
    def delete(self, request, conn):
        instances = request.GET.get('instances')
        print(instances)
        # str 分割成列表 如hello world -》  ["hello","world"]
        instances = instances.split()
        # print(type(instances))
        res = conn_cease_instanses(request, conn, instances)
        end = end_response(res, '彻底删除成功')
        return JsonResponse(end)


class ImagesList(APIView):
    """
    get:
        获取回收站镜像
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
        ])

    @method_decorator(token_certify_decorator)
    def get(self, request, conn):  # request 必须，装饰器需要
        try:
            images = conn.describe_images(status='deleted')
        except AttributeError:
            resp = {
                'errorCode': 0,
                'errorMessage': 'dc_code无效,openstack暂无此功能',
                'content': None,
                'resultCode': 1,
                'resultMessage': ''}
            return JsonResponse(resp, status=200)
        res = image_unity(request, images)
        end = end_response(res, 'SUCCESS')
        return JsonResponse(end, safe=False)


class ImagesCease(APIView):
    """
    delete:
        彻底删除镜像
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
                name='images',
                required=True,
                location='query',
                description='镜像id',
            )])

    @method_decorator(token_certify_decorator)
    def delete(self, request, conn):
        imagesid = request.GET.get('images')
        imagesid = imagesid.split()
        res = conn.cease_images(imagesid)
        end = end_response(res, '删除镜像成功')
        return JsonResponse(end)


class VolumesList(APIView):
    """
    get:
        获取回收站硬盘
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
        ])

    @method_decorator(token_certify_decorator)
    def get(self, request, conn):
        volumes = conn.describe_volumes(status=["deleted"]),
        res = volume_unity(request, volumes)
        end = end_response(res, 'SUCCESS')
        return JsonResponse(end, safe=False)


class VolumesCease(APIView):
    """
    delete:
        彻底删除硬盘
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
                name='volumes',
                required=True,
                location='query',
                description='硬盘id',
            )])

    @method_decorator(token_certify_decorator)
    def delete(self, request, conn):
        volumes = request.GET.get('volumes')
        volumes = volumes.split()
        res = conn.cease_volumes(volumes)
        end = end_response(res, '删除成功')
        return JsonResponse(end)


class SnapshotsList(APIView):
    """
    get:
       获取回收站中的备份
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
        ])

    @method_decorator(token_certify_decorator)
    def get(self, request, conn):
        snapshots = conn.describe_snapshots(status=["deleted"]),
        res = snapshot_unity(request, snapshots)
        end = end_response(res, "SUCCESS")
        return JsonResponse(end, safe=False)


class SnapshotsCease(APIView):
    """
    delete:
        彻底删除备份
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
                name='snapshots',
                required=True,
                location='query',
                description='备份id',
            )])

    @method_decorator(token_certify_decorator)
    def delete(self, request, conn):
        snapshots = request.GET.get('snapshots')
        snapshots = snapshots.split()
        res = conn.cease_snapshots(snapshots)
        # print(res)
        end = end_response(res, "删除成功")
        # print(end)
        return JsonResponse(end, safe=False)


class RdbsList(APIView):
    """
    get:
       获取回收站中的rdb
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
        ])

    @method_decorator(token_certify_decorator)
    def get(self, request, conn):
        rdbs = conn.describe_rdbs(status=["deleted"]),
        res = rdb_unity(request, rdbs)
        end = end_response(res, "SUCCESS")
        return JsonResponse(end, safe=False)


class RdbsCease(APIView):
    """
    delete:
        彻底删除rdb
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
                name='rdbs',
                required=True,
                location='query',
                description='rdbid',
            )])

    @method_decorator(token_certify_decorator)
    def delete(self, request, conn):
        rdbs = request.GET.get('rdbs')
        rdbs = rdbs.split()
        res = conn.cease_rdbs(rdbs)
        end = end_response(res, "删除成功")
        return JsonResponse(end)
