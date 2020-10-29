from pprint import PrettyPrinter
from json import dumps
import plugin

mylights = plugin.get_mylights(globals())
params = mylights.plugin_params()

def message():
  if 'json' in params:
    return dumps(mylights.input_state())
  else:
    pp = PrettyPrinter(indent=2)
    return pp.pprint(mylights.input_state())

if 'file' in params:
  with open(params['file'], 'w') as stream:
    stream.write(message())
else:
  print(message())