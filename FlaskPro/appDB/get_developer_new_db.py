import io

import pymysql
from flask import jsonify, send_file
import json


class GetDeveloperNewFingersDB:
    def __init__(self, host='rm-j6c1pi4d3j4u787x3mo.mysql.rds.aliyuncs.com', user='thl_admin', password="Ll5028852", db="xydposition"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self. conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self. cursor = self.conn.cursor()

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def get_developer_new_fingers(self, table_name):
        sql = "SELECT * FROM {}".format(table_name)
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            json_dict = {

            }
            for (_psx, _psy, _psz, _id1, _ap1, _id2, _ap2, _id3, _ap3, _id4, _ap4, _id5, _ap5,
                                         _id6, _ap6, _id7, _ap7, _id8, _ap8, _id9, _ap9, _id10, _ap10) in res:
                key_str = str(_psx) + ',' + str(_psy) + ',' + str(_psz)
                json_dict[key_str] = {
                    _id1: _ap1,
                    _id2: _ap2,
                    _id3: _ap3,
                    _id4: _ap4,
                    _id5: _ap5,
                    _id6: _ap6,
                    _id7: _ap7,
                    _id8: _ap8,
                    _id9: _ap9,
                    _id10: _ap10
                }
            return jsonify(json_dict)
        except Exception as e:
            print("When get developer fingers infos some wrong occurred!")
            print(e)
            return "-5"


    def get_developer_new_fingers_for_developer(self, table_name):
        sql = "SELECT * FROM {}".format(table_name)
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            json_dict_list = []
            for (_psx, _psy, _psz, _id1, _ap1, _id2, _ap2, _id3, _ap3, _id4, _ap4, _id5, _ap5,
                                         _id6, _ap6, _id7, _ap7, _id8, _ap8, _id9, _ap9, _id10, _ap10) in res:
                # key_str = str(_psx) + ',' + str(_psy) + ',' + str(_psz)
                json_dict = {
                    'psx': _psx,
                    'psy': _psy,
                    'psz': _psz,
                    'id1': _id1,
                    'ap1': _ap1,
                    'id2': _id2,
                    'ap2': _ap2,
                    'id3': _id3,
                    'ap3': _ap3,
                    'id4': _id4,
                    'ap4': _ap4,
                    'id5': _id5,
                    'ap5': _ap5,
                    'id6': _id6,
                    'ap6': _ap6,
                    'id7': _id7,
                    'ap7': _ap7,
                    'id8': _id8,
                    'ap8': _ap8,
                    'id9': _id9,
                    'ap9': _ap9,
                    'id10': _id10,
                    'ap10': _ap10
                }
                json_dict_list.append(json_dict)
            return jsonify(json_dict_list)
        except Exception as e:
            print("When get developer fingers infos some wrong occurred!")
            print(e)
            return "-5"

    def get_developer_new_fingers_for_developer_json(self, table_name):
        sql = "SELECT * FROM {}".format(table_name)
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            json_dict_list = []
            for (_psx, _psy, _psz, _id1, _ap1, _id2, _ap2, _id3, _ap3, _id4, _ap4, _id5, _ap5,
                                         _id6, _ap6, _id7, _ap7, _id8, _ap8, _id9, _ap9, _id10, _ap10) in res:
                # key_str = str(_psx) + ',' + str(_psy) + ',' + str(_psz)
                json_dict = {
                    'psx': _psx,
                    'psy': _psy,
                    'psz': _psz,
                    'id1': _id1,
                    'ap1': _ap1,
                    'id2': _id2,
                    'ap2': _ap2,
                    'id3': _id3,
                    'ap3': _ap3,
                    'id4': _id4,
                    'ap4': _ap4,
                    'id5': _id5,
                    'ap5': _ap5,
                    'id6': _id6,
                    'ap6': _ap6,
                    'id7': _id7,
                    'ap7': _ap7,
                    'id8': _id8,
                    'ap8': _ap8,
                    'id9': _id9,
                    'ap9': _ap9,
                    'id10': _id10,
                    'ap10': _ap10
                }
                json_dict_list.append(json_dict)
            return send_file(io.BytesIO(json.dumps(json_dict_list).encode()), attachment_filename='jsonData')
        except Exception as e:
            print("When get developer fingers infos some wrong occurred!")
            print(e)
            return "-5"


class GetDeveloperNewObjectsDB:
    def __init__(self, host='rm-j6c1pi4d3j4u787x3mo.mysql.rds.aliyuncs.com', user='thl_admin', password="Ll5028852", db="xydobjects"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self. conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self. cursor = self.conn.cursor()

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def get_developer_new_objects(self, table_name):
        sql = "SELECT name,coordinate,label,img_url,details,comments FROM {}".format(table_name)
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            json_dict_list = []
            for (_name, _coordinate, _label, _img_url, _details, _comments) in res:
                json_dict = {
                    'name': _name,
                    'coordinate': _coordinate,
                    'label': _label,
                    'img': _img_url,
                    'details': _details,
                    'comments': _comments
                }
                json_dict_list.append(json_dict)
            return json.dumps(json_dict_list)
        except Exception as e:
            print("Exception when get developer new objects")
            print(e)
            return "-3"

    def get_developer_new_objects_simply(self, table_name):
        sql = "SELECT name,coordinate FROM {}".format(table_name)
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            json_dict_list = []
            for (_name, _coordinate) in res:
                json_dict = {
                    'name': _name,
                    'coordinate': _coordinate
                }
                json_dict_list.append(json_dict)
            return json.dumps(json_dict_list)
        except Exception as e:
            print("Exception occurred when get developer new objects simply")
            print(e)
            return "-3"

    def get_developer_object_img_from_url(self, table_name, i_url):
        sql = "SELECT img,img_url FROM {}".format(table_name)
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for (_img, _img_url) in res:
                if _img_url == i_url:
                    return _img
            return -1
        except Exception as e:
            return -3


class GetDeveloperNewImgDB:
    def __init__(self, host='rm-j6c1pi4d3j4u787x3mo.mysql.rds.aliyuncs.com', user='thl_admin', password="Ll5028852", db="xydimage"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self. conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self. cursor = self.conn.cursor()

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def get_developer_img_img(self, table_name):
        sql = "SELECT img FROM {}".format(table_name)
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            return res[0][0]
        except Exception as e:
            return -3


class GetDeveloperNavsDB:
    def __init__(self, host='rm-j6c1pi4d3j4u787x3mo.mysql.rds.aliyuncs.com', user='thl_admin', password="Ll5028852", db="xydnav"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self. conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self. cursor = self.conn.cursor()

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def get_developer_new_navs(self, table_name):
        sql = "SELECT * FROM {}".format(table_name)
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            json_dict_list = []
            for (_x1, _y1, _z1, _x2, _y2, _z2) in res:
                json_dict = {
                    'x1': _x1,
                    'y1': _y1,
                    'z1': _z1,
                    'x2': _x2,
                    'y2': _y2,
                    'z2': _z2
                }
                json_dict_list.append(json_dict)
            return json.dumps(json_dict_list)
        except Exception as e:
            print("When get developer navs infos some wrong occurred!")
            print(e)
            return "-5"

