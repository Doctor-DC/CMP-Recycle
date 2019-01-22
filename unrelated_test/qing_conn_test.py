from django.core.paginator import Paginator

from resouces.qingcloud.qingcloud_conn import new_connect_to_zone

conn = new_connect_to_zone (
            zone='LFRZ1',  # 你的资源所在的节点ID，可在控制台切换节点的地方查看，如 'pek1', 'pek2', 'gd1' 等
            access_key_id="XJBTKEUYJWEQIRFTAGLH",
            secret_access_key="9dCGFkYEqAnYuxQdfklNj3hyAQoNVzriIClLcNV6",
            host="api.enncloud.cn",
            port=80,
            lowercase=False,
        )


# res = conn.describe_instances ()
# res = conn.describe_instances (limit=1, offset=10, )
# datalist = res['instance_set']
# # print(datalist)
# page1=Paginator(datalist,2,10)
# print(page1.count)
# print(page1.page(2).object_list)


def quota_list():
    ret = conn.describe_quotas()
    quota_left = conn.get_quota_left()
    
    quota_left = quota_left['quota_left_set']
    quota_all = ret['quota_set'][0]
    
    # print(type(quota_all.keys()))
    # instance = quota_all['instance']
    list = []
    for key in quota_all.keys():
        for x in range(len(quota_left)):
            left = quota_left[x]
            if left['resource_type'] == key:
    
                quota = quota_all[key]
                new = {}
                new.update(left)
                new.update({'quota': quota})
                list.append(new)
                break
            else:
                pass
    return(list)

from urllib import parse,request

#输出内容:user=admin&password=admin
header = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjbXBfYWRtaW4iLCJwaG9uZSI6IiIsIm9yZ0NvZGUiOjEwMDAwMSwiZXhwIjoxNTM2ODMzNzgyLCJ1dWlkIjoiNDI3YWIwMDgtZTk4Zi00ZjUzLWIzZDctOTJkZTFhNGQ4OTNkIiwiZW1haWwiOiIiLCJhdXRob3JpdGllcyI6WyJST0xFX1NZUyIsIkNNUF9DTVBfQURNSU4iLCJCTVNfU1lTIl0sInJlc291cmNlQ29kZXMiOltdLCJ1c2VybmFtZSI6ImNtcF9hZG1pbiJ9.Qopxx0-ELTaRUjGwGuHGmhuAdmgwVR18hnqBGHXN1Yw-HxNtyDREkRQn1W3yWNpxLudlgaNkPQUJTHxpP6XFoA',
          'DcCode':'S03-HB-002'}
url ='http://10.22.29.100:8081/iaas/instance/'
path = 'i-w1uqifnm'
req = request.Request(url=url+path,headers=header)
print(req)
res2 = request.urlopen(req)
res2 = res2.read()
print(res2)