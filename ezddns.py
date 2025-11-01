import requests
from flask import Flask, request, jsonify
import re
import os
from base64 import b64decode
app = Flask(__name__)




@app.route('/nic/update', methods=['GET'])
def nic_update():
    print("Updating IP")
    hostname = request.args.get('hostname')
    myip = request.args.get('myip')
    ips = myip.split(",")
    ipv6 = ips[0]
    ipv4 = ips[1]

    if not hostname or not myip:
        return jsonify({"error": "Missing hostname or myip parameter"}), 400

    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Basic '):
        return 'Missing or invalid auth header', 401

    encoded_credentials = auth_header.split(' ')[1]
    decoded_credentials = b64decode(encoded_credentials).decode('utf-8')
    username, password = decoded_credentials.split(':', 1)

    if app.config["BACKEND"] == "None":
        return "No Backend specified", 500

    if app.config["BACKEND"] == "duckdns":
        print("using duckdns backend")
        import custom.duckdns as dydns
        # for duckdns password==api token
        dydns.update_ip_addresses(ipv4,ipv6,hostname,password)
    return f"good {myip}", 200, {"Content-Type": "text/plain"}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8666))
    app.config['BACKEND'] = os.getenv("EZDDNS_BACKEND", "None")
    app.run(host='0.0.0.0', port=port, debug=False)
