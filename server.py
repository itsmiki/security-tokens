import json
import flask
from flask import request, jsonify
from flask_cors import CORS
import time
import os
import sys

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
        print("token nie istnieje " + os.path.dirname(os.path.abspath(__file__)))
        return "Token does not exist."

    with open(os.path.dirname(os.path.abspath(__file__)) + '/session_logs/' + token_id[:16] + "/" + str(token_id) + '_info.txt', 'r', encoding='utf-8') as file:
        info = json.loads(file.read().replace("\'", "\""))
    
    user_agent = request.headers.get('User-Agent')
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy

    log = {
        "token_id": token_id,
        "token_name": info['token_name'],
        "token_type": info['token_type'],
        "description": info['description'],
        "message": info['message'],
        "ip": ip,
        "time_epoch": time_of_request_epoch,
        "time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_of_request_epoch)),
        "user-agent": user_agent,
    }

    with open(os.path.dirname(os.path.abspath(__file__)) + '/session_logs/' + token_id[:16] + "/" + str(token_id) + '.txt', 'a') as file:
        file.write(json.dumps(log) + "\n")

    return ip


if __name__ == "__main__":
    if len(sys.argv) == 2:
        app.run(host='0.0.0.0', port = sys.argv[1])
    elif len(sys.argv) == 3:
        app.run(host=sys.argv[1], port = sys.argv[2])
    else:
        app.run(host='0.0.0.0')

