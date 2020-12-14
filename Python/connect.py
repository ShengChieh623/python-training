# import pymysql

import pymysql.cursors

# try:
config = {
'host':'59.125.94.41',
'port':3306,
'user':'webdemo',
'password':'TjV8cXGw!77H',
'db':'webdemo',
'charset':'utf8mb4',
'cursorclass':pymysql.cursors.DictCursor,
}
# Connect to the database
connection = pymysql.connect(**config)
connection.close()
# except Exception as e:
    # connection.rollback()
#     print("Error!:{0}".format(e))
# finally:
    # connection.close()
