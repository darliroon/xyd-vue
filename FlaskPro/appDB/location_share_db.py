import pymysql
from flask import jsonify
import json

class Location_share_db:
    def __init__(self, host='rm-j6c1pi4d3j4u787x3mo.mysql.rds.aliyuncs.com', user='thl_admin', password="Ll5028852", db="xydinfo"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self. conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self. cursor = self.conn.cursor()

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def location_upload(self, _source_name, _id, _psx, _psy, _psz):
        sql = "SELECT userId FROM locationshare"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (goal,) in res:
            if goal == _id:
                update_sql = "UPDATE locationshare SET sourceName = %s,psx = %s,psy = %s,psz = %s WHERE userId = %s"
                self.cursor.execute(update_sql, [_source_name, _psx, _psy, _psz, _id])
                self.conn.commit()
                return 1
        insert_sql = "INSERT INTO locationshare VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(insert_sql, [_source_name, _id, _psx, _psy, _psz])
        self.conn.commit()
        return 2

    def location_delete(self, user_id):
        sql = "SELECT userId FROM locationshare"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (goal,) in res:
            if goal == user_id:
                delete_sql = "DELETE FROM locationshare WHERE userId = %s"
                self.cursor.execute(delete_sql, [user_id])
                self.conn.commit()
                return 0
        return -1

    def location_delete_all(self):
        try:
            drop_sql = "DROP TABLE locationshare"
            self.cursor.execute(drop_sql)
            self.conn.commit()
            new_sql = "create table locationshare(sourceName text, userId text, psx int, psy int, psz int)"
            self.cursor.execute(new_sql)
            self.conn.commit()
            return 0
        except Exception as e:
            print("When location delete all, an exception occurred!")
            print(e)

    def location_get_all(self, spe_sour):
        get_sql = "SELECT * FROM locationshare"
        try:
            self.cursor.execute(get_sql)
            res = self.cursor.fetchall()
            json_dict_list = []
            for (_source, _id, _psx, _psy, _psz) in res:
                if _source == spe_sour:
                    json_dict = {
                        'sourceName': _source,
                        'userId': _id,
                        'psx': _psx,
                        'psy': _psy,
                        'psz': _psz
                    }
                    json_dict_list.append(json_dict)
            return json.dumps(json_dict_list)

        except Exception as e:
            print("When get all shared location: something wrong occurred!")
            print(e)
            return "-3"




