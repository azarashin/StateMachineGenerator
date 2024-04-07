import re

class Transition:
    def __init__(self, state_from, state_to, transition_type, event, action):
        self.state_from = state_from
        self.state_to = state_to
        self.transition_type = transition_type
        self.event = event
        self.action = action

class TransitionManager:
    
    def __init__(self):
        self._initial_transition = re.compile("\s*\[\*\]\s*(-+>)\s*(\w+)\s*$")
        self._transition_no_event_no_action = re.compile("\s*(\w+)\s*(-+>)\s*(\w+|\[\*\])\s*$")
        self._transition_no_action = re.compile("\s*(\w+)\s*(-+>)\s*(\w+|\[\*\])\s*:\s*(\w+)\s*$")
        self._transition = re.compile("\s*(\w+)\s*(-+>)\s*(\w+|\[\*\])\s*:\s*(\w+)\s*/\s*(\w+)\s*$")

    def is_initial_transition(self, line):
        m = self._initial_transition.search(line)
        if m:
            return Transition(None, m.group(2), m.group(1), None, None)
        return None

    def is_transition(self, line):
        m0 = self._transition_no_event_no_action.search(line)
        if m0:
            return Transition(m0.group(1), m0.group(3), m0.group(2), None, None)
        m1 = self._transition_no_action.search(line)
        if m1:
            return Transition(m1.group(1), m1.group(3), m1.group(2), m1.group(4), None)
        m2 = self._transition.search(line)
        if m2:
            return Transition(m2.group(1), m2.group(3), m2.group(2), m2.group(4), m2.group(5))
        return None
