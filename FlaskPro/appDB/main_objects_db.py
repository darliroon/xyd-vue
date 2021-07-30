import pymysql
from flask import jsonify
import requests
import random, string


def get_ten_random ():
    rand_str = ""
    num = string.ascii_letters+string.digits
    for i in range(10):
        rand_str += random.choice(num)
    return rand_str


def list_to_str(the_list: list):
    return ','.join([str(x) for x in the_list])


def str_to_list(the_str: str):
    return [str(i) for i in (the_str.split(','))]


class MainObjectsDB:
    def __init__(self, host='rm-j6c1pi4d3j4u787x3mo.mysql.rds.aliyuncs.com', user='thl_admin', password="Ll5028852", db="xydobjects", table="siyusiyu"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self. conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self. cursor = self.conn.cursor()
        self.table = table

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def create_new_object(self, object_name):
        sql = "SELECT name FROM {}".format(self.table)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_name,) in res:
            if _name == object_name:
                return -1
        create_sql = "INSERT INTO {} VALUES (%s, '', 0, '', '', '', '0')".format(self.table)
        self.cursor.execute(create_sql, [object_name])
        self.conn.commit()
        return 0

    def update_specific_object_name(self, old_name, new_name):
        sql = "SELECT name FROM {}".format(self.table)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_name,) in res:
            if _name == old_name:
                update_sql = "UPDATE {} SET name = %s WHERE name = %s".format(self.table)
                self.cursor.execute(update_sql, [new_name, old_name])
                self.conn.commit()
                return 0
        return -1

    def update_specific_object_coordinate(self, object_name, new_coordinate):
        sql = "SELECT name FROM {}".format(self.table)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_name,) in res:
            if _name == object_name:
                update_sql = "UPDATE {} SET coordinate = %s WHERE name = %s".format(self.table)
                self.cursor.execute(update_sql, [new_coordinate, object_name])
                self.conn.commit()
                return 0
        return -1

    def update_specific_object_label(self, object_name, new_label:int):
        sql = "SELECT name FROM {}".format(self.table)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_name,) in res:
            if _name == object_name:
                update_sql = "UPDATE {} SET label = %s WHERE name = %s".format(self.table)
                self.cursor.execute(update_sql, [new_label, object_name])
                self.conn.commit()
                return 0
        return -1

    def update_specific_object_img(self, object_name, img_data):
        sql = "SELECT name FROM {}".format(self.table)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_name,) in res:
            if _name == object_name:
                update_sql = "UPDATE {} SET img = %s WHERE name = %s".format(self.table)
                self.cursor.execute(update_sql, [img_data, object_name])
                self.conn.commit()
                update_sql2 = "UPDATE {} SET img_url = %s WHERE name = %s".format(self.table)
                self.cursor.execute(update_sql2, [get_ten_random(), object_name])
                self.conn.commit()
                return 0
        return -1

    def get_object_img(self, object_name):
        sql = "SELECT name,img FROM {}".format(self.table)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_name, img) in res:
            if _name == object_name:
                return img
        return -1

    def update_object_details(self, object_name, detail):
        sql = "SELECT name FROM {}".format(self.table)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_name,) in res:
            if _name == object_name:
                update_sql = "UPDATE {} SET details = %s WHERE name = %s".format(self.table)
                self.cursor.execute(update_sql, [detail, object_name])
                self.conn.commit()
                return 0
        return -1

    def update_object_comments(self, object_name, new_comment):
        sql = "SELECT name FROM {}".format(self.table)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_name,) in res:
            if _name == object_name:
                update_sql = "UPDATE {} SET comments = %s WHERE name = %s".format(self.table)
                self.cursor.execute(update_sql, [new_comment, object_name])
                self.conn.commit()
                return 0
        return -1

    def add_object_comment(self, object_name, add_comment):
        sql = "SELECT name,comments FROM {}".format(self.table)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_name, _comments) in res:
            if _name == object_name:
                if _comments == "0":
                    update_sql = "UPDATE {} SET comments = %s WHERE name = %s".format(self.table)
                    self.cursor.execute(update_sql, [add_comment, object_name])
                    self.conn.commit()
                else:
                    comments_list = str_to_list(_comments)
                    comments_list.append(add_comment)
                    new_comments_str = list_to_str(comments_list)
                    update_sql = "UPDATE {} SET comments = %s WHERE name = %s".format(self.table)
                    self.cursor.execute(update_sql, [new_comments_str, object_name])
                    self.conn.commit()
                return 0
        return -1

    """ 开发者端接口"""
    def delete_object_all_comments(self, object_name):
        sql = "SELECT name FROM {}".format(self.table)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_name,) in res:
            if _name == object_name:
                update_sql = "UPDATE {} SET comments = %s WHERE name = %s".format(self.table)
                self.cursor.execute(update_sql, ['0', object_name])
                self.conn.commit()
                return 0
        return -1

    def delete_specific_comment(self, object_name, comments_content):
        sql = "SELECT name,comments FROM {}".format(self.table)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_name, _comments) in res:
            if _name == object_name:
                comments_list = str_to_list(_comments)
                for _single_comment in comments_list:
                    if _single_comment == comments_content:
                        comments_list.remove(comments_content)
                        if len(comments_list) == 0:
                            update_sql = "UPDATE {} SET comments = %s WHERE name = %s".format(self.table)
                            self.cursor.execute(update_sql, ['0', object_name])
                            self.conn.commit()
                        else :
                            new_comments_str = list_to_str(comments_list)
                            update_sql = "UPDATE {} SET comments = %s WHERE name = %s".format(self.table)
                            self.cursor.execute(update_sql, [new_comments_str, object_name])
                            self.conn.commit()
                        return 0
                return 2
        return -1

    def get_all_comments(self, object_name):
        sql = "SELECT name,comments FROM {}".format(self.table)
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_name, _comments) in res:
            if _name == object_name:
                return _comments
        return "-1"

    # def add_object(self, name, coordinate, label, img, details, comments):
    #     sql = "SELECT name FROM mainobjectinfo"
    #     self.cursor.execute(sql)
    #     res = self.cursor.fetchall()
    #     flag = 0
    #     #查重
    #     for (_name,) in res:
    #         if _name == name:
    #             flag = 1
    #     if flag == 1:
    #         return -1
    #
    #     #没有重复名
    #     add_object_sql = "INSERT INTO mainobjectinfo VALUES (%s, %s, %s, %s, %s, %s)"
    #     self.cursor.execute(add_object_sql, [name, coordinate, label, img, details, comments])
    #     self.conn.commit()
    #     return 0