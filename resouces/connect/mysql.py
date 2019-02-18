import json
import pymysql
from django.http import JsonResponse

from resouces.connect.config_para import sql_host ,sql_user,sql_password,sql_db,sql_port


def getparams(orgCode,dc_code):
    # print(sql_host)
    db = pymysql.connect(
        host=sql_host,
        user=sql_user,
        password=sql_password,
        db=sql_db,
        port=sql_port
    )

    cursor = db.cursor()
    projectid = orgCode
    provider = dc_code

    sql = """
        SELECT
        A.POOL_ID,
        A.DC_CODE,
        B.PROJECT_ID,
        A.PROVIDER
        FROM
        RES_POOL A
        JOIN RES_PROJECT_POOL B ON A.POOL_ID = B.POOL_ID
        AND B.PROJECT_ID = '%s'
        AND A.DC_CODE = '%s'
          """

    cursor.execute(sql%(projectid,provider))

    try:
        results = cursor.fetchone ()
        pool_id = results[0]
    except TypeError:
        msg = ('dc_code无效')
        resp = {'errorCode': 0, 'errorMessage': msg, 'content': {}, 'resultCode': 1, 'resultMessage': ''}
        return JsonResponse (resp, status=200)
    db.close()
    return(pool_id)
#
# print(getparams(100001,"S03-HB-002"))