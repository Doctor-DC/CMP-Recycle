
def conn_server(request,conn):
    dc_code = request.META.get ('HTTP_DCCODE', None)
    if dc_code =="S03-HB-002":
        res = conn.describe_instances(status=["terminated"])
    else:
        list = []
        for server in conn.compute.servers (status='SOFT_DELETED'):
            list.append (server)

        res = list
    return res

def unity(request,data):
    dc_code = request.META.get('HTTP_DCCODE',None)
    if dc_code =="S03-HB-002":
        datalist = data['instance_set']
        data_set = []
        for index in range (len(datalist)):
            dataone = datalist[index]

            newdata = {}
            newdata['resourceId'] = dataone['instance_id']
            newdata['resourceName'] = dataone['instance_name']
            newdata['images'] = {}
            newdata['images']['imageId'] = dataone['image']['image_id']
            newdata['images']['imageName'] = dataone['image']['image_name']
            newdata['deletetime'] = dataone['status_time']
            data_set.append(newdata)
        Newdata = {}
        # print(data_set)
        Newdata['list'] = data_set
        return Newdata
    else:
        return data
        # print(data)
        # datalist = data['data']['data']
        # data_set = []
        # for index in range (len (datalist)):
        #     dataone = datalist[index]
        #
        #     newdata = {}
        #     newdata['resourceId'] = data['id']
        #     newdata['resourceName'] = dataone['name']
        #     newdata['images'] = {}
        #     newdata['image']['imageId'] = dataone['imageId']
        #     newdata['image']['imageName'] = dataone['imageName']
        #     newdata['deletetime'] = dataone['updatatime']
        #     data_set.append (newdata)
        # Newdata = {}
        # Newdata['list'] = data_set
        # return Newdata