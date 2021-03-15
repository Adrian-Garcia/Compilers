from state import State

class Grammar():
  def __init__(self, file_name):
    self.file_name = file_name
    self.states = []
    self.names = []
    self.first = []
    self.follow = []

  def print_grammar(self):
    for State in self.states:
      State.print_State()

  def first(self):
    pass

  def follow(self):
    pass

  def get_option_number(self):
    size = 0
    for state in self.states:
      size += len(state.sub_grammar)

    return size

  def read(self):
    file = open(self.file_name)

    while True:
      line = file.readline()

      if line:
        statements = line.split()

        curr_sub_grammar = []
        option = []

        name = statements[0]

        for index, statement in enumerate(statements):
          if index == 0:
            self.names.append(statement)
          elif statement == '->':
            continue
          elif statement != '|':
            option.append(statement)
          else:
            curr_sub_grammar.append(option)
            option = []

        if len(option):
          curr_sub_grammar.append(option)

        curr_state = State(name, curr_sub_grammar)

        self.states.append(curr_state)

      else:
        break
