# python
import traceback
import __main__

import lx

args = lx.args()

print args

'''
namespace = __main__.__dict__.get('_atom_maya_plugin_SendToMaya')
if not namespace:
    namespace = __main__.__dict__.copy()
    __main__.__dict__['_atom_maya_plugin_SendToMaya'] = namespace

namespace['__file__'] = {2!r}

try:
    {0}({1!r}, namespace, namespace)
except:
    traceback.print_exc()
'''
