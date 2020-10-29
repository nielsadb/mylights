
from typing import Union, Dict
from bridge import Bridge

PluginParams = Dict[str, Union[str, bool]]

class MyLights:
  __slots__ = ('_params', '_result', '_input', '_bridge')
  _params : PluginParams
  _bridge : Bridge

  def plugin_params(self) -> PluginParams:
    return self._params
  def input_state(self):
    return self._input
  def set_result(self, result):
    self._result = result
  def result(self):
    return self._result
  def bridge(self) -> Bridge:
    return self._bridge
  def __init__(self, params, input, bridge):
    self._input = input
    self._params = params
    self._result = None
    self._bridge = bridge

def make_globals(mylights:MyLights):
  return {'_mylights':mylights}

def get_mylights(globals) -> MyLights:
  return globals['_mylights']
