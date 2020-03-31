#!/usr/bin/env python3

import requests
import logging
import json
import sys

def logger():
  handler = logging.StreamHandler(sys.stderr)
  formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
  handler.setFormatter(formatter)
  log = logging.getLogger('mylights')
  log.addHandler(handler)
  log.setLevel(logging.DEBUG)
  return log

log = logger()

class MyLightException(BaseException):
  def __init__(self, msg):
    self._msg = msg

class Bridge(object):

  def api(self, method, resource, *, data=None):
    url = f"http://{self._ip}/api/{self._username}/{resource}"
    if data:
      data = json.dumps(data)
    log.debug(f'HTTP {method} {url} with data {data}')
    if method == 'GET':
      r = requests.get(url)
    elif method == 'POST':
      r = requests.post(url, data=data)
    else:
      raise TypeError("method must be GET or POST")
    log.debug(f'--> {r.status_code}: {r.text}')
    return r.json()

  def register(self):
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

  def __init__(self, *, ip, username=None, cache=None):
    self._ip = ip
    if username is None and cache is not None:
      username = cache.read()
    if username is None:
      username = self.register()
      if username is not None and cache is not None:
        cache.write(username)
    if username is None:
      raise MyLightException("Failed to register. Press the button first.")
    self._username = username


class FileCache(object):
  def read(self):
    try:
      with open(self._filename, 'r') as f:
        return f.read()
    except FileNotFoundError:
      log.info('Failed to load file {self._filename}.')

  def write(self, str):
    try:
      with open(self._filename, 'w') as f:
        f.write(str)
    except:
      log.info('Failed to write to file {self._filename}.')
    
  def __init__(self, filename):
    self._filename = filename

bridge = Bridge(ip='192.168.1.10', cache=FileCache('username.txt'))

print(bridge)
