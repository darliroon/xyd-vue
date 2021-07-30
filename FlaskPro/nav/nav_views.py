from . import nav_bp
from appDB import nav_db
import json
from flask import jsonify, request,send_file


@nav_bp.route("/addNewNav/<int:x1>/<int:y1>/<int:z1>/<int:x2>/<int:y2>/<int:z2>", methods=['GET'])
def add_new_nav(x1: int, y1: int, z1: int, x2: int, y2: int, z2: int):
    odb = nav_db.NavfDB()
    result = odb.add_new_nav_info(x1, y1, z1, x2, y2, z2)
    odb.close_db()
    return str(result)


@nav_bp.route("/deleteNav/<int:x1>/<int:y1>/<int:z1>/<int:x2>/<int:y2>/<int:z2>", methods=['GET'])
def delete_nav(x1: int, y1: int, z1: int, x2: int, y2: int, z2: int):
    odb = nav_db.NavfDB()
    result = odb.delete_nav_info(x1, y1, z1, x2, y2, z2)
    odb.close_db()
    return str(result)















