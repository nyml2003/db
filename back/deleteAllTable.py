
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

# 获取所有表名
# cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'CS2305.his' AND TABLE_NAME = 'Patient';")
tables = cursor.fetchall()
print(tables)
# 删除所有表
for table in tables:
    cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")

# 关闭连接
conn.close()