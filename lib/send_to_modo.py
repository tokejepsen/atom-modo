import os
import socket

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="file", help="The file")
parser.add_option("-a", "--host", dest="host",
                  help="The host for the connection to Maya")
parser.add_option("-p", "--port", dest="port",
                  help="The port for the connection to Maya")

(options, args) = parser.parse_args()

host = options.host.replace('\'', '')
port = int(options.port)
f = options.file.replace('\'', '')

path = os.path.dirname(__file__)
command = r'@%s' % (os.path.join(path, 'traceback.py'))
command += ' %s' % f

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
    if '> \0' in data:
        alldata += data[:data.find('> \0')]
        break
    alldata += data
# process data
alldata = alldata.split('\0')
alldata.remove('')  # remove trailing blank line from alldata

for line in alldata[1:]:
    print line
