
from SDK.qingcloud.iaas.connection import APIConnection

def new_connect_to_zone(zone, access_key_id, secret_access_key, host, port,lowercase=True):

    if lowercase:
        zone = zone.strip().lower()
    return APIConnection(access_key_id, secret_access_key, zone, host, port, protocol="http",
                 pool=None, expires=None,
                 retry_time=2, http_socket_timeout=60, debug=True)

def connect_qing(ak,sk):
    conn = new_connect_to_zone (
        zone='LFRZ1',  # 你的资源所在的节点ID，可在控制台切换节点的地方查看，如 'pek1', 'pek2', 'gd1' 等
        access_key_id=ak,
        secret_access_key=sk,
        host="api.enncloud.cn",
        port=80,
        lowercase=False,
    )
    return (conn)


