
from SDK.qingcloud.iaas.connection import APIConnection
from resouces.connect.config_para import qing_zone, qing_host, qing_port


def new_connect_to_zone(
        zone,
        access_key_id,
        secret_access_key,
        host,
        port,
        lowercase=True):

    if lowercase:
        zone = zone.strip().lower()
    return APIConnection(
        access_key_id,
        secret_access_key,
        zone,
        host,
        port,
        protocol="http",
        pool=None,
        expires=None,
        retry_time=2,
        http_socket_timeout=60,
        debug=True)


def connect_qing(ak, sk):
    conn = new_connect_to_zone(
        zone=qing_zone,  # 你的资源所在的节点ID，可在控制台切换节点的地方查看，如 'pek1', 'pek2', 'gd1' 等
        access_key_id=ak,
        secret_access_key=sk,
        host=qing_host,
        port=qing_port,
        lowercase=False,
    )
    # print (type (conn))
    return (conn)

# conn = connect_qing("XJBTKEUYJWEQIRFTAGLH","9dCGFkYEqAnYuxQdfklNj3hyAQoNVzriIClLcNV6")
# print(type(conn))