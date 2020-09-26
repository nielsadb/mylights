from log import get_logger
import plugin
from pprint import PrettyPrinter

mylights = plugin.get_mylights(globals())
log = get_logger('print_state')
pp = PrettyPrinter(indent=2)

pp.pprint(mylights.input_state())
