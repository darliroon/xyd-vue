from flask import Flask, Blueprint, request, jsonify
from user_enter import user_bp
from user_friends import friends_bp
from connect_main_objects  import main_objects_bp
from positional_info import positional_info_bp
from dm_enter import dm_enter_views_bp
from new_finger_table import new_finger_table_bp
from new_object_table import new_object_table_bp
from new_img_table import new_img_table_bp
from dm_insert import dm_insert_views_bp
from get_developer_new import get_developer_new_bp
from location_share import location_share_bp
from chat import chat_bp
from nav import nav_bp
from new_nav_table import new_nav_table_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.register_blueprint(user_bp)
app.register_blueprint(friends_bp)
app.register_blueprint(main_objects_bp)
app.register_blueprint(positional_info_bp)
app.register_blueprint(dm_enter_views_bp)
app.register_blueprint(new_finger_table_bp)
app.register_blueprint(new_object_table_bp)
app.register_blueprint(new_img_table_bp)
app.register_blueprint(dm_insert_views_bp)
app.register_blueprint(get_developer_new_bp)
app.register_blueprint(location_share_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(new_nav_table_bp)
app.register_blueprint(nav_bp)

# # 跨域支持
# def after_request(resp):
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     return resp
#
#
# app.after_request(after_request)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )