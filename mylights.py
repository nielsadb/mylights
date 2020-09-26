#!/usr/bin/env python3

import sys
import runpy
import plugin
from util import split_on
from log import get_logger
from typing import Optional
from bridge import Bridge, FileCache
from ipaddress import IPv4Address

log = get_logger('mylights(main)')

def run_plugin(name, params, state, bridge):
    file = name + '.py'
    init_globals = plugin.make_globals(plugin.MyLights(params, state, bridge))
    returned_globals = runpy.run_path(file, init_globals=init_globals)
    return plugin.get_mylights(returned_globals).result()

def parse_argv(argv):
  def make_params(pstrs):
    splitps = [p[1:].split('=') for p in pstrs]
    return {sp[0]:(sp[1] if len(sp) > 1 else True) for sp in splitps}
  runs = split_on(argv, lambda s: not s.startswith('-'))
  has_options = len(argv) > 0 and argv[0].startswith('-')
  options = make_params(next(runs)) if has_options else {}
  plugins = [(run[0], make_params(run[1:])) for run in runs]
  return options, plugins

def main(argv):  
  options, plugins = parse_argv(argv)
  print(f'{options=}')
  state = {}
  bridge = Bridge(ip=IPv4Address('192.168.1.10'), cache=FileCache('username.txt'))
  for name, params in plugins:
    state = run_plugin(name, params, state, bridge) or state

if __name__ == '__main__':
  main(sys.argv[1:])
