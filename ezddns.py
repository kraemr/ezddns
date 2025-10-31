import requests
from flask import Flask, request, jsonify
import re
import os
from base64 import b64decode
app = Flask(__name__)




@app.route('/nic/update', methods=['GET'])
def nic_update():
    hostname = request.args.get('hostname')
    myip = request.args.get('myip')
    ips = myip.split(",")
    ipv6 = ips[0]
    ipv4 = ips[1]

    if not hostname or not myip:
        return jsonify({"error": "Missing hostname or myip parameter"}), 400

#    print(hostname)
#    print(ipv6)
#    print(ipv4)


    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Basic '):
        return 'Missing or invalid auth header', 401

    # Decode the base64 part
    encoded_credentials = auth_header.split(' ')[1]
    decoded_credentials = b64decode(encoded_credentials).decode('utf-8')

    # Split into username and password
    username, password = decoded_credentials.split(':', 1)
    import custom.duckdns as dydns
    dydns.update_ip_addresses(ipv4,ipv6,hostname)




    return jsonify({
        "status": "success",
        "hostname": hostname,
        "myip": myip
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8666, debug=False)
