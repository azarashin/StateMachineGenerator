import re
from transition import TransitionManager, Transition

class State:
    def __init__(self, name, parent):
        self.name = name; 
        self.description = ''
        self.parent = parent
        self.children = []
        if parent is not None:
            parent.children.append(self)
        self.initial_state = None
        
    def get_full_name(self):
        if self.parent is None: 
            return self.name
        return f'{self.parent.get_full_name()}.{self.name}'
    
class StateManager: 
    def __init__(self, source):
        pattern_state_description = re.compile("^\s*(\w+)\s*:\s*(.*)$")
        pattern_start_of_sub_state = re.compile("^\s*state\s+(\w+)\s*{\s*$")
        pattern_end_of_sub_state = re.compile("^\s*}\s*$")
        transition_manager = TransitionManager()
        self._dic = {}
        self._transitions = []
        self.initial_state = None
        lines = source.split('\n')
        parent = None
        for line in lines:
            m_start_of_sub_state = pattern_start_of_sub_state.search(line)
            if m_start_of_sub_state:
                new_state = m_start_of_sub_state.group(1)
                self._setup_state(new_state, parent)
                parent = self.get_state(new_state)

            m_end_of_sub_state = pattern_end_of_sub_state.search(line)
            if m_end_of_sub_state:
                parent = parent.parent
            
            
            transition = transition_manager.is_initial_transition(line)
            if transition:
                initial = self._setup_state(transition.state_to, parent)
                if parent is None:
                    self.initial_state = transition.state_to
                else:
                    parent.initial_state = initial.name
                if not self._contains_transition(transition, self._transitions):
                    self._transitions.append(transition)
                
            transition = transition_manager.is_transition(line)
            if transition:
                self._setup_state(transition.state_from, parent)
                self._setup_state(transition.state_to, parent)
                if not self._contains_transition(transition, self._transitions):
                    self._transitions.append(transition)

            m = pattern_state_description.search(line)
            if m:
                state_name = m.group(1)
                state_description = m.group(2)
                self._setup_state(state_name, parent)
                self._dic[state_name].description += f'{state_description}\n'

    def _contains_transition(self, target_transition, all_transition):
        for transition in all_transition:
            if transition.state_from == target_transition.state_from and transition.state_to == target_transition.state_to:
                return True
        return False
                    
    def _setup_state(self, name, parent):
        if name != '[*]' and not name in self._dic:
            self._dic[name] = State(name, parent)
        if name in self._dic and self._dic[name].parent is None:
            pass # self._dic[name].parent will not be overwritten by parent. 
        if name in self._dic:
            return self._dic[name]
        return None
            
    def get_state_dic(self):
        return self._dic
                
    def get_state(self, name):
        if name in self._dic:
            return self._dic[name]
        return None
    
    def get_transitions(self):
        return self._transitions + self._get_inherited_transitions()
    
    def get_initial(self):
        return self.initial_state
    
    def _get_inherited_transitions(self):
        ret = []
        for transition in self._transitions:
            if transition.state_from:
                start = self._dic[transition.state_from]
                children = self._get_children(start)
                ret += [Transition(d.name, transition.state_to, transition.transition_type, transition.event, transition.action) for d in children]
        return ret

    def _get_children(self, parent):
        ret = [] + parent.children
        for child in parent.children:
            ret += self._get_children(child)
        return ret
    
    def get_parent_list(self):
        return list(set([self._dic[d].parent for d in self._dic if self._dic[d].parent is not None]))
            
