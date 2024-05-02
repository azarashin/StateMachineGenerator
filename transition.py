import re

class Transition:
    def __init__(self, state_from, state_to, transition_type, history, event, action):
        self.state_from = state_from
        self.state_to = state_to
        self.transition_type = transition_type
        self.history = history
        self.event = event
        self.action = action
        
    def get_event_as_key(self):
        if self.event is None:
            return '_'
        return self.event
            
            

class TransitionManager:
    
    def __init__(self):
        self._initial_transition = re.compile("\s*\[\*\]\s*(-+>)\s*(\w*)(\[H\]|\[H\*\]|)\s*$")
        self._transition_no_event_no_action = re.compile("\s*(\w+)\s*(-+>)\s*(\w*|\[\*\])(\[H\]|\[H\*\]|)\s*$")
        self._transition_no_event = re.compile("\s*(\w+)\s*(-+>)\s*(\w*|\[\*\])(\[H\]|\[H\*\]|)\s*:\s*/\s*(\w+)\s*$")
        self._transition_no_action = re.compile("\s*(\w+)\s*(-+>)\s*(\w*|\[\*\])(\[H\]|\[H\*\]|)\s*:\s*(\w+)\s*$")
        self._transition = re.compile("\s*(\w+)\s*(-+>)\s*(\w*|\[\*\])(\[H\]|\[H\*\]|)\s*:\s*(\w+)\s*/\s*(\w+)\s*$")

    def is_initial_transition(self, line):
        m = self._initial_transition.search(line)
        if m:
            state_from = None
            state_to = m.group(2)
            transition = m.group(1)
            history = m.group(3)
            event = None
            action = None
            if history.strip() == '':
                history = None
            return Transition(state_from, state_to, transition, history, event, action)
        return None

    def is_transition(self, line):
        state_from = None
        m0 = self._transition_no_event_no_action.search(line)
        if m0:
            state_from = m0.group(1)
            state_to = m0.group(3)
            transition = m0.group(2)
            history = m0.group(4)
            event = ''
            action = ''
        m1 = self._transition_no_action.search(line)
        if m1:
            state_from = m1.group(1)
            state_to = m1.group(3)
            transition = m1.group(2)
            history = m1.group(4)
            event = m1.group(5)
            action = ''
        m2 = self._transition_no_event.search(line)
        if m2:
            state_from = m2.group(1)
            state_to = m2.group(3)
            transition = m2.group(2)
            history = m2.group(4)
            event = ''
            action = m2.group(5)
        m3 = self._transition.search(line)
        if m3:
            state_from = m3.group(1)
            state_to = m3.group(3)
            transition = m3.group(2)
            history = m3.group(4)
            event = m3.group(5)
            action = m3.group(6)
        if state_from:
            if state_to.strip() == '':
                state_to = None
            if event.strip() == '':
                event = None
            if action.strip() == '':
                action = None
            if history.strip() == '':
                history = None
            if history is not None and state_to == '[*]':
                return None
            return Transition(state_from, state_to, transition, history, event, action)
        return None
