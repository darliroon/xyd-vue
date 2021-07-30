from . import new_img_table_bp
from appDB import new_img_table_db
import json
from flask import jsonify, request, send_file

import io

@new_img_table_bp.route("/newImgTable", methods=['POST'])
def _new_img_table():
    # print(request.data)
    # print(request.get_data(as_text=True))
    # print(data)
    data = json.loads(request.get_data(as_text=True))  #JSON -> dict
    nfdb = new_img_table_db.NewImgTableDB()
    result = nfdb.create_new_table(data['name'], data['sql'])
    nfdb.close_db()
    return str(result)


@new_img_table_bp.route("/dropImgTable/<tab_name>", methods=['GET'])
def _drop_img_table(tab_name):
    nfdb = new_img_table_db.NewImgTableDB()
    result = nfdb.drop_the_table(tab_name)
    nfdb.close_db()
    return str(result)


@new_img_table_bp.route("/imgToTable/<table_name>", methods=['POST'])
def _add_img_to_table(table_name):
    file_obj = request.files['file']
    nfdb = new_img_table_db.NewImgTableDB()
    result = nfdb.add_img(table_name, file_obj.read())
    nfdb.close_db()
    return str(result)


@new_img_table_bp.route("/fromTableImg/<table_name>", methods=['GET'])
def _from_table_get_img(table_name):
    nfdb = new_img_table_db.NewImgTableDB()
    result = nfdb.get_img(table_name)
    nfdb.close_db()
    if result != -3:
        return send_file(io.BytesIO(result), attachment_filename='lol')
    return "Failed!"


@new_img_table_bp.route("/tet", methods=['POST'])
def _use_for_test():
    json_data = request.get_json()
    print(json_data)
    print(type(json_data))
    print(type(json_data[0]))
    print(type(json_data[0]['hello']))
    print(type(json_data[1]['lol']))
    print("single record:")
    for single_record in json_data:
        print(type(single_record))
    return "0020"



















