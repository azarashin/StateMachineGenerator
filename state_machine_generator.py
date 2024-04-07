from code_filter import filter_code
import re

class StateMachineGenerator:
    
    def __init__(self):
        self._initial_transition = re.compile("\s*\[\*\]\s*(-+>)\s*(\w+)\s*$")
        self._transition_no_event_no_action = re.compile("\s*(\w+)\s*(-+>)\s*(\w+|\[\*\])\s*$")
        self._transition_no_action = re.compile("\s*(\w+)\s*(-+>)\s*(\w+|\[\*\])\s*:\s*(\w+)\s*$")
        self._transition = re.compile("\s*(\w+)\s*(-+>)\s*(\w+|\[\*\])\s*:\s*(\w+)\s*/\s*(\w+)\s*$")
#    "\s*\[\*\]\s*[-−−−>]+\s*(\w+)\s*$"
    def generate(sellf, pumls):
        return {
            'file_path': 'source_body', 
            'file_path2': 'source_body2', 
            'file_path3': 'source_body3', 
            'file_path4': 'source_body4', 
            'ConsoleOutControllee.cs': 'source_body4', 
            }

    def generate_for_puml(sellf, puml):
        lines = filter_code(open(puml, 'r')).split()
        if len(lines):
            return (False, 'puml does not contains @startuml or/and @enduml.')
        if lines[0] != '@startuml':
            return (False, 'beginning of puml does not match to @startuml.')
        if lines[-1] != '@enduml':
            return (False, 'end of puml does not match to @enduml.')
        for line in lines[1:-2]:
            line
        states = []
        transitions = []
        return {
            'file_path': 'source_body', 
            'file_path2': 'source_body2', 
            'file_path3': 'source_body3', 
            'file_path4': 'source_body4', 
            'ConsoleOutControllee.cs': 'source_body4', 
            }

    def is_initial_transition(self, line):
        m = self._initial_transition.search(line)
        if m:
            return (True, m.group(2), m.group(1))
        return (False, None, None)

    def is_transition(self, line):
        m0 = self._transition_no_event_no_action.search(line)
        if m0:
            return (True, m0.group(1), m0.group(3), m0.group(2), None, None)
        m1 = self._transition_no_action.search(line)
        if m1:
            return (True, m1.group(1), m1.group(3), m1.group(2), m1.group(4), None)
        m2 = self._transition.search(line)
        if m2:
            return (True, m2.group(1), m2.group(3), m2.group(2), m2.group(4), m2.group(5))
        return (False, None, None, None, None, None)
