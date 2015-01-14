import os
import socket

_END = '> \0'

# status codes
_ERROR = -1
_OK = 1
_INFO = 2

host = '127.0.0.1'
port = 12357

path = os.path.dirname(__file__)
command = r'@%s' % (os.path.join(path, 'traceback.py'))
print command

con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((host, port))

con.recv(1024)  # eat the first prompt character

result = []
# send command
con.sendall('%s\0' % command)
alldata = ''
# collect data
while 1:
    data = con.recv(1024)
    if not data:
        break
    if _END in data:
        alldata += data[:data.find(_END)]
        break
    alldata += data
# process data
alldata = alldata.split('\0')
alldata.remove('')  # remove trailing blank line from alldata
print alldata
