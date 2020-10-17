
from types import GeneratorType, TupleType

def where(condition):
  def f(xs):
    if type(xs) == GeneratorType:
      return (x for x in xs if condition(x))
    else:
      return 
  return f

def select(element):
  def f():
    pass
  return f

def query(text):
  pass

query('/lights[@name="Woon Kap"]/$')