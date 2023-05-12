from flask import Flask
import socket
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    # Start a new process to run the stress_cpu.py script
    subprocess.Popen(["python3", "stress_cpu.py"])
    return 'Started stress_cpu.py', 200

@app.route('/', methods=['GET'])
def get_ip():
    # Get private IP address
    ip_address = socket.gethostbyname(socket.gethostname())
    return ip_address, 200

if __name__ == '__main__':
    # Run the server on a specific port
    app.run(host='0.0.0.0', port=8080)

