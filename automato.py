# arquivo para o automato

from automaton import machines

m = machines.FiniteMachine()

def prototipo():
    m.add_state('up')
    m.add_state('down')
    m.add_transition('down', 'up', 'jump')
    m.add_transition('up', 'down', 'fall')
    m.default_start_state = 'down'
    return print(m.pformat())