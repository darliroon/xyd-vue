from . import dm_insert_views_bp
from appDB import dm_insert_db
import json
from flask import jsonify, request


@dm_insert_views_bp.route("/insertManyFingers/<table_name>", methods=['POST'])
def insert_many_fingers(table_name):
    json_data = request.get_json()
    odb = dm_insert_db.InsertFingerDB()
    result = odb.insert_many_finger_info(table_name, json_data)
    odb.close_db()
    return str(result)


@dm_insert_views_bp.route("/insertManyObjects/<table_name>", methods=['POST'])
def insert_many_objects(table_name):
    json_data = request.get_json()
    odb = dm_insert_db.InsertObjectDB()
    result = odb.insert_many_objects_info(table_name, json_data)
    odb.close_db()
    return str(result)


@dm_insert_views_bp.route("/insertManyNavs/<table_name>", methods=['POST'])
def insert_many_navs(table_name):
    json_data = request.get_json()
    odb = dm_insert_db.InsertNavDB()
    result = odb.insert_many_nav_info(table_name, json_data)
    odb.close_db()
    return str(result)

