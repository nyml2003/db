import pymysql
from pymysql.constants import CLIENT
class DataBase():
    def __init__(self):
        self.conn = pymysql.connect(
            host="124.71.219.185",
            port = 3306, 
            user="root",
            password="uestc2022!",
            database="cs2305.his",
            charset="utf8",
            client_flag=CLIENT.MULTI_STATEMENTS
        )
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
    def execute(self,sql, params=None):
        try:
            self.cursor.execute(sql, params)
            self.conn.commit()
            ret = {"error":True,"content":self.cursor.fetchall()}
        except Exception as e:
            self.conn.rollback()
            ret = {'error': False,"content":{"error":str(e)}}
            print(ret)
        finally:
            self.cursor.close()
            self.conn.close()
        return ret
    def getTable(self,table):
        sql=f"SELECT * FROM {table}"
        return self.execute(sql)
    def getView(self,view):
        sql=f"SELECT * FROM {view}"
        return self.execute(sql)
    def update(self, table, id, col, value,pk):
        sql = f"UPDATE {table} SET {col} = %s WHERE {pk} = %s"
        return self.execute(sql, (value, id))
    def delete(self,table,id,pk):
        sql = f"DELETE FROM {table} WHERE {pk} = %s"
        return self.execute(sql, (id,))
    def insert(self,table,values):
        sql = f"INSERT INTO {table} VALUES ({','.join(['%s']*len(values))})"
        return self.execute(sql, values)
    def login(self,username):
        sql = f"SELECT * FROM `cs2305.user` WHERE username=%s"
        return self.execute(sql, (username))
    def register(self,username,password,role):
        sql = f"INSERT INTO `cs2305.user` (username, password, role) VALUES (%s,%s,%s)"
        return self.execute(sql, (username,password,role))
        
    def search(self,table,col,value):
        sql = f"SELECT * FROM `{table}` WHERE {col} LIKE %s"
        return self.execute(sql, (value,))
    def guahao(self,table,values):
        sql = f"INSERT INTO {table} (RFdept,RFdoctor,RFpatient,RFtime,RFnotes) VALUES ({','.join(['%s']*len(values))})"
        return self.execute(sql, values)
    # def deleteAllTables(self):
    #     sql='''
    #     ALTER TABLE `cs2305.Dept` DROP FOREIGN KEY `cs2305.dept_ibfk_1`;
    #     ALTER TABLE `cs2305.Dept` DROP FOREIGN KEY `cs2305.dept_ibfk_2`;
    #     ALTER TABLE `cs2305.Doctor` DROP FOREIGN KEY `cs2305.doctor_ibfk_1`;
    #     ALTER TABLE `cs2305.Doctor` DROP FOREIGN KEY `cs2305.doctor_ibfk_2`;
    #     ALTER TABLE `cs2305.Title` DROP FOREIGN KEY `cs2305.title_ibfk_1`;
    #     ALTER TABLE `cs2305.Godown_Slave` DROP FOREIGN KEY `cs2305.godown_slave_ibfk_1`;
    #     ALTER TABLE `cs2305.Godown_Slave` DROP FOREIGN KEY `cs2305.godown_slave_ibfk_2`;
    #     ALTER TABLE `cs2305.Medicine` DROP FOREIGN KEY `cs2305.medicine_ibfk_1`;
    #     ALTER TABLE `cs2305.Diagnosis` DROP FOREIGN KEY `cs2305.diagnosis_ibfk_1`;
    #     ALTER TABLE `cs2305.Diagnosis` DROP FOREIGN KEY `cs2305.diagnosis_ibfk_2`;
    #     ALTER TABLE `cs2305.Recipe_Master` DROP FOREIGN KEY `cs2305.recipe_master_ibfk_1`;
    #     ALTER TABLE `cs2305.Recipe_Master` DROP FOREIGN KEY `cs2305.recipe_master_ibfk_2`;
    #     ALTER TABLE `cs2305.Recipe_Master` DROP FOREIGN KEY `cs2305.recipe_master_ibfk_3`;
    #     ALTER TABLE `cs2305.Recipe_Detail` DROP FOREIGN KEY `cs2305.recipe_detail_ibfk_1`;
    #     ALTER TABLE `cs2305.Recipe_Detail` DROP FOREIGN KEY `cs2305.recipe_detail_ibfk_2`;
    #     ALTER TABLE `cs2305.Register_Form` DROP FOREIGN KEY `cs2305.register_form_ibfk_1`;
    #     ALTER TABLE `cs2305.Register_Form` DROP FOREIGN KEY `cs2305.register_form_ibfk_2`;
    #     ALTER TABLE `cs2305.Register_Form` DROP FOREIGN KEY `cs2305.register_form_ibfk_3`;
    #     ALTER TABLE `cs2305.Register_Form` DROP FOREIGN KEY `cs2305.register_form_ibfk_4`;
    #     ALTER TABLE `cs2305.Fee` DROP FOREIGN KEY `cs2305.fee_ibfk_1`;
    #     ALTER TABLE `cs2305.Fee` DROP FOREIGN KEY `cs2305.fee_ibfk_2`;
    #     ALTER TABLE `cs2305.Fee` DROP FOREIGN KEY `cs2305.fee_ibfk_3`;
    #     ALTER TABLE `cs2305.Fee` DROP FOREIGN KEY `cs2305.fee_ibfk_4`;
    #     '''
    #     print(self.execute(sql))
    #     sql='''
    #     SHOW TABLES
    #     '''
    #     self.execute(sql)
    #     tables = self.cursor.fetchall()
    #     print(tables)
    #     for table in tables:
    #         sql=f"DROP TABLE IF EXISTS {table[0]}"
    #         print(self.execute(sql))
        

# import pymysql
# from pymysql.constants import CLIENT
# class DataBase():
#  def __init__(self):
#  self.conn = pymysql.connect(
#  host=host,
#  port = 3306, 
#  user="root",
#  password=pwd,
#  database="a.his",
#  charset="utf8",
#  client_flag=CLIENT.MULTI_STATEMENTS
#  )
#  self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
#  def execute(self,sql, params=None):
#  try: 
#  self.cursor.execute(sql,params)
#  self.conn.commit()
#  except:
#  self.conn.rollback()
#  ret = self.cursor.fetchall()
#  self.cursor.close()
#  self.conn.close()
#  return ret
#  def getTable(self,table):
#  sql=f"SELECT * FROM {table}"
#  return self.execute(sql)
#  def update(self,table,id,col,value):
#  sql = f"SELECT {col} FROM {table} WHERE id = %s"
#  res = self.execute(sql, (id,))
#  if res is not None and res[0] == value:
#  return
#  else:
#  sql = f"UPDATE {table} SET {col} = %s WHERE id = %s"
#  self.cursor.execute(sql,(value,id))
#  return