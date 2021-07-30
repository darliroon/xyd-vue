from . import new_object_table_bp
from appDB import new_object_table_db
import json
from flask import jsonify, request


@new_object_table_bp.route("/newObjectTable", methods=['POST'])
def _new_object_table():
    # print(request.data)
    # print(request.get_data(as_text=True))
    # print(data)
    data = json.loads(request.get_data(as_text=True))  #JSON -> dict
    nfdb = new_object_table_db.NewObjectTable()
    result = nfdb.create_new_table(data['name'], data['sql'])
    nfdb.close_db()
    return str(result)


@new_object_table_bp.route("/dropObjectTable/<tab_name>", methods=['GET'])
def _drop_object_table(tab_name):
    nfdb = new_object_table_db.NewObjectTable()
    result = nfdb.drop_the_table(tab_name)
    nfdb.close_db()
    return str(result)


@new_object_table_bp.route("/getAHolds", methods=['GET'])
def _get_a_holds():
    nfdb = new_object_table_db.NewObjectTable()
    result = nfdb.get_all_holds()
    nfdb.close_db()
    return result
