import coreapi
import coreschema
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework.schemas import AutoSchema
from rest_framework.utils import json
from rest_framework.views import APIView
# from json_schema_generator import SchemaGenerator
# from asyn.tasks import task_response
from resouces.connect.select_conn import SnapshotUnity, InsUnity, EndResponse, ImageUnity, VolumeUnity, \
    RdbUnity, conn_describe_ins, conn_cease_instanses
from resouces.connect.decorators import token_certify_decorator

conn = None




class instances(APIView):
    """
    get:
        获取回收站instances列表
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field(name='Authorization',required='True',location='header',description='Authentication header',type='string'),
            coreapi.Field(name='DcCode',required='True',location='header',description='dccode header')
        ]

    )
    @method_decorator(token_certify_decorator)
    def get(self,request,conn):
        ins = conn_describe_ins(request,conn)
        # ins = conn.describe_instances(status=["terminated"],owner="usr-zHHGDyko")
        # res = InsUnity(request,ins)
        end = EndResponse(ins,'获取回收站列表成功')
        return JsonResponse(end,safe=False)

class ceaseinstances(APIView):
    """
    delete:
    彻底删除instances
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field (name='Authorization', required='True', location='header',description='Authentication header', type='string'),
            coreapi.Field (name='DcCode', required='True', location='header', description='dccode header'),
            coreapi.Field (name='instances', required=True, location="query", description='主机id')
        ]

    )
    @method_decorator(token_certify_decorator)
    def delete(self,request,conn):
        instances = request.GET.get('instances')
        print(instances)
        instances = instances.split()  #str 分割成列表 如hello world -》  ["hello","world"]
        # print(type(instances))
        res = conn_cease_instanses(request,conn,instances)
        end = EndResponse (res, '彻底删除成功')
        return JsonResponse(end)

class imageslist(APIView):
    """
    get:
        获取回收站镜像
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field (name='Authorization', required='True', location='header',
                           description='Authentication header', type='string'),
            coreapi.Field (name='DcCode', required='True', location='header', description='dccode header'),

        ]
    )
    @method_decorator(token_certify_decorator)
    def get(self,request,conn):                          #request 必须，装饰器需要
        images = conn.describe_images(status='deleted'),
        res = ImageUnity(request,images)
        end = EndResponse (res, 'SUCCESS')
        return JsonResponse(end,safe=False)

class imagescease(APIView):
    """
    delete:
        彻底删除镜像
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field (name='Authorization', required='True', location='header',
                           description='Authentication header', type='string'),
            coreapi.Field (name='DcCode', required='True', location='header', description='dccode header'),
            coreapi.Field(name='images',required=True,location='query',description='镜像id',)
        ]
    )

    @method_decorator(token_certify_decorator)
    def delete(self,request,conn):
        imagesid = request.GET.get('images')
        imagesid = imagesid.split()
        res = conn.cease_images(imagesid)
        end = EndResponse(res,'删除镜像成功')
        return JsonResponse(end)



class volumeslist(APIView):
    """
    get:
        获取回收站硬盘
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field (name='Authorization', required='True', location='header',
                           description='Authentication header', type='string'),
            coreapi.Field (name='DcCode', required='True', location='header', description='dccode header'),

        ]
    )
    @method_decorator(token_certify_decorator)
    def get(self,request,conn):
        volumes = conn.describe_volumes(status=["deleted"]),
        res = VolumeUnity(request,volumes)
        end = EndResponse(res,'SUCCESS')
        return JsonResponse(end,safe=False)

class volumescease(APIView):
    """
    put:
        彻底删除硬盘
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field (name='Authorization', required='True', location='header',
                           description='Authentication header', type='string'),
            coreapi.Field (name='DcCode', required='True', location='header', description='dccode header'),
            coreapi.Field(name='volumes',required=True,location='query',description='硬盘id',)
        ]
    )

    @method_decorator(token_certify_decorator)
    def delete(self,request,conn):
        volumes = request.GET.get('volumes')
        volumes = volumes.split()
        res = conn.cease_volumes(volumes)
        end = EndResponse(res,'删除成功')
        return JsonResponse(end)

class snapshotslist(APIView):
    """
    get:
       获取回收站中的备份
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field (name='Authorization', required='True', location='header',
                           description='Authentication header', type='string'),
            coreapi.Field (name='DcCode', required='True', location='header', description='dccode header'),

        ]
    )
    @method_decorator(token_certify_decorator)
    def get(self,request,conn):
        snapshots = conn.describe_snapshots(status=["deleted"]),
        res = SnapshotUnity(request,snapshots)
        end = EndResponse(res,"SUCCESS")
        return JsonResponse(end,safe=False)

class snapshotscease(APIView):
    """
    delete:
        彻底删除备份
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field (name='Authorization', required='True', location='header',
                           description='Authentication header', type='string'),
            coreapi.Field (name='DcCode', required='True', location='header', description='dccode header'),
            coreapi.Field(name='snapshots',required=True,location='query',description='备份id',)
        ]
    )

    @method_decorator(token_certify_decorator)
    def delete(self,request,conn):
        snapshots = request.GET.get('snapshots')
        snapshots = snapshots.split()
        res = conn.cease_snapshots(snapshots)
        # print(res)
        end = EndResponse(res,"删除成功")
        # print(end)
        return JsonResponse(end,safe=False)

class rdbslist(APIView):
    """
    get:
       获取回收站中的rdb
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field (name='Authorization', required='True', location='header',
                           description='Authentication header', type='string'),
            coreapi.Field (name='DcCode', required='True', location='header', description='dccode header'),

        ]
    )
    @method_decorator(token_certify_decorator)
    def get(self,request,conn):
        rdbs = conn.describe_rdbs(status=["deleted"]),
        res = RdbUnity(request,rdbs)
        end = EndResponse(res,"SUCCESS")
        return JsonResponse(end,safe=False)

class rdbscease(APIView):
    """
    delete:
        彻底删除rdb
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field (name='Authorization', required='True', location='header',
                           description='Authentication header', type='string'),
            coreapi.Field (name='DcCode', required='True', location='header', description='dccode header'),
            coreapi.Field(name='rdbs',required=True,location='query',description='rdbid',)
        ]
    )

    @method_decorator(token_certify_decorator)
    def delete(self,request,conn):
        rdbs = request.GET.get('rdbs')
        rdbs = rdbs.split()
        res = conn.cease_rdbs(rdbs)
        end = EndResponse(res,"删除成功")
        return JsonResponse(end)
