import hvac
# Using plaintext
from resouces.connect.mysql import getparams

client = hvac.Client(url='http://10.22.28.151:8200', token='5IFiMasppgZJymn5lqiZL3kF')

def connect_valut(orgCode,dc_code):
    # global \
    ak=''
    sk=''

    pool_id = getparams(orgCode,dc_code)
    # pool_id = 9
    id = str(pool_id)
    print(client.read('secret/iaasbroker-service/pool/' + id))
    pool= client.read('secret/iaasbroker-service/pool/'+id)
    data = pool['data']

    if "access_key_id" in data:
        ak = data['access_key_id']
        sk = data['access_key_secret']
    else:
        ak = data['username']
        sk = data['password']
    print(ak,sk)
    return(ak,sk)

# ak,sk = connect_valut(100001,"S03-HB-002")