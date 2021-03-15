class State():
  def __init__(self, name, sub_grammar):
    self.name = name
    self.sub_grammar = sub_grammar

  def print_State(self):
    print("Nombre del estado:\t{} \nSub Gramatica:\t\t{}\n".format(self.name, self.sub_grammar_decorator()))

  def sub_grammar_decorator(self):
    result = ""
    for i in self.sub_grammar:
      for j in i:
        result += j+" "
      result += "| "

    return result[:-2]
