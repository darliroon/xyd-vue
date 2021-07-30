import pymysql
from flask import jsonify


def list_to_str(the_list: list):
    return '&'.join([str(x) for x in the_list])


def str_to_list(the_str: str):
    return [str(i) for i in (the_str.split('&'))]


class CharDB:
    def __init__(self, host='rm-j6c1pi4d3j4u787x3mo.mysql.rds.aliyuncs.com', user='thl_admin', password="Ll5028852", db="xydchat"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self. conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self. cursor = self.conn.cursor()

    def close_db(self):
        self.cursor.close()
        self.conn.close()


    def post_info_to_receiver(self, poster, receiver, info):
        search_sql = "SELECT receiver,poster,info FROM chatbuffer"
        self.cursor.execute(search_sql)
        res = self.cursor.fetchall()
        for (_rec, _poster, _info) in res:
            if _rec == receiver:
                poster_list = str_to_list(_poster)
                poster_list.append(poster)
                new_poster_str = list_to_str(poster_list)
                info_list = str_to_list(_info)
                info_list.append(info)
                new_info_str = list_to_str(info_list)
                update_sql = "UPDATE chatbuffer SET poster = %s,info = %s WHERE receiver = %s"
                try:
                    self.cursor.execute(update_sql, [new_poster_str, new_info_str, receiver])
                    self.conn.commit()
                    return 0   #当前已有缓冲的receiver数据
                except Exception as e:
                    print("When find the receiver and add something , exception occurred!")
                    print(e)
                    return -3  #出现异常
        insert_sql = "INSERT INTO chatbuffer VALUES (%s, %s, %s)"
        try:
            self.cursor.execute(insert_sql, [receiver, poster, info])
            self.conn.commit()
            return 1   # 正常 创建一条数据
        except Exception as e:
            print("When not find the receiver and insert it , exception occurred!")
            print(e)
            return -4  #出现 异常

    def get_info_from_all_posters(self, receiver):
        sql = "SELECT receiver,poster,info FROM chatbuffer"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        json_data = {

        }
        for (_res, _poster, _info) in res:
            if _res == receiver:
                json_data['poster'] = _poster
                json_data['info'] = _info
                return json_data
        return "-1"

    def get_spe_poster_info(self, recevier_name, poster_name):
        sql = "SELECT receiver,poster,info FROM chatbuffer"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_res, _poster, _info) in res:
            if _res == recevier_name:
                poster_list = str_to_list(_poster)
                info_list = str_to_list(_info)
                poster_list_length = len(poster_list)
                result_list = []
                for i in range(poster_list_length):
                    if poster_list[i] == poster_name:
                        result_list.append(info_list[i])
                for re in result_list:
                    poster_list.remove(poster_name)
                    info_list.remove(re)
                if len(poster_list) == 0:
                    delete_sql = "DELETE FROM chatbuffer WHERE receiver = %s"
                    self.cursor.execute(delete_sql, [recevier_name])
                    self.conn.commit()
                else:
                    update_sql = "UPDATE chatbuffer SET poster = %s,info = %s WHERE receiver = %s"
                    self.cursor.execute(update_sql, [list_to_str(poster_list), list_to_str(info_list), recevier_name])
                    self.conn.commit()
                return list_to_str(result_list)
        return "-1"


