from . import chat_bp
from appDB import chat_db
import json
from flask import jsonify, request


@chat_bp.route("/postToRec/<poster>/<receiver>", methods=['POST'])
def _post_to_rec(poster, receiver):
    json_data = request.get_json()
    odb = chat_db.CharDB()
    result = odb.post_info_to_receiver(poster, receiver, json_data['info'])
    odb.close_db()
    return str(result)


@chat_bp.route("/getInfoFromAllPoster/<receiver>", methods=['GET'])
def _get_info_from_all_posters(receiver):
    odb = chat_db.CharDB()
    result = odb.get_info_from_all_posters(receiver)
    odb.close_db()
    return result   #JSON or "-1"


@chat_bp.route("/getSpePosterInfo/<receiver_name>/<poster_name>", methods=['GET'])
def _get_sep_poster_info(receiver_name, poster_name):
    odb = chat_db.CharDB()
    result = odb.get_spe_poster_info(receiver_name, poster_name)
    odb.close_db()
    return result


