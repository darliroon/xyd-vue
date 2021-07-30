import json

import pymysql
from flask import jsonify

class NewObjectTable:
    def __init__(self, host='rm-j6c1pi4d3j4u787x3mo.mysql.rds.aliyuncs.com', user='thl_admin', password="Ll5028852", db="xydinfo", db2="xydobjects"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.db2 = db2

        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self.cursor = self.conn.cursor()

        self.conn2 = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db2)
        self.cursor2 = self.conn2.cursor()

    def close_db(self):
        self.cursor.close()
        self.conn.close()

        self.cursor2.close()
        self.conn2.close()

    def create_new_table(self, new_table_name, create_sql):
        sql = "SELECT name FROM mainobjecttableinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_name,) in res:
            if _name == new_table_name:
                return -1
        try:
            self.cursor2.execute(create_sql)
            self.conn2.commit()
            insert_sql = "INSERT INTO mainobjecttableinfo VALUES (%s)"
            self.cursor.execute(insert_sql, [new_table_name])
            self.conn.commit()
            return 0
        except Exception as e:
            return -3

    def drop_the_table(self, table_name):
        sql = "SELECT name FROM mainobjecttableinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_name,) in res:
            if _name == table_name:
                try:
                    delete_sql = "DELETE FROM mainobjecttableinfo WHERE name = %s"
                    self.cursor.execute('SET SQL_SAFE_UPDATES = 0')
                    self.cursor.execute(delete_sql, [table_name])
                    self.conn.commit()
                    drop_sql = "DROP TABLE {}".format(table_name)
                    self.cursor2.execute(drop_sql)
                    self.conn2.commit()
                    return 0
                except Exception as e:
                    return -3
        return -1

    def get_all_holds(self):
        sql = "SELECT name FROM mainobjecttableinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return json.dumps(res)


