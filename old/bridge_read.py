from log import get_logger
import plugin

mylights = plugin.get_mylights(globals())
log = get_logger('read_bridge')

result = {}
for section in "lights groups schedules scenes sensors rules".split(' '):
  result[section] = mylights.bridge().api('GET', section)
mylights.set_result(result)
