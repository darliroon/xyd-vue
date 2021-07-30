import pymysql
from flask import jsonify

class DbOpera:
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

    def register(self, userId, password, email, phone, gender, age, face, sign):
        sql = "SELECT userId FROM registerinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (goal,) in res:
            print(goal)
            if goal == userId:
                print("Same User ID")
                return -1
        #向数据库中插入信息
        insert_sql = "INSERT INTO registerinfo VALUES('{}','{}','{}','{}', {}, {}, {}, '{}')".format(userId, password, email, phone, gender, age, face, sign)
        print(insert_sql)
        self.cursor.execute(insert_sql)
        self.conn.commit()
        update_sql = "INSERT INTO friendsinfo VALUES ('{}', 0, '0')".format(userId)
        print(update_sql)
        self.cursor.execute(update_sql)
        self.conn.commit()
        return 0

    def total_modify(self, old_id, new_id, new_el, new_pe, new_gd, new_ag, new_fc, new_sg):
        sql = "SELECT userId FROM registerinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        flag = 0
        for (id,) in res:
            if id == new_id:
                return -2  #出现重复
            if id == old_id:
                flag = 1
        if flag == 0: #没有找到了旧id
            return -1

        modify_sql_all = "UPDATE registerinfo SET userId = '{}',email = '{}',phone = '{}',gender = {}, age = {}, face = {}, " \
                        "sign = '{}' WHERE userId = '{}'".format(new_id, new_el, new_pe, new_gd, new_ag, new_fc, new_sg, old_id)
        self.cursor.execute(modify_sql_all)
        self.conn.commit()
        return 0

    def log_in(self, userId, password):
        sql = "SELECT userId,password,email,phone,gender,age,face,sign FROM registerinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (id, pw, el, po, gd, ag, fc,sg) in res:
            if id == userId and pw == password:
                json_dict = {
                    "userId" : id,
                    "password" : pw,
                    "email" : el,
                    "phone" : po,
                    "gender" : gd,
                    "age" : ag,
                    "face" : fc,
                    "sign" : sg
                }
                return jsonify(json_dict)
        return "-1"

    def modify_user_id(self, old_value, new_value):
        sql = "SELECT userId FROM registerinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        flag = 0
        for (id,) in res:
            if id == new_value:
                return -2  #出现重复
            if id == old_value:
                flag = 1
        if flag == 0: #没有找到了旧id
            return -1

        modify_sql = "UPDATE registerinfo SET userId = '{}' WHERE userId = '{}'".format(new_value, old_value)
        # print(modify_sql)
        self.cursor.execute(modify_sql)
        self.conn.commit()
        return 0

    def modify_user_password(self, user_id, old_value, new_value):
        sql = "SELECT userId,password FROM registerinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        flag = 0
        for (id, pw) in res:
            if id == user_id and pw == old_value:
                flag = 1
                break
        if flag == 0:
            return -1
        modify_sql = "UPDATE registerinfo SET password = '{}' WHERE userId = '{}'".format(new_value, user_id)
        self.cursor.execute(modify_sql)
        self.conn.commit()
        return 0

    # def modify_user_

    def modify_user_email(self, user_id, new_value):
        sql = "SELECT userId FROM registerinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        flag = 0
        for (id,) in res:
            if id == user_id:
                flag = 1
                break
        if flag == 0:  #没有找到
            return -1

        modify_sql = "UPDATE registerinfo SET email = '{}' WHERE userId = '{}'".format(new_value, user_id)
        self.cursor.execute(modify_sql)
        self.conn.commit()
        return 0

    def modify_user_phone(self, user_id, new_value):
        sql = "SELECT userId FROM registerinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        flag = 0
        for (id,) in res:
            if id == user_id:
                flag = 1
                break
        if flag == 0:  #没有找到
            return -1

        modify_sql = "UPDATE registerinfo SET phone = '{}' WHERE userId = '{}'".format(new_value, user_id)
        self.cursor.execute(modify_sql)
        self.conn.commit()
        return 0

    def modify_user_gender(self, user_id, new_value: int):
        sql = "SELECT userId FROM registerinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        flag = 0
        for (id,) in res:
            if id == user_id:
                flag = 1
                break
        if flag == 0:  #没有找到
            return -1

        modify_sql = "UPDATE registerinfo SET gender = {} WHERE userId = '{}'".format(new_value, user_id)
        self.cursor.execute(modify_sql)
        self.conn.commit()
        return 0

    def modify_user_age(self, user_id, new_value: int):
        sql = "SELECT userId FROM registerinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        flag = 0
        for (id,) in res:
            if id == user_id:
                flag = 1
                break
        if flag == 0:  #没有找到
            return -1

        modify_sql = "UPDATE registerinfo SET age = {} WHERE userId = '{}'".format(new_value, user_id)
        self.cursor.execute(modify_sql)
        self.conn.commit()
        return 0

    def modify_user_face(self, user_id, new_value: int):
        sql = "SELECT userId FROM registerinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        flag = 0
        for (id,) in res:
            if id == user_id:
                flag = 1
                break
        if flag == 0:  #没有找到
            return -1

        modify_sql = "UPDATE registerinfo SET face = {} WHERE userId = '{}'".format(new_value, user_id)
        self.cursor.execute(modify_sql)
        self.conn.commit()
        return 0

    def modify_user_sign(self, user_id, new_value):
        sql = "SELECT userId FROM registerinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        flag = 0
        for (id,) in res:
            if id == user_id:
                flag = 1
                break
        if flag == 0:  #没有找到
            return -1

        modify_sql = "UPDATE registerinfo SET sign = '{}' WHERE userId = '{}'".format(new_value, user_id)
        self.cursor.execute(modify_sql)
        self.conn.commit()
        return 0

    # 根据Id查找指定人
    def search_specific_person(self, user_id):
        sql = "SELECT userId,gender,age,face,sign FROM registerinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (id, gd, ag, fc, sg) in res:
            if id == user_id:
                json_dict = {
                    "userId": id,
                    "gender": gd,
                    "age": ag,
                    "face": fc,
                    "sign": sg
                }
                return jsonify(json_dict)
        return "-1"


    # 注销用户信息
    def cancellation_info(self, user_id):
        sql = "SELECT userId FROM registerinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        flag = 0
        for (id,) in res:
            if id == user_id:
                flag = 1
                break
        if flag == 0:
            return -1
        delete_sql = "DELETE FROM registerinfo WHERE userId = '{}'".format(user_id)
        self.cursor.execute(delete_sql)
        self.conn.commit()
        delete_friends_sql = "DELETE FROM friendsinfo WHERE userId = '{}'".format(user_id)
        self.cursor.execute(delete_friends_sql)
        self.conn.commit()
        return 0

    def forget_the_password(self, user_id, new_password, user_email):
        sql = "SELECT userId,email FROM registerinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_id, _email) in res:
            if _id == user_id and _email == user_email:
                update_sql = "UPDATE registerinfo SET password = %s WHERE userId = %s"
                self.cursor.execute(update_sql, [new_password, user_id])
                self.conn.commit()
                return 0
        return -1

    # def get_info_from_id(self, userId):
        # for (user_id, user_password, user_email, user_phone, user_gender, user_age, user_face, user_sign) in res:
        # print(res)


# test.register("hello.world", "Ajklsdjflsd", "jsdflk", "jdsfljd", 1, 10, 2, "kldjsflk")
# test.register("hello.world2", "cc@qq", "jsdflk", "jdsfljd", 1, 10, 2, "kldjsflk")
# test.register('darliron3', '123456789abc', '123@qq', '12312312', 1, 13, 20, "Hello World")
# print(test.log_in("darliron", "Aa@456456456"))
# test.get_info_from_id("sldkfj")
# print(test.log_in("darliron", "Ajsdfljldlsfj"))
# test.modify_user_id(new_value="ljdlfj")
# print(test.log_in("sdljfl", "kldsjf"))
# print(test.modify_user_id("darliron", "darlir"))
# print(test.modify_user_password("darliroon", "ello23", "Hello23"))
# test.cancellation_info("darliron")
# print(test.cancellation_info("darliron2"))
# test.total_modify("Li Hai tao4", "LiLiLi", "1111@qq.com", "1864524654", 1, 2, 3, "pouwer")

# test = DbOpera()
# test.cancellation_info("test")
# test.register('test', '123456789abc', '123@qq', '12312312', 1, 13, 20, "Hello World")
# test.cancellation_info("test")
# test.close_db()












