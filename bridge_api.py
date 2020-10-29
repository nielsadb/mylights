
import http.client
import json
from typing import Literal

HTTPMethod = Literal['GET', 'POST', 'PUT']

def _request(ip:str, method:HTTPMethod, path:str, data=None):
  connection = http.client.HTTPConnection(ip, timeout=10)
  if method == 'GET' or method == 'DELETE':
    connection.request(method, path)
  if method == 'PUT' or method == 'POST':
    connection.request(method, path, json.dumps(data))
  response = connection.getresponse().read().decode('utf-8')
  connection.close()
  return json.loads(response)

def get_api(ip:str, username:str):
  def api_call(method:HTTPMethod, api_path:str, data=None):
    if api_path.startswith('/'):
      api_path = api_path[1:]
    return _request(ip, method, f'/api/{username}/{api_path}', data)
  return api_call

def register(ip:str):
  data = json.dumps({'devicetype':'mylights#macbook niels'})
  response = _request(ip, 'POST', '/api', data)
  if 'success' in response:
    return response['success']['username']
