from . import positional_info_bp
from appDB import position_info_db
import json
from flask import jsonify, request


@positional_info_bp.route("/position/createNewPS/<int:_psx>/<int:_psy>/<int:_psz>/<_id1>/<int:_ap1>/<_id2>/<int:_ap2>/<"
                          "_id3>/<int:_ap3>/<_id4>/<int:_ap4>/<_id5>/<int:_ap5>/<_id6>/<int:_ap6>/<_id7>/<int:_ap7>/<_id8"
                          ">/<int:_ap8>/<_id9>/<int:_ap9>/<_id10>/<int:_ap10>", methods=['GET'])
def _create_new_position(_psx, _psy, _psz, _id1, _ap1, _id2, _ap2, _id3, _ap3, _id4, _ap4, _id5, _ap5, _id6, _ap6, _id7,
                         _ap7, _id8, _ap8, _id9, _ap9, _id10, _ap10):
    pdb = position_info_db.PositionDB()
    result = pdb.create_new_position(_psx, _psy, _psz, _id1, _ap1, _id2, _ap2, _id3, _ap3, _id4, _ap4, _id5, _ap5,
                                     _id6, _ap6, _id7, _ap7, _id8, _ap8, _id9, _ap9, _id10, _ap10)
    pdb.close_db()
    return str(result)


@positional_info_bp.route("/position/deleteSpePS/<int:_psx>/<int:_psy>/<int:_psz>", methods=['GET'])
def _delete_specific_position(_psx, _psy, _psz):
    pdb = position_info_db.PositionDB()
    result = pdb.delete_spe_position(_psx, _psy, _psz)
    pdb.close_db()
    return str(result)


@positional_info_bp.route("/position/getLatestPS", methods=['GET'])
def _get_latest_position_info():
    pdb = position_info_db.PositionDB()
    result = pdb.get_latest_position_info()
    pdb.close_db()
    return result    #JSON






