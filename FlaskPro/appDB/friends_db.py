import pymysql
from flask import jsonify


def list_to_str(the_list: list):
    return ','.join([str(x) for x in the_list])


def str_to_list(the_str: str):
    return [str(i) for i in (the_str.split(','))]


class FriendsDB:
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

    """
    首先提取出朋友信息到列表中
    遍历列表查看当前要加的好友id是否重复
    如果不重复将friend_id 添加到列表
    将列表转为str 更新数据库 并将好友数量+1
    """
    def add_a_friend(self, user_id, friend_id: str):
        sql = "SELECT userId,num,friends FROM friendsinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_id, _num, _friends) in res:
            if _id == user_id:
                if _friends == "0":
                    update_sql = "UPDATE friendsinfo SET friends = '{}',num = 1 WHERE userId = '{}'".format(friend_id, user_id)
                    self.cursor.execute(update_sql)
                    self.conn.commit()
                else:
                    friend_list = str_to_list(_friends)
                    for a_friend in friend_list:
                        if a_friend == friend_id:
                            return -1
                    friend_list.append(friend_id)
                    friend_str = list_to_str(friend_list)
                    update_sql = "UPDATE friendsinfo SET friends = '{}',num = {} WHERE userId = '{}'".format(friend_str, (_num + 1) ,user_id)
                    self.cursor.execute(update_sql)
                    self.conn.commit()
                return 0
        return -2

    def get_all_friends(self, user_id):
        sql = "SELECT userId,friends FROM friendsinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_id, _friends) in res:
            if _id == user_id:
                if _friends == "0":
                    return 0
                else:
                    # friend_list = str_to_list(_friends)
                    return _friends
                # return 0
        return -2

    def delete_a_friend(self, user_id, friend_id):
        sql = "SELECT userId,num,friends FROM friendsinfo"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for (_id, _num, _friends) in res:
            if _id == user_id:
                if _friends == "0":
                    return -3  #没朋友可删除
                else:
                    friend_list = str_to_list(_friends)
                    for a_friend in friend_list:
                        if a_friend == friend_id:
                            friend_list.remove(friend_id)
                            friend_str = "0"
                            if _num != 1:
                                friend_str = list_to_str(friend_list)
                            update_sql = "UPDATE friendsinfo SET friends = '{}',num = {} WHERE userId = '{}'".format(
                                friend_str, (_num - 1), user_id)
                            self.cursor.execute(update_sql)
                            self.conn.commit()
                            return 0
                    return -1 #没有找到要删除的人
        return -2  #没找到该user

# test = FriendsDB()
# print(test.add_a_friend("test", "darliron"))
# print(test.add_a_friend("test", "a"))
# print(test.add_a_friend("test", "bcd"))
# print(test.add_a_friend("test", "deq"))
# print(type(test.get_all_friends("test")), test.get_all_friends("test"))
# str1 = list_to_str(["darliron", "Hello.World", "abc123"])
# print(type(str1), str1)
# list1 = str_to_list(str1)
# print(type(list1), list1)
# print(test.delete_a_friend("test", "bcd"))
