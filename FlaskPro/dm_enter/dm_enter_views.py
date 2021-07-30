from . import dm_enter_views_bp
from appDB import dm_enter_db
import json
from flask import jsonify, request


@dm_enter_views_bp.route("/dmRegister/<user_id>/<password>", methods=['GET'])
def _dm_register(user_id, password):
    dmdb = dm_enter_db.DMRegister_db()
    result = dmdb.dm_register(user_id, password)
    dmdb.close_db()
    return str(result)  #-1  0


@dm_enter_views_bp.route("/dmLogIn/<user_id>/<password>", methods=['GET'])
def _dm_log_in(user_id, password):
    dmdb = dm_enter_db.DMRegister_db()
    result = dmdb.dm_log_in(user_id, password)
    dmdb.close_db()
    return str(result)  # 1  -1


@dm_enter_views_bp.route("/dmAddHold/<user_id>/<new_hold>", methods=['GET'])
def _dm_add_hold(user_id, new_hold):
    dmdb = dm_enter_db.DMRegister_db()
    result = dmdb.add_hold(user_id, new_hold)
    dmdb.close_db()
    return str(result)


@dm_enter_views_bp.route("/dmGetHold/<user_id>", methods=['GET'])
def _dm_get_hold(user_id):
    dmdb = dm_enter_db.DMRegister_db()
    result = dmdb.get_hold(user_id)
    dmdb.close_db()
    return result


@dm_enter_views_bp.route("/dmRemoveHold/<user_id>/<spe_hold>", methods=['GET'])
def _dm_remove_hold(user_id, spe_hold):
    dmdb = dm_enter_db.DMRegister_db()
    result = dmdb.remove_hold(user_id, spe_hold)
    dmdb.close_db()
    return str(result)

