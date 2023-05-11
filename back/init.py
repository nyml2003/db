import pymysql
from pymysql.constants import CLIENT

conn = pymysql.connect(
    host="124.71.219.185",
    port = 3306, 
    user="root",
    password="uestc2022!",
    database="CS2305.his",
    charset="utf8",
    client_flag=CLIENT.MULTI_STATEMENTS
)
cursor = conn.cursor()
sql = """




"""
cursor.execute(sql)
conn.commit()
ret = cursor.fetchall()
cursor.close()
conn.close()
print(ret)