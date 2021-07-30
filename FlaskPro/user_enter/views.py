from . import user_bp
from appDB import DbOpera
import json
from flask import jsonify, request


@user_bp.route('/logIn/<user_id>/<user_password>', methods=["GET"])
def log_in_and_get_personal_info(user_id, user_password):
    print(user_id)
    print(user_password)
    d = DbOpera()
    judge = d.log_in(user_id, user_password)    #return JSON or "-1"
    d.close_db()
    return judge
    # return "0"

#接收 JSON 数据
@user_bp.route('/register', methods=['POST'])
def _register():
    data = json.loads(request.get_data(as_text=True))
    #对字典数据进行处理
    d = DbOpera()
    result = d.register(data['userId'], data['password'], data['email'], data['phone'], data['gender'], data['age'], data['face'], data['sign'])
    d.close_db()
    return str(result)   #-1  0


    # for key, value in data.items():
    #     print("Then we have got the json_dicts: now we will display them")
    #     print(key, value)
    # json_dict = {  #测试数据
    #     "ljdsf" : "ldjsf",
    #     "ljdf" : "ljdsf"
    # }
    # return data


@user_bp.route('/modifyId/<old_value>/<new_value>', methods=['GET'])
def _modify_id(old_value, new_value):
    d = DbOpera()
    result = d.modify_user_id(old_value, new_value)
    d.close_db()
    return str(result)  #-2  -1  0


@user_bp.route('/modifyPw/<user_id>/<old_value>/<new_value>', methods=['GET'])
def _modify_password(user_id, old_value, new_value):
    d = DbOpera()
    result = d.modify_user_password(user_id, old_value, new_value)
    d.close_db()
    return str(result)  #-1 0


@user_bp.route('/modifyEmail/<user_id>', methods=['POST'])
def _modify_email(user_id):
    json_data = request.get_json()
    d = DbOpera()
    result = d.modify_user_email(user_id, json_data['new_email'])
    d.close_db()
    return str(result)


@user_bp.route('/modifyPhone/<user_id>/<new_value>', methods=['GET'])
def _modify_phone(user_id, new_value):
    d = DbOpera()
    result = d.modify_user_phone(user_id, new_value)
    d.close_db()
    return str(result)


@user_bp.route('/modifyGender/<user_id>/<int:new_value>', methods=['GET'])
def _modify_gender(user_id, new_value):
    d = DbOpera()
    result = d.modify_user_gender(user_id, new_value)
    d.close_db()
    return str(result)


@user_bp.route('/modifyAge/<user_id>/<int:new_value>', methods=['GET'])
def _modify_age(user_id, new_value):
    d = DbOpera()
    result = d.modify_user_age(user_id, new_value)
    d.close_db()
    return str(result)


@user_bp.route('/modifyFace/<user_id>/<int:new_value>', methods=['GET'])
def _modify_face(user_id, new_value):
    d = DbOpera()
    result = d.modify_user_face(user_id, new_value)
    d.close_db()
    return str(result)


@user_bp.route('/modifySign/<user_id>/<new_value>', methods=['GET'])
def _modify_sign(user_id, new_value):
    d = DbOpera()
    result = d.modify_user_sign(user_id, new_value)
    d.close_db()
    return str(result)


# def total_modify(self, old_id, new_id, new_el, new_pe, new_gd, new_ag, new_fc, new_sg):
# @user_bp.route('/modifyAll/<old_id>/<new_id>/<new_el>/<new_pe>/<int:new_gd>/<int:new_ag>/<int:new_fc>/<new_sg>', methods=['GET'])
@user_bp.route("/modifyAll", methods=['POST'])
def _modify_all():
    json_data = request.get_json()
    d = DbOpera()
    result = d.total_modify(json_data['old_id'], json_data['new_id'], json_data['new_el'], json_data['new_pe'], json_data['new_gd'],
                            json_data['new_ag'], json_data['new_fc'], json_data['new_sg'])
    d.close_db()
    return str(result)   # "-2"   "-1"    "0"


@user_bp.route("/searchAPerson/<user_id>", methods=['GET'])
def _search_specific_person(user_id):
    d = DbOpera()
    result = d.search_specific_person(user_id)
    d.close_db()
    return result     # JSON or "-1"


@user_bp.route("/cancellation/<user_id>", methods=['GET'])
def _cancellation_of_account(user_id):
    d = DbOpera()
    result = d.cancellation_info(user_id)
    d.close_db()
    return str(result)  #"-1"  "0"


@user_bp.route("/forgetPassword", methods=['POST'])
def _forget_password():
    json_data = request.get_json()
    d = DbOpera()
    result = d.forget_the_password(json_data['userId'], json_data['newPassword'], json_data['email'])
    d.close_db()
    return str(result)   #-1   0
