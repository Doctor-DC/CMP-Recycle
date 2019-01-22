import configparser

# 读取配置文件
config = configparser.ConfigParser ()
config.read ("D:\\MyDownloads\Recycle\\resouces\\connect\\Config.ini")
# config.read ('/root/python/work/venv3/Recycle/resouces/connect/Config.ini')

# secs = config.sections()
# print(secs)

qing_zone = config.get ("Qing", "zone")
qing_host = config.get ("Qing", "host")
qing_port = config.get ("Qing", "port")
qing_port = int(qing_port)

os_auth_url = config.get("OpenStack","auth_url")
os_project_name = config.get("OpenStack","project_name")
os_region_name = config.get("OpenStack","region_name")
os_domain_id = config.get("OpenStack","domain_id")

sql_host = config.get("Mysql","host")
sql_user = config.get("Mysql","user")
sql_password = config.get("Mysql","password")
sql_db = config.get("Mysql","db")
sql_port = config.get("Mysql","port")
sql_port = int(sql_port)

valut_url = config.get("Valut","url")
valut_token = config.get("Valut","token")



# class QingGlobal:
#     def __init__(self):
#         self.qingzone='LFRZ1'
#         self.qinghost="api.enncloud.cn"
#
#         self.host = "10.22.29.100",
#         self.user = "root",
#         self.password = "1qazXSW@",
#         self.db = "cmp",
#         self.port = 3306
#
# QING = QingGlobal()
# # SQL = SqlGlobal()
