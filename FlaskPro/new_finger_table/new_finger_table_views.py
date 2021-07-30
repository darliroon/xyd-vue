from . import new_finger_table_bp
from appDB import new_finger_table_db
import json
from flask import jsonify, request


@new_finger_table_bp.route("/newFingerTable", methods=['POST'])
def _new_finger_table():
    # print(request.data)
    # print(request.get_data(as_text=True))
    # print(data)
    data = json.loads(request.get_data(as_text=True))  #JSON -> dict
    nfdb = new_finger_table_db.NewTable()
    result = nfdb.create_new_table(data['name'], data['sql'])
    nfdb.close_db()
    return str(result)


@new_finger_table_bp.route("/dropFingerTable/<tab_name>", methods=['GET'])
def _drop_finger_table(tab_name):
    nfdb = new_finger_table_db.NewTable()
    result = nfdb.drop_the_table(tab_name)
    nfdb.close_db()
    return str(result)








