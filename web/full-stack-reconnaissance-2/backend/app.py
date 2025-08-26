from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import secrets
import random

app = Flask(__name__)
# app.secret_key = secrets.token_hex(32) 
dbName = 'users.db'

@app.after_request
def apply_cors(response):
    origin = request.headers.get("Origin")
    if origin:
        response.headers["Access-Control-Allow-Origin"] = origin
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization,X-CSRFToken"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    return response


@app.route('/test', methods=['GET'])
def testLink():
    return jsonify({"message": "Hello from Kaled Aljebur!"}), 200

@app.route('/network', methods=['GET'])
def network():
    filtered = request.args.get('filtered', 'false').lower() == 'true'
    message="""
    Network Penetration Testing:
    External Network: Focuses on internet-facing assets 
    (public IP addresses, web servers, firewalls, routers, VPNs, email servers) 
    that an attacker could reach from outside the organization's perimeter. 
    Aims to identify vulnerabilities that could lead to initial unauthorized access.
    Internal Network: Simulates an attack from within the organization's 
    network, either as a malicious insider or an attacker who has already 
    gained initial access (e.g., through a compromised workstation). 
    It assesses vulnerabilities in internal servers, workstations, 
    network devices, and segmentation.
    Wireless Network: Specifically targets Wi-Fi networks, Bluetooth, 
    and other wireless protocols to identify weaknesses in encryption, 
    authentication, rogue access points, or misconfigurations that could 
    allow unauthorized access to the internal network.
    """
    if not filtered:
        message="N/A"
    return jsonify({"message": message}), 200

@app.route('/web', methods=['GET'])
def web():
    filtered = request.args.get('filtered', 'false').lower() == 'true'
    message="""
    Web Application Penetration Testing:
    Focuses on web applications (websites, portals, APIs) to 
    identify vulnerabilities in their code, configuration, and design.
    Common vulnerabilities tested include those listed in the OWASP Top 
    10 (e.g., Injection, Broken Authentication, Cross-Site Scripting 
    (XSS), Insecure Deserialization, Security Misconfigurations).
    Includes testing of underlying web servers, databases, and 
    application programming interfaces (APIs).
    """
    if not filtered:
        message="N/A"
    return jsonify({"message": message}), 200

@app.route('/cloud', methods=['GET'])
def cloud():
    filtered = request.args.get('filtered', 'false').lower() == 'true'
    message="""
    Cloud Penetration Testing:
    Evaluates the security posture of cloud environments and services (IaaS, PaaS, SaaS).
    This includes assessing misconfigurations in cloud infrastructure (e.g., 
    AWS S3 buckets, Azure VMs, Google Cloud services), identity and access management 
    (IAM) issues, container security, and cloud application vulnerabilities.
    """
    if not filtered:
        message="N/A"
    return jsonify({"message": message}), 200

@app.route('/mobile', methods=['GET'])
def mobile():
    message="""
    Mobile Application Penetration Testing:
    Assesses the security of mobile applications (iOS, Android, etc.) and their associated backend APIs.
    Looks for vulnerabilities related to insecure 
    data storage, weak authentication, insecure 
    communication, side-channel data leakage, and improper session management.
    """
    return jsonify({"message": message}), 200

@app.route('/social', methods=['GET'])
def social():
    filtered = request.args.get('filtered', 'false').lower() == 'true'
    message="""
    Social Engineering Penetration Testing:
    Focuses on the "human element" of security.
    Simulates attacks designed to trick individuals 
    into divulging sensitive information, performing actions they shouldn't, or granting unauthorized access.
    Common techniques include:
    Phishing/Spear Phishing: Email attacks to steal credentials or deliver malware.
    Vishing: Voice-based phishing (phone calls).
    Smishing: SMS/text message phishing.
    Pretexting: Creating a fabricated scenario to manipulate targets.
    Baiting: Using physical media (e.g., infected USB drives).
    """
    if not filtered:
        message="N/A"
    return jsonify({"message": message}), 200

@app.route('/physical', methods=['GET'])
def physical():
    filtered = request.args.get('filtered', 'false').lower() == 'true'
    message="""
    Physical Security Penetration Testing:
    Simulates an attacker attempting to gain 
    unauthorized physical access to a facility, data centers, or restricted areas.
    This can involve attempts to bypass locks, 
    alarms, surveillance systems, or tailgating legitimate employees to access sensitive equipment or information.
    """
    if not filtered:
        message="N/A"
    return jsonify({"message": message}), 200

@app.route('/client', methods=['GET'])
def client():
    # filtered = 'filtered' in request.args
    filtered = request.args.get('filtered', 'false').lower() == 'true'
    # filtered = request.args.get('filtered', 'false').lower()
    # is_filtered = filtered_param == 'true'  
    # print(filtered)
    has_query_params = len(request.args) > 0
    message="""
    Client-Side Penetration Testing:
    Focuses on vulnerabilities in client-side applications, 
    such as web browsers, email clients, or desktop applications that interact with a server.
    Looks for flaws like Cross-Site Scripting (XSS), Clickjacking, 
    DOM-based vulnerabilities, and issues in browser plugins or extensions.
    """
    if filtered == 'false':
        message= "Smart move flipping the filter!"
    # if not filtered:
    if not has_query_params:
        message="Well done! the flag is: pecan{flag3_a#GkjJHY743$$9JF}"
    return jsonify({"message": message}), 200

@app.route('/iot', methods=['GET'])
def iot():
    message="""
    IoT (Internet of Things) Penetration Testing:
    Evaluates the security of interconnected physical devices 
    (smart home devices, industrial control systems, wearables, medical devices).
    Looks for vulnerabilities in device firmware, communication protocols, cloud connectivity, and API interfaces.
    """
    return jsonify({"message": message}), 200

@app.route('/', methods=['GET'])
def secret():
    message="Well done! the flag is: pecan{flag2_sf@hNsa;*67^$4fJ}"
    return jsonify({"message": message}), 200

# @app.route('/web/secret', methods=['GET'])
# def webSecret():
#     message="Well done! the flag is: pecan{flag3_a#GkjJHY743$$9JF}"
#     return jsonify({"message": message}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='7123')
