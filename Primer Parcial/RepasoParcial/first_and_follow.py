from grammar import Grammar

my_grammar = Grammar("grammar.txt")
my_grammar.read()
my_grammar.print_grammar()
print(my_grammar.get_option_number())
