
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