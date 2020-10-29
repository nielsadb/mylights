#
# Hue light API:
# https://developers.meethue.com/develop/hue-api/
#
# Sample implementation:
# https://github.com/studioimaginaire/phue/blob/master/phue.py
#

from log import get_logger, MyLightException
import requests
import json
from ipaddress import IPv4Address, IPv6Address
import logging
from typing import Union, Literal, Optional

log = get_logger('bridge')

IpAddr = Union[IPv4Address, IPv6Address]
HTTPMethod = Literal['GET', 'POST', 'PUT']

class Bridge(object):
  __slots__ = ('_ip', '_username')
  _ip: IpAddr
  _username: str

  def api(self, method:HTTPMethod, resource, *, data=None):
    url = f"http://{self._ip}/api/{self._username}/{resource}"
    if data:
      data = json.dumps(data)
    log.debug(f'HTTP {method} {url} with data {data}')
    if method == 'GET':
      r = requests.get(url)
    elif method == 'POST':
      r = requests.post(url, data=data)
    elif method == 'PUT':
      r = requests.put(url, data=data)
    log.debug(f'--> {r.status_code}: {r.text}')
    return r.json()

  def _register(self):
    url = f"http://{self._ip}/api/"
    data = json.dumps({'devicetype':'mylights#macbook niels'})
    log.debug(f'HTTP POST {url} with data {data}')
    r = requests.post(url, data=data)
    log.debug(f'--> {r.status_code}: {r.text}')
    reply = r.json()[0]
    if 'success' in reply:
      return reply['success']['username']

  def __repr__(self):
    return f"<Bridge ip:{self._ip} username:{self._username}>"

  def __init__(self, *, ip:IpAddr, username=None, cache=None):
    self._ip = ip
    if username is None and cache is not None:
      username = cache.read()
    if username is None:
      username = self._register()
      if username is not None and cache is not None:
        cache.write(username)
    if username is None:
      raise log.MyLightException("Failed to register. Press the button first.")
    self._username = username

class FileCache(object):
  def read(self) -> Optional[str]:
    try:
      with open(self._filename, 'r', encoding='utf-8') as f:
        return f.read()
    except FileNotFoundError:
      log.info(f'Failed to load file {self._filename}.')
    return None
  def write(self, str:str):
    try:
      with open(self._filename, 'w', encoding='utf-8') as f:
        f.write(str)
    except:
      log.info(f'Failed to write to file {self._filename}.') 
  def __init__(self, filename):
    self._filename = filename
