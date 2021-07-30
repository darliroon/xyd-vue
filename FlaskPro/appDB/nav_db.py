import pymysql
from flask import jsonify

class NavfDB:
    def __init__(self, host='rm-j6c1pi4d3j4u787x3mo.mysql.rds.aliyuncs.com', user='thl_admin', password="Ll5028852", db="xydnav", table="siyusiyu"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self.cursor = self.conn.cursor()
        self.table = table

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def add_new_nav_info(self, x1, y1, z1, x2, y2, z2):
        sql = "INSERT INTO {} VALUES(%s, %s, %s, %s, %s, %s)".format(self.table)
        try:
            self.cursor.execute(sql, [x1, y1, z1, x2, y2, z2])
            self.conn.commit()
            return 0
        except Exception as e:
            print(e)
            print("When add new nav info, something wrong occurred!")
            return -3

    def delete_nav_info(self, x1, y1, z1, x2, y2, z2):
        sql = "SELECT x1,y1,z1,x2,y2,z2 FROM {}".format(self.table)
        delete_sql = "DELETE FROM {} WHERE x1 = %s and y1 = %s and z1 = %s and x2 = %s and y2 = %s and z2 = %s".format(self.table)
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for (_x1, _y1, _z1, _x2, _y2, _z2) in res:
                if _x1 == x1 and _y1 == y1 and _z1 == z1 and _x2 == x2 and _y2 == y2 and _z2 == z2:
                    self.cursor.execute(delete_sql, [x1, y1, z1, x2, y2, z2])
                    self.conn.commit()
                    return 0
            return -1
        except Exception as e:
            print(e)
            print("When delete nav info, something wrong occurred!")
            return -3















