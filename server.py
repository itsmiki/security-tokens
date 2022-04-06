import flask
from flask import request, jsonify
from flask_cors import CORS
import time
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

api_key = ''
API_KEYS = {}

@app.route('/', methods=['GET'])
def home():
    return '''<h1>SERVER</h1>
<p>Server home page.</p>'''


@app.route('/token', methods=['GET'])
def get_token():
    time_of_request_epoch = time.time()

    if 'id' in request.args:
        token_id = str(request.args['id'])
        print(id)

    if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + '/session_logs/' + token_id[:16] + "/" + str(token_id) + '.txt'):
        print("token nie istnieje")
        return
    
    user_agent = request.headers.get('User-Agent')
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy

    log = {
        "token_id": token_id,
        "ip": ip,
        "time_epoch": time_of_request_epoch,
        "time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_of_request_epoch)),
        "user-agent": user_agent,
    }

    with open(os.path.dirname(os.path.abspath(__file__)) + '/session_logs/' + token_id[:16] + "/" + str(token_id) + '.txt', 'a') as file:
        file.write(str(log) + "\n")

    return ip



app.run(host='192.168.0.102')


# app.run(host='0.0.0.0')