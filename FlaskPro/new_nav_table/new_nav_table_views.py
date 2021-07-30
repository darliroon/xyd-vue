from . import new_nav_table_bp
from appDB import new_nav_table_db
import json
from flask import jsonify, request


@new_nav_table_bp.route("/newNavTable", methods=['POST'])
def _new_nav_table():
    data = json.loads(request.get_data(as_text=True))  #JSON -> dict
    odb = new_nav_table_db.NavTableDB()
    result = odb.create_new_table(data['name'], data['sql'])
    odb.close_db()
    return str(result)


@new_nav_table_bp.route("/dropNavTable/<tab_name>", methods=['GET'])
def _drop_nav_table(tab_name):
    odb = new_nav_table_db.NavTableDB()
    result = odb.drop_the_table(tab_name)
    odb.close_db()
    return str(result)

