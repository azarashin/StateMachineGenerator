import re
from transition import TransitionManager

class State:
    def __init__(self, name):
        self.name = name; 
        self.description = ''
    
class StateManager: 
    def __init__(self, source):
        pattern_state_description = re.compile("\s*(\w+)\s*:\s*(.*)$")
        transition_manager = TransitionManager()
        self._dic = {}
        lines = source.split('\n')
        for line in lines:
            transition = transition_manager.is_initial_transition(line)
            if transition:
                self._setup_state(transition.state_to)
                
            transition = transition_manager.is_transition(line)
            if transition:
                self._setup_state(transition.state_from)
                self._setup_state(transition.state_to)

            m = pattern_state_description.search(line)
            if m:
                state_name = m.group(1)
                state_description = m.group(2)
                self._setup_state(state_name)
                self._dic[state_name].description += f'{state_description}\n'
                    
    def _setup_state(self, name):
        if name != '[*]' and not name in self._dic:
            self._dic[name] = State(name)
            
    def get_state_list(self):
        return self._dic.keys()
                
    def get_state(self, name):
        if name in self._dic:
            return self._dic[name]
        return None
            
