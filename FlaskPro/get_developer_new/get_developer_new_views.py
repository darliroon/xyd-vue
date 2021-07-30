from . import get_developer_new_bp
from appDB import get_developer_new_db
import json
from flask import jsonify, request,send_file
import io


@get_developer_new_bp.route("/getDeveloperNewFingers/<table_name>", methods=['GET'])
def _get_developer_new_fingers(table_name):
    odb = get_developer_new_db.GetDeveloperNewFingersDB()
    result = odb.get_developer_new_fingers(table_name)
    odb.close_db()
    return result


@get_developer_new_bp.route("/getDeveloperNewObjects/<table_name>", methods=['GET'])
def _get_developer_new_objects(table_name):
    odb = get_developer_new_db.GetDeveloperNewObjectsDB()
    result = odb.get_developer_new_objects(table_name)
    odb.close_db()
    return result


# def get_developer_new_objects_simply(self, table_name):
@get_developer_new_bp.route("/getDeveloperNewObjectsSimply/<table_name>", methods=['GET'])
def _get_developer_new_objects_simply(table_name):
    odb = get_developer_new_db.GetDeveloperNewObjectsDB()
    result = odb.get_developer_new_objects_simply(table_name)
    odb.close_db()
    return result


@get_developer_new_bp.route("/getDeveloperObjectImgFromURL/<table_name>/<i_url>", methods=['GET'])
def _get_developer_object_img_from_url(table_name, i_url):
    odb = get_developer_new_db.GetDeveloperNewObjectsDB()
    result = odb.get_developer_object_img_from_url(table_name, i_url)
    odb.close_db()
    if result == -1:
        return "Failed-1"
    elif result == -3:
        return "Failed-3"
    else:
        return send_file(io.BytesIO(result), attachment_filename='haitao.jpg')


@get_developer_new_bp.route("/getDeveloperImgImg/<table_name>", methods=['GET'])
def _get_developer_img_img_from_table(table_name):
    odb = get_developer_new_db.GetDeveloperNewImgDB()
    result = odb.get_developer_img_img(table_name)
    odb.close_db()
    if result == -3:
        return "Failed-3"
    else:
        return send_file(io.BytesIO(result), attachment_filename='happy.jpg')


@get_developer_new_bp.route("/getDeveloperNavs/<table_name>", methods=['GET'])
def _get_developer_navs_from_table(table_name):
    odb = get_developer_new_db.GetDeveloperNavsDB()
    result = odb.get_developer_new_navs(table_name)
    odb.close_db()
    return result


@get_developer_new_bp.route("/getDeveloperNewFingersForDeveloper/<table_name>", methods=['GET'])
def _get_developer_new_fingers_for_developer(table_name):
    odb = get_developer_new_db.GetDeveloperNewFingersDB()
    result = odb.get_developer_new_fingers_for_developer(table_name)
    odb.close_db()
    return result


@get_developer_new_bp.route("/getDeveloperNewFingersForDeveloperJson/<table_name>", methods=['GET'])
def _get_developer_new_fingers_for_developer_json(table_name):
    odb = get_developer_new_db.GetDeveloperNewFingersDB()
    result = odb.get_developer_new_fingers_for_developer_json(table_name)
    odb.close_db()
    return result


