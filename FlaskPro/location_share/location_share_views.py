from . import location_share_bp
from appDB import location_share_db
import json
from flask import jsonify, request, send_file
import io


@location_share_bp.route("/locationUpload/<source_name>/<user_id>/<int:_psx>/<int:_psy>/<int:_psz>", methods=['GET'])
def _location_upload(source_name, user_id, _psx, _psy, _psz):
    odb = location_share_db.Location_share_db()
    result = odb.location_upload(source_name, user_id, _psx, _psy, _psz)
    odb.close_db()
    return str(result)


@location_share_bp.route("/deleteUserLocation/<user_id>", methods=['GET'])
def _delete_user_location(user_id):
    odb = location_share_db.Location_share_db()
    result = odb.location_delete(user_id)
    odb.close_db()
    return str(result)


@location_share_bp.route("/deleteAllLocation", methods=['GET'])
def _delete_all_location():
    odb = location_share_db.Location_share_db()
    result = odb.location_delete_all()
    odb.close_db()
    return str(result)


@location_share_bp.route("/getAllLocation/<spe_sour>", methods=['GET'])
def _get_all_location(spe_sour):
    odb = location_share_db.Location_share_db()
    result = odb.location_get_all(spe_sour)
    odb.close_db()
    return result  #JSON  or  "-3"




