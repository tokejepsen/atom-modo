import socket
import sys
import textwrap
from optparse import OptionParser

'''
parser = OptionParser()
parser.add_option("-f", "--file", dest="file", help="The file")
parser.add_option("-a", "--host", dest="host", help="The host for the connection to Modo")
parser.add_option("-p", "--port", dest="port", help="The port for the connection to Modo")

(options, args) = parser.parse_args()

def SendToModo(options):

    PY_CMD_TEMPLATE = textwrap.dedent(
        import traceback
        import __main__

        namespace = __main__.__dict__.get('_atom_modo_plugin_SendToModo')
        if not namespace:
            namespace = __main__.__dict__.copy()
            __main__.__dict__['_atom_modo_plugin_SendToModo'] = namespace

        namespace['__file__'] = {2!r}

        try:
            {0}({1!r}, namespace, namespace)
        except:
            traceback.print_exc()
	)

    command_tpl = PY_CMD_TEMPLATE.format('execfile', options.file, options.file)

    host = options.host.replace('\'', '')
    port = int(options.port)

    ADDR = (host, port)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    client.send(command_tpl)
    data = client.recv(1024)

    print(data)

    client.close()

if __name__=='__main__':
    if options.file:
        SendToModo(options)
    else:
        sys.exit("No command given")
'''

import socket

HOST = '127.0.0.1' # the local host
PORT = 12357 # The same port as used by the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
command = 'item.create locator'

client.sendall('%s\0' % command)
print client.recv(1024)
