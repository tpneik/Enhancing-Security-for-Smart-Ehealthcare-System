from flask import Flask
from web_base._flask import FlaskAppWrapper
from dotenv import load_dotenv
import os,json
from bson.objectid import ObjectId
load_dotenv()

flask_app = Flask(__name__)

# Json Encoder
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super(JSONEncoder, self).default(o)
flask_app.json_encoder = JSONEncoder
app = FlaskAppWrapper(flask_app)


# Controller declaration
from controller.hello_world import hello_world
from controller.user import add_user, login
from controller.client import *
from controller.fl_server import start_train, get_fit_prgress_by_id
from controller.response import *


# Add route
app.add_endpoint('/hello', 'hello', hello_world) # This test need login -> pass Authorized key to headers ->  call
app.add_endpoint('/total_client', 'total_client', get_total_client) #
app.add_endpoint('/start_train', 'start_train', start_train, ["POST"])
app.add_endpoint('/add_user', 'add_user', add_user, ["POST"])
app.add_endpoint('/login', 'login', login, ["POST"])
app.add_endpoint('/add_client', 'add_client', add_client, ["POST"])
app.add_endpoint('/delete_client', 'delete_client', delete_client, ["POST"])
app.add_endpoint('/client_login', 'client_login', client_login, ["POST"])
app.add_endpoint('/zip_file', 'zip_file', zip_file)
app.add_endpoint('/sh_file', 'sh_file', sh_file)
app.add_endpoint('/is_exist', 'is_exist', is_exist, ["POST"])
app.add_endpoint('/client_online', 'client_online', client_online, ["POST"])
app.add_endpoint('/get_fit_prgress_by_id', 'get_fit_prgress_by_id', get_fit_prgress_by_id, ["POST"])
app.add_endpoint('/update_client_status', 'update_client_status', update_client_status, ["POST"])
# app.add_endpoint('monitor_train', 'monitor_train', monitor_train, ["GET"])
app.add_endpoint('/get_active_client', 'get_active_client', get_active_client, ["GET"])
app.add_endpoint('/get_waiting_client', 'get_waiting_client', get_waiting_client, ["GET"])
app.add_endpoint('/get_training_client', 'get_training_client',get_training_client, ["GET"])
app.add_endpoint('/get_error_client', 'get_error_client', get_error_client, ["GET"])
app.add_endpoint('/install_file', 'install_file', install_file, ["GET"])




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv('PORT'))
    