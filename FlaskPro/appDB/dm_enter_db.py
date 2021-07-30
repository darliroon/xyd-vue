import pymysql
from flask import jsonify

def list_to_str(the_list: list):
    return ','.join([str(x) for x in the_list])


def str_to_list(the_str: str):
    return [str(i) for i in (the_str.split(','))]

class DMRegister_db:
    def __init__(self, host='rm-j6c1pi4d3j4u787x3mo.mysql.rds.aliyuncs.com', user='thl_admin', password="Ll5028852",
                 db="xydinfo"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
        self.cursor = self.conn.cursor()

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def dm_register(self, user_id, password):
        sql = "SELECT id FROM dmregisterinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_id,) in res:
            if _id == user_id:
                return -1
        create_sql = "INSERT INTO dmregisterinfo VALUES (%s, %s, '0')"
        self.cursor.execute(create_sql, [user_id, password])
        self.conn.commit()
        return 0

    def dm_log_in(self, user_id, password):
        sql = "SELECT id,password FROM dmregisterinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_id, _password) in res:
            if _id == user_id and _password == password:
                return 1
        return -1

    def add_hold(self, user_id, new_hold):
        sql = "SELECT id,hold FROM dmregisterinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_id, _hold) in res:
            if _id == user_id:
                if _hold == "0":
                    add_sql = "UPDATE dmregisterinfo SET hold = %s WHERE id = %s"
                    self.cursor.execute(add_sql, [new_hold, user_id])
                    self.conn.commit()
                else:
                    hold_list = str_to_list(_hold)
                    hold_list.append(new_hold)
                    new_hold_str = list_to_str(hold_list)
                    add_sql = "UPDATE dmregisterinfo SET hold = %s WHERE id = %s"
                    self.cursor.execute(add_sql, [new_hold_str, user_id])
                    self.conn.commit()
                return 0
        return -1


    def get_hold(self, user_id):
        sql = "SELECT id,hold FROM dmregisterinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_id, _hold) in res:
            if _id == user_id:
                return _hold
        return "-1"

    def remove_hold(self, user_id, spe_hold):
        sql = "SELECT id,hold FROM dmregisterinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_id, _hold) in res:
            if _id == user_id:
                hold_list = str_to_list(_hold)
                for a_hold in hold_list:
                    if a_hold == spe_hold:
                        hold_list.remove(spe_hold)
                        if len(hold_list) == 0:
                            update_sql = "UPDATE dmregisterinfo SET hold = %s WHERE  id = %s"
                            self.cursor.execute(update_sql, ['0', user_id])
                            self.conn.commit()
                        else:
                            hold_list_str = list_to_str(hold_list)
                            update_sql = "UPDATE dmregisterinfo SET hold = %s WHERE id = %s"
                            self.cursor.execute(update_sql, [hold_list_str, user_id])
                            self.conn.commit()
                        return 0
                return -2
        return -1








