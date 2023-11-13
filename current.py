import getpass
import subprocess

# Get current username
username = getpass.getuser()

# Get MAC address
output = subprocess.check_output(['ipconfig', '/all']).decode('utf-8')
mac_address = None

for line in output.split('\n'):
    if 'Physical Address' in line:
        mac_address = line.split(':')[1].strip().replace('-', ':')
        break

# Get SSID
output = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8')
ssid = None

for line in output.split('\n'):
    if 'SSID' in line:
        ssid = line.split(':')[1].strip()
        break

# Write the collected information to a text file
with open('system_info.txt', 'w') as file:
    file.write("Username: {}\n".format(username))
    file.write("MAC Address: {}\n".format(mac_address))
    file.write("SSID: {}\n".format(ssid))

    # Print the collected information
print("Username:", username)
print("MAC Address:", mac_address)
print("SSID:", ssid)