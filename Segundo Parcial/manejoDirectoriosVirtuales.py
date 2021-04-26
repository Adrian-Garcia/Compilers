class Var(object):
  def __init__(self, tipo, dirY):
    self.tipo = tipo
    self.dir = dirY

class TablaVars(object):
  def __init__(self):
    self.tabla = {}

class Concepto(object):
  def __init__(self, nombre, size):
    self.nombre = nombre
    self.size = size

class ManejoDirectoriosVirtuales(object):
  def __init__(self, ds, cs, ss, es):
    self.ds = ds  # Data  ->  Global 
    self.cs = cs  # Code  ->  Codigo
    self.ss = ss  # Stack ->  Local
    self.es = es  # Extra ->  Extra
                  #             ↳ Temp

tablaVars = tablaVars

ds = Concepto("Global", 10000)
cs = Concepto("Local", 10000)
ss = Concepto("Total", 15000)
es = Concepto("Cte", 5000)

virtual_dir = ManejoDirectoriosVirtuales(ds, cs, ss, es)
