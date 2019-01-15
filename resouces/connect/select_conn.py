
def conn_describe_ins(request,conn):
    dc_code = request.META.get ('HTTP_DCCODE', None)
    if dc_code =="S03-HB-002":
        res = conn.describe_instances(status=["terminated"])

        datalist = res['instance_set']
        print (type (res))
        data_set = []
        for index in range (len (datalist)):
            dataone = datalist[index]

            newdata = {}
            newdata['resourceId'] = dataone['instance_id']
            newdata['resourceName'] = dataone['instance_name']
            newdata['image'] = {}
            newdata['image']['imageId'] = dataone['image']['image_id']
            newdata['image']['imageName'] = dataone['image']['image_name']
            newdata['deletetime'] = dataone['status_time']
            data_set.append (newdata)
        Newdata = {}
        # print(data_set)
        Newdata['list'] = data_set
        return Newdata
    else:
        list = []
        for server in conn.compute.servers (status='SOFT_DELETED'):
            list.append (server)
        res = list

        data_set = []
        for index in range (len (res)):
            dataone = res[index]

            newdata = {}
            newdata['resourceId'] = dataone['id']
            print(dataone)
            newdata['resourceName'] = dataone['name']
            newdata['image'] = {}
            # newdata['image']['imageId'] = dataone['instance_id']
            # newdata['image']['imageName'] = dataone['instance_name']
            newdata['deletetime'] = dataone['updated_at']
            data_set.append (newdata)
        Newdata = {}
        Newdata['list'] = data_set
        return Newdata

def conn_cease_instanses(request,conn,instances):
    dc_code = request.META.get ('HTTP_DCCODE', None)
    if dc_code =="S03-HB-002":
        res = conn.cease_instances(instances)
    else:
        res =  conn.compute.delete_server (instances, force=True)

    return res


def EndResponse(res,resultMessage):
    if res == None:
        resp = {'errorCode': 0, 'errorMessage': '', 'content': res, 'resultCode': 1, 'resultMessage': resultMessage}
    elif ('message' in res.keys ()):
        resp = {'errorCode': res['ret_code'], 'errorMessage': res['message'], 'content': {}, 'resultCode': 0,
                'resultMessage': 'FAILURE'}
    else:
        resp = {'errorCode': 0, 'errorMessage': '', 'content': res, 'resultCode': 1, 'resultMessage': resultMessage}
    return  resp

def InsUnity(request,data):
    dc_code = request.META.get('HTTP_DCCODE',None)
    if dc_code =="S03-HB-002":
        datalist = data['instance_set']
        print (type (data))
        data_set = []
        for index in range (len(datalist)):
            dataone = datalist[index]

            newdata = {}
            newdata['resourceId'] = dataone['instance_id']
            newdata['resourceName'] = dataone['instance_name']
            newdata['image'] = {}
            newdata['image']['imageId'] = dataone['image']['image_id']
            newdata['image']['imageName'] = dataone['image']['image_name']
            newdata['deletetime'] = dataone['status_time']
            data_set.append(newdata)
        Newdata = {}
        # print(data_set)
        Newdata['list'] = data_set
        return Newdata
    else:
        # datalist = data[0]
        data_set = []
        for index in range (len (data)):
            dataone = data[index]

            newdata = {}
            newdata['resourceId'] = dataone['id']
            print(dataone)
            newdata['resourceName'] = dataone['name']
            newdata['image'] = {}
            # newdata['image']['imageId'] = dataone['instance_id']
            # newdata['image']['imageName'] = dataone['instance_name']
            newdata['deletetime'] = dataone['updated_at']
            data_set.append (newdata)
        Newdata = {}
        Newdata['list'] = data_set
        return Newdata

def ImageUnity(request,data):
    # dc_code = request.META.get('HTTP_DCCODE',None)
    # if dc_code =="S03-HB-002":
    #     print(type(data))
        datalist = data[0]
        datalist = datalist['image_set']
        data_set = []
        for index in range (len(datalist)):
            dataone = datalist[index]

            newdata = {}
            newdata['status'] = "deleted"
            newdata['size'] = dataone['size']
            newdata['image'] = {}
            newdata['image']['imageId'] = dataone['image_id']
            newdata['image']['imageName'] = dataone['image_name']
            newdata['deletetime'] = dataone['status_time']
            data_set.append(newdata)
        Newdata = {}
        # print(data_set)
        Newdata['list'] = data_set
        return Newdata

def VolumeUnity(request,data):
    # dc_code = request.META.get('HTTP_DCCODE',None)
    # if dc_code =="S03-HB-002":
    #     print(type(data))
        datalist = data[0]
        datalist = datalist['volume_set']
        data_set = []
        for index in range (len(datalist)):
            dataone = datalist[index]

            newdata = {}
            newdata['status'] = "deleted"
            newdata['size'] = dataone['size']
            newdata['zone'] = dataone['zone_id']
            newdata['resourceId'] = dataone['volume_id']
            newdata['resourceName'] = dataone['volume_name']
            newdata['deletetime'] = dataone['status_time']
            data_set.append(newdata)
        Newdata = {}
        # print(data_set)
        Newdata['list'] = data_set
        return Newdata

def SnapshotUnity(request,data):
    # dc_code = request.META.get('HTTP_DCCODE',None)
    # if dc_code =="S03-HB-002":
    #     print(type(data))
        datalist = data[0]
        datalist = datalist['snapshot_set']
        data_set = []
        for index in range (len(datalist)):
            dataone = datalist[index]

            newdata = {}
            newdata['status'] = "deleted"
            newdata['size'] = dataone['size']
            # newdata['zone'] = dataone['zone_id']
            newdata['resourceId'] = dataone['snapshot_id']
            newdata['resourceName'] = dataone['snapshot_name']
            newdata['sourceId'] = dataone['resource']['resource_id']
            # newdata['source'] = dataone['resource']['resource_name']
            newdata['deletetime'] = dataone['status_time']
            data_set.append(newdata)
        Newdata = {}
        # print(data_set)
        Newdata['list'] = data_set
        return Newdata

def RdbUnity(request,data):
    # dc_code = request.META.get('HTTP_DCCODE',None)
    # if dc_code =="S03-HB-002":
    #     print(type(data))
        datalist = data[0]
        datalist = datalist['rdb_set']
        data_set = []
        for index in range (len(datalist)):
            dataone = datalist[index]

            newdata = {}
            newdata['status'] = "deleted"
            newdata['size'] = dataone['storage_size']
            newdata['zone'] = dataone['zone_id']
            newdata['resourceId'] = dataone['rdb_id']
            newdata['resourceName'] = dataone['rdb_name']
            newdata['deletetime'] = dataone['status_time']
            data_set.append(newdata)
        Newdata = {}
        # print(data_set)
        Newdata['list'] = data_set
        return Newdata