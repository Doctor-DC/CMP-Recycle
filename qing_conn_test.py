from resouces.qingcloud.qingcloud_conn import new_connect_to_zone

conn2 = new_connect_to_zone (
            zone='LFRZ1',  # 你的资源所在的节点ID，可在控制台切换节点的地方查看，如 'pek1', 'pek2', 'gd1' 等
            access_key_id="CPCYMTFLBEVDKENFCUIQ", #"XJBTKEUYJWEQIRFTAGLH",
            secret_access_key="ugwWAEekJiX8hpdm3rCbfK2Y6VihEpLzaDZbGN6C",#"9dCGFkYEqAnYuxQdfklNj3hyAQoNVzriIClLcNV6",
            host="api.enncloud.cn",
            port=80,
            lowercase=False,
        )
# ret = conn2.describe_instances (status=["terminated"],owner="usr-zHHGDyko")
# ret = conn2.cease_instances (["i-tstobohq"])
# ret = conn2.describe_images (status=["deleted"],owner="usr-zHHGDyko")
# ret = conn2.cease_images (["img-6oquy2in"])
# ret = conn2.describe_volumes (status=["deleted"],owner="usr-zHHGDyko")
#
# ret = conn2.describe_quotas()
# quota_set = ret['quota_set'][0]
# instance = quota_set['instance']

ret = conn2.get_quota_left()
quota_set = ret['quota_left_set']
for index in range(len(quota_set)):
    quota = quota_set[index]
    if quota['resource_type'] == "instance":
        instance = quota['left']
        print(instance)
    else:
        pass