
from pprint import PrettyPrinter
from bridge_api import get_api

pp = PrettyPrinter(indent=2)

username = "tErioA8acfVFttduV35u7-apCQJgh20fZtOBBqZ5"
ip = '192.168.1.10'

api = get_api(ip, username)

# night2 = 'w3NrHOv81te4DTQ'
# evening = 'xiS2f8OOclUk-jX'
# api('PUT', 'groups/0/action', {'scene': evening})
