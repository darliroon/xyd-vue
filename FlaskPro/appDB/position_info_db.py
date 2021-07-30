import pymysql
from flask import jsonify

def list_to_str(the_list: list):
    return ','.join([str(x) for x in the_list])


def str_to_list(the_str: str):
    return [str(i) for i in (the_str.split(','))]

class PositionDB:
    def __init__(self, host='rm-j6c1pi4d3j4u787x3mo.mysql.rds.aliyuncs.com', user='thl_admin', password="Ll5028852", db="xydposition", psition="siyusiyu"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self. conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self. cursor = self.conn.cursor()
        self.psition = psition

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def create_new_position(self, _psx: int, _psy: int, _psz: int, _id1: str, _ap1: int, _id2: str, _ap2: int, _id3: str, _ap3: int, _id4: str, _ap4: int, _id5: str, _ap5: int,
                            _id6: str, _ap6: int, _id7: str, _ap7: int, _id8: str, _ap8: int, _id9: str, _ap9: int, _id10: str, _ap10: int):
        pre_sql = "SELECT psx,psy,psz FROM {}".format(self.psition)
        self.cursor.execute(pre_sql)
        res = self.cursor.fetchall()
        for (x, y, z) in res:
            if x == _psx and y == _psy and z == _psz:
                return -1
        create_sql = "INSERT INTO {} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(self.psition)
        self.cursor.execute(create_sql, [_psx, _psy, _psz, _id1, _ap1, _id2, _ap2, _id3, _ap3, _id4, _ap4, _id5, _ap5,
                                         _id6, _ap6, _id7, _ap7, _id8, _ap8, _id9, _ap9, _id10, _ap10])
        # sql = "INSERT INTO positioninfo VALUES ({}, {}, {}, {}, {})"
        self.conn.commit()
        return 0

    def delete_spe_position(self, _psx: int, _psy: int, _psz: int):
        sql = "SELECT psx,psy,psz FROM {}".format(self.psition)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (x, y, z) in res:
            if x == _psx and y == _psy and z == _psz:
                delete_sql = "DELETE FROM {} WHERE psx = %s and psy = %s and psz = %s".format(self.psition)
                self.cursor.execute(delete_sql, [_psx, _psy, _psz])
                self.conn.commit()
                return 0
        return -1

    def get_latest_position_info(self):
        sql = "SELECT psx,psy,psz,id1,ap1,id2,ap2,id3,ap3,id4,ap4,id5,ap5,id6,ap6,id7,ap7,id8,ap8,id9,ap9,id10,ap10 " \
              "FROM {}".format(self.psition)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        json_dict = {

        }
        for (x, y, z, id_1, ap_1, id_2, ap_2, id_3, ap_3, id_4, ap_4, id_5, ap_5, id_6, ap_6, id_7, ap_7, id_8, ap_8, id_9, ap_9, id_10, ap_10) in res:
            key_str = str(x) + ',' + str(y) + ',' + str(z)
            json_dict[key_str] = {
                id_1: ap_1,
                id_2: ap_2,
                id_3: ap_3,
                id_4: ap_4,
                id_5: ap_5,
                id_6: ap_6,
                id_7: ap_7,
                id_8: ap_8,
                id_9: ap_9,
                id_10: ap_10
            }
        return jsonify(json_dict)
        # sql = "DELETE FROM positioninfo WHERE psx = %s and psy = %s"
        # self.cursor.execute(sql, [_psx, _psy])
        # self.conn.commit()
        # return 0
