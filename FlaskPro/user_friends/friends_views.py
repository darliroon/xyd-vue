from . import friends_bp
from appDB import friends_db

import json
from flask import jsonify, request


@friends_bp.route('/friends/addFriend/<user_id>/<friend_id>', methods=['GET'])
def addFriend(user_id, friend_id):
    db = friends_db.FriendsDB()
    result = db.add_a_friend(user_id, friend_id)
    db.close_db()
    return str(result)


@friends_bp.route('/friends/getAllFriends/<user_id>', methods=['GET'])
def getFriends(user_id):
    db = friends_db.FriendsDB()
    result = db.get_all_friends(user_id)  #返回字符串
    db.close_db()
    if result == 0 or result == -2:
        return "null"
    else:
        return result


@friends_bp.route('/friends/deleteFriend/<user_id>/<friend_id>', methods=['GET'])
def deleteFriend(user_id, friend_id):
    db = friends_db.FriendsDB()
    result = db.delete_a_friend(user_id, friend_id)
    db.close_db()
    return str(result)














