from SDK import openstack
from resouces.connect.config_para import os_auth_url,os_project_name,os_region_name,os_domain_id


def create_connection(ak,sk):

    return openstack.connect(
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

# conn = create_connection(auth_url='http://10.19.137.110:20001/keystone/v3', project_name='CMP_DEV', region='FFFFF', username='cmp_dev', password='!QAZxsw2')
# print(conn)
#S01-HD-001