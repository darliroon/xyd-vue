from . import main_objects_bp
from appDB import main_objects_db
import json
from flask import jsonify, request
from flask import send_from_directory, send_file
import requests

import io

# @main_objects_bp.route('/mainObject/addObject/', methods=['POST'])
# def add_object():
#     data = json.loads(request.get_data(as_text=True))
# #接收一个文件保存到服务器静态端
# @main_objects_bp.route('mainObjects/uploadPic', methods=["POST"])
# def upload_pic():
#     f = request.files['pic'] #key值为pic的文件
#     with open('./demo.png', 'wb') as new_file:
#         new_file.write(f.read())
#     return 'ok'


@main_objects_bp.route("/mainObjects/createNewObject/<object_name>", methods=['GET'])
def _create_new_object(object_name):
    mdb = main_objects_db.MainObjectsDB()
    result = mdb.create_new_object(object_name)
    mdb.close_db()
    return str(result)


@main_objects_bp.route("/mainObjects/updateName/<old_name>/<new_name>", methods=['GET'])
def _update_specific_object_name(old_name, new_name):
    mdb = main_objects_db.MainObjectsDB()
    result = mdb.update_specific_object_name(old_name, new_name)
    mdb.close_db()
    return str(result)


# update_specific_object_coordinate
@main_objects_bp.route("/mainObjects/updateCoordinate/<object_name>/<new_coordinate>", methods=['GET'])
def _update_specific_object_coordinate(object_name, new_coordinate):
    mdb = main_objects_db.MainObjectsDB()
    result = mdb.update_specific_object_coordinate(object_name, new_coordinate)
    mdb.close_db()
    return str(result)


#update_specific_object_label
@main_objects_bp.route("/mainObjects/updateLabel/<object_name>/<int:new_label>", methods=['GET'])
def _update_specific_object_label(object_name, new_label):
    mdb = main_objects_db.MainObjectsDB()
    result = mdb.update_specific_object_label(object_name, new_label)
    mdb.close_db()
    return str(result)


#update_specific_object_img
@main_objects_bp.route("/mainObjects/updateImg/<object_name>", methods=['POST'])
def _update_specific_object_img(object_name):
    url = request.get_data(as_text=True)
    print(url)
    data = requests.get(url)
    data_content = data.content
    # print(data_content)
    mdb = main_objects_db.MainObjectsDB()
    result = mdb.update_specific_object_img(object_name, data_content)
    mdb.close_db()
    return str(result)
    # f = request.files['pic'] #key值为pic的文件
    # mdb = main_objects_db.MainObjectsDB()
    # result = mdb.update_specific_object_img(object_name, f.read())
    # mdb.close_db()
    # with open('./demo.jpeg', 'wb') as new_file:
    #     new_file.write(f.read())
    # return "0"
    # return str(result)


@main_objects_bp.route("/mainObjects/getImg/<object_name>", methods=['GET'])
def _get_object_img(object_name):
    mdb = main_objects_db.MainObjectsDB()
    result = mdb.get_object_img(object_name)
    mdb.close_db()
    if result != -1:
        return send_file(io.BytesIO(result), attachment_filename='imgFile.jpg')
        # return send_file(io.BytesIO(result))
    return "Failed!"


# @main_objects_bp.route("/mainObjects/updateDetails/<object_name>/<detail>", methods=['GET'])
# def _update_specific_object_detail(object_name, detail):
#     mdb = main_objects_db.MainObjectsDB()
#     result = mdb.update_object_details(object_name, detail)
#     mdb.close_db()
#     return str(result)

@main_objects_bp.route("/mainObjects/updateDetails/<object_name>", methods=['POST'])
def _update_specific_object_detail(object_name):
    data = request.get_data(as_text=True)     #text/plain   data是str类型  这样的话就可以实现data中包含中文
    mdb = main_objects_db.MainObjectsDB()
    result = mdb.update_object_details(object_name, data)
    mdb.close_db()
    return str(result)
    # print(type(data))
    # print(data)
    # print(request.form['pic'])
    # print(request.form['pic'])
    # print(request.form['pic'])


@main_objects_bp.route("/mainObjects/updateComments/<object_name>", methods=['POST'])
def _update_specific_object_comments(object_name):
    data = request.get_data(as_text=True)
    mdb = main_objects_db.MainObjectsDB()
    result = mdb.update_object_comments(object_name, data)
    mdb.close_db()
    return str(result)


@main_objects_bp.route("/mainObjects/addComments/<object_name>", methods=['POST'])
def _add_specific_object_comments(object_name):
    data = request.get_data(as_text=True)
    mdb = main_objects_db.MainObjectsDB()
    result = mdb.add_object_comment(object_name, data)
    mdb.close_db()
    return str(result)


@main_objects_bp.route("/mainObjects/deleteAllComments/<object_name>", methods=['GET'])
def _delete_all_object_comments(object_name):
    mdb = main_objects_db.MainObjectsDB()
    result = mdb.delete_object_all_comments(object_name)
    mdb.close_db()
    return str(result)


@main_objects_bp.route("/mainObjects/deleteSpeComment/<object_name>", methods=['POST'])
def _delete_specific_object_comment(object_name):
    data = request.get_data(as_text=True)
    mdb = main_objects_db.MainObjectsDB()
    result = mdb.delete_specific_comment(object_name, data)
    mdb.close_db()
    return str(result)


@main_objects_bp.route("/mainObjects/getAllComments/<object_name>", methods=['GET'])
def _get_all_comments(object_name):
    mdb = main_objects_db.MainObjectsDB()
    result = mdb.get_all_comments(object_name)
    mdb.close_db()
    return result   # "0" or "..."

#查找
# @main_objects_bp.route("/mainObjects/upd")
"""
    def update_object_comments(self, object_name, new_comment):
        def add_object_comment(self, object_name, add_comment):
            def delete_object_all_comments(self, object_name):
                def delete_specific_comment(self, object_name, comments_content):
"""

