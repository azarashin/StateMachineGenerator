from code_filter import filter_code

from state import StateManager

class StateMachineGenerator:
    
    def __init__(self):
        self._tab = ' ' * 4
    
    def generate(self, pumls):
        return {
            'file_path': 'source_body', 
            'file_path2': 'source_body2', 
            'file_path3': 'source_body3', 
            'file_path4': 'source_body4', 
            'ConsoleOutControllee.cs': 'source_body4', 
            }

    def generate_for_puml(self, puml_body, generator):
        lines = filter_code(puml_body).split('\n')
        if len(lines) <= 2:
            return (False, 'puml does not contains @startuml or/and @enduml.')
        if lines[0] != '@startuml':
            return (False, 'beginning of puml does not match to @startuml.')
        if lines[-1] != '@enduml':
            return (False, 'end of puml does not match to @enduml.')
        state_manager = StateManager(puml_body)
        state_dic = state_manager.get_state_dic()
        transitions = state_manager.get_transitions()
        initial = state_manager.get_initial()
        files = generator.generate_files(state_dic, transitions, initial)
        files = {d: files[d].replace('\t', self._tab) for d in files}
        return files
