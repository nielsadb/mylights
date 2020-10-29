

def split_on(seq, f):
  collected = []
  for x in seq:
    if f(x):
      if len(collected) > 0:
        yield collected
      collected = [x]
    else:
      collected.append(x)
  if len(collected) > 0:
    yield collected
