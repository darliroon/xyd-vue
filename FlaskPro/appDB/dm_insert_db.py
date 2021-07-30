import random
import string

import pymysql
import requests


def get_ten_random():
    rand_str = ""
    num = string.ascii_letters+string.digits
    for i in range(10):
        rand_str += random.choice(num)
    return rand_str


class InsertFingerDB:
    def __init__(self, host='rm-j6c1pi4d3j4u787x3mo.mysql.rds.aliyuncs.com', user='thl_admin', password="Ll5028852",
                 db="xydposition"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self.cursor = self.conn.cursor()

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def insert_many_finger_info(self, table_name, json_list):
        sql = "INSERT INTO {} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(table_name)
        try:
            for each_dict in json_list:
                self.cursor.execute(sql, [each_dict['psx'], each_dict['psy'], each_dict['psz'], each_dict['id1'],
                                          each_dict['ap1'], each_dict['id2'], each_dict['ap2'], each_dict['id3'],
                                          each_dict['ap3'], each_dict['id4'], each_dict['ap4'], each_dict['id5'],
                                          each_dict['ap5'], each_dict['id6'], each_dict['ap6'], each_dict['id7'],
                                          each_dict['ap7'], each_dict['id8'], each_dict['ap8'], each_dict['id9'],
                                          each_dict['ap9'], each_dict['id10'], each_dict['ap10']])
            self.conn.commit()
            return 0
        except Exception as e:
            print("When insert many finger info, exception occurred!")
            print(e)
            return -3


class InsertObjectDB:
    def __init__(self, host='rm-j6c1pi4d3j4u787x3mo.mysql.rds.aliyuncs.com', user='thl_admin', password="Ll5028852",
                 db="xydobjects"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self.cursor = self.conn.cursor()

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def insert_many_objects_info(self, table_name, json_list):
        sql = "INSERT INTO {} VALUES (%s, %s, %s, %s, %s, %s, %s)".format(table_name)
        try:
            for each_dict in json_list:
                _name = each_dict['name']
                _coordinatex = each_dict['coordinatex']
                _coordinatey = each_dict['coordinatey']
                _coordinatez = each_dict['coordinatez']
                _coordinate = _coordinatex + '&' + _coordinatey + '&' + _coordinatez
                _label = each_dict['label']
                _img_url = each_dict['img_url']
                _details = each_dict['details']
                _comments = each_dict['comments']
                binary_data = requests.get(_img_url)
                binary_data_content = binary_data.content
                self.cursor.execute(sql, [_name, _coordinate, _label, binary_data_content, get_ten_random(), _details, _comments])
            self.conn.commit()
            return 0
        except Exception as e:
            print("When insert many objects info, exception occurred!")
            print(e)
            return -3


class InsertNavDB:
    def __init__(self, host='rm-j6c1pi4d3j4u787x3mo.mysql.rds.aliyuncs.com', user='thl_admin', password="Ll5028852",
                 db="xydnav"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self.cursor = self.conn.cursor()

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def insert_many_nav_info(self, table_name, json_list):
        sql = "INSERT INTO {} VALUES (%s, %s, %s, %s, %s, %s)".format(table_name)
        try:
            for each_dict in json_list:
                self.cursor.execute(sql, [each_dict['x1'], each_dict['y1'], each_dict['z1'], each_dict['x2'],
                                          each_dict['y2'], each_dict['z2']])
            self.conn.commit()
            return 0
        except Exception as e:
            print("When insert many nav info, exception occurred!")
            print(e)
            return -3


