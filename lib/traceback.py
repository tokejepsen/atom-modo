# python
import traceback
import __main__

import lx

args = lx.args()

namespace = __main__.__dict__.get('_atom_maya_plugin_SendToModo')
if not namespace:
    namespace = __main__.__dict__.copy()
    __main__.__dict__['_atom_maya_plugin_SendToModo'] = namespace

namespace['__file__'] = args[0]

try:
    execfile(args[0], namespace, namespace)
except:
    traceback.print_exc()
