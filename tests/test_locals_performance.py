
def fun_with_locals():
  def fset():
    pass
  def fget():
    pass
  return locals()

def fun_with_dict():
  def fset():
    pass
  def fget():
    pass
  return {'fset':fset,'fget': fget}



def test_locals_performance():
  import timeit
  t1 = timeit.timeit('fun()',number=100000,  globals={'fun': fun_with_locals})
  t2 = timeit.timeit('fun()',number=100000,  globals={'fun': fun_with_dict})
  print("fun_with_locals:", t1)
  print("fun_with_dict:", t2)
  print("percent:",((t1-t2)/t2)*100)
  assert fun_with_dict().keys() == fun_with_locals().keys()
  assert t2 < t1
