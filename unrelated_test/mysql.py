import pymysql

from unrelated_test.qing_conn_test import quota_list

db = pymysql.connect (host="10.22.29.100", user="root",
                      password="1qazXSW@", db="test", port=3306)

cursor = db.cursor ()

# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute ("DROP TABLE IF EXISTS EMPLOYEE")


sql = """INSERT INTO QUOTA(RESCOURCE_TYPE,
       QUOTA_LEFT, QUOTA_ALL)
       VALUES (%s,%s,%s)
       """
# T = (('Mac',20,3000),('Mac',20,3000))
# T = [['Mac',20,3000],['Mac',20,3000]]
# print(type(T))

lists = quota_list()
T = []
for index in lists:
    list = (index['resource_type'],index['left'],index['quota'])
    T.append(list)

print(T)
      
try:
    # 执行sql语句
    cursor.executemany(sql,T)
    # 提交到数据库执行
    db.commit ()
except:
    # 如果发生错误则回滚
    db.rollback ()

# 关闭数据库连接
db.close ()