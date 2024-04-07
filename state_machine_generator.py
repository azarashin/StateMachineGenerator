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
        lines = filter_code(open(puml, 'r')).split('\n')
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

