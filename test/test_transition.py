from transition import TransitionManager

def test_initial_transition_01():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition('[*] --> State1', None)
    assert transition is not None
    assert transition.state_to == 'State1'
    assert transition.transition_type == '-->'
    assert transition.history is None

def test_initial_transition_02():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition(' [*]  ->  State2  ', None)
    assert transition is not None
    assert transition.state_to == 'State2'
    assert transition.transition_type == '->'
    assert transition.history is None

def test_initial_transition_03():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition(' [*]  - -> State3  ', None)
    assert transition is None

def test_initial_transition_04():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition(' StateX  --> State4  ', None)
    assert transition is None

def test_initial_transition_05():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition(' [*]  ->  State2[H]  ', None)
    assert transition is not None
    assert transition.state_to == 'State2'
    assert transition.transition_type == '->'
    assert transition.history == '[H]'

def test_initial_transition_06():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition(' [*]  ->  State2[H*]  ', None)
    assert transition is not None
    assert transition.state_to == 'State2'
    assert transition.transition_type == '->'
    assert transition.history == '[H*]'

def test_initial_transition_07():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition(' [*]  ->  [*][H]  ', None)
    assert transition is None

def test_initial_transition_08():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition(' [*]  ->  [*][H*]  ', None)
    assert transition is None

def test_initial_transition_09():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition(' [*]  ->  [H]  ', 'Parent')
    assert transition is not None
    assert transition.state_to == 'Parent'
    assert transition.transition_type == '->'
    assert transition.history == '[H]'

def test_initial_transition_10():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition(' [*]  ->  [H*]  ', 'Parent')
    assert transition is not None
    assert transition.state_to == 'Parent'
    assert transition.transition_type == '->'
    assert transition.history == '[H*]'

def test_initial_transition_11():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition(' [*]  ->  [H]  ', None)
    assert transition is None

def test_initial_transition_12():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition(' [*]  ->  [H*]  ', None)
    assert transition is None


def test_transition_no_event_no_action_01():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX1->StateY1', None)
    assert transition is not None
    assert transition.state_from == 'StateX1'
    assert transition.state_to == 'StateY1'
    assert transition.transition_type == '->'
    assert transition.event is None
    assert transition.action is None
    assert transition.history is None

def test_transition_no_event_no_action_02():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2  ', None)
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event is None
    assert transition.action is None
    assert transition.history is None

def test_transition_no_event_no_action_03():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX3  - ->  StateY3  ', None)
    assert transition is None

def test_transition_no_event_no_action_04():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  [*]  -->  StateY4  ', None)
    assert transition is None

def test_transition_no_event_no_action_05():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*]', None)
    assert transition is not None
    assert transition.state_from == 'StateX5'
    assert transition.state_to == '[*]'
    assert transition.transition_type == '->'
    assert transition.event is None
    assert transition.action is None
    assert transition.history is None

def test_transition_no_event_no_action_06():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2[H]  ', None)
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event is None
    assert transition.action is None
    assert transition.history == '[H]'

def test_transition_no_event_no_action_07():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2[H*]  ', None)
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event is None
    assert transition.action is None
    assert transition.history == '[H*]'

def test_transition_no_event_no_action_08():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*][H]', None)
    assert transition is None

def test_transition_no_event_no_action_09():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*][H*]', None)
    assert transition is None

def test_transition_no_event_no_action_10():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H]  ', 'Parent')
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'Parent'
    assert transition.transition_type == '-->'
    assert transition.event is None
    assert transition.action is None
    assert transition.history == '[H]'

def test_transition_no_event_no_action_11():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H*]  ', 'Parent')
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'Parent'
    assert transition.transition_type == '-->'
    assert transition.event is None
    assert transition.action is None
    assert transition.history == '[H*]'

def test_transition_no_event_no_action_12():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H]  ', None)
    assert transition is None

def test_transition_no_event_no_action_13():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H*]  ', None)
    assert transition is None


def test_transition_no_action_01():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX1->StateY1:Event1', None)
    assert transition is not None
    assert transition.state_from == 'StateX1'
    assert transition.state_to == 'StateY1'
    assert transition.transition_type == '->'
    assert transition.event == 'Event1'
    assert transition.action is None

def test_transition_no_action_02():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2   :  Event2  ', None)
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event == 'Event2'
    assert transition.action is None

def test_transition_no_action_03():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX3  - ->  StateY3   : Event3', None)
    assert transition is None

def test_transition_no_action_04():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  [*]  -->  StateY4  :  Event4', None)
    assert transition is None

def test_transition_no_action_05():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*]:Event5', None)
    assert transition is not None
    assert transition.state_from == 'StateX5'
    assert transition.state_to == '[*]'
    assert transition.transition_type == '->'
    assert transition.event == 'Event5'
    assert transition.action is None

def test_transition_no_action_06():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2[H] : Event ', None)
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event == 'Event'
    assert transition.action is None
    assert transition.history == '[H]'

def test_transition_no_action_07():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2[H*] : Event   ', None)
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event == 'Event'
    assert transition.action is None
    assert transition.history == '[H*]'

def test_transition_no_action_08():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*][H] : Event ', None)
    assert transition is None

def test_transition_no_action_09():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*][H*] : Event ', None)
    assert transition is None

def test_transition_no_action_10():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H] : Event ', 'Parent')
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'Parent'
    assert transition.transition_type == '-->'
    assert transition.event == 'Event'
    assert transition.action is None
    assert transition.history == '[H]'

def test_transition_no_action_11():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H*] : Event   ', 'Parent')
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'Parent'
    assert transition.transition_type == '-->'
    assert transition.event == 'Event'
    assert transition.action is None
    assert transition.history == '[H*]'

def test_transition_no_action_12():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H] : Event ', None)
    assert transition is None

def test_transition_no_action_13():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H*] : Event   ', None)
    assert transition is None


def test_transition_no_event_01():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX1->StateY1:/Action1', None)
    assert transition is not None
    assert transition.state_from == 'StateX1'
    assert transition.state_to == 'StateY1'
    assert transition.transition_type == '->'
    assert transition.event is None
    assert transition.action == 'Action1'

def test_transition_no_event_02():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2   :  /Action2  ', None)
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event is None
    assert transition.action == 'Action2'

def test_transition_no_event_03():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX3  - ->  StateY3   : /Action3', None)
    assert transition is None

def test_transition_no_event_04():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  [*]  -->  StateY4  :  /Action4', None)
    assert transition is None

def test_transition_no_event_05():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*]:/Action5', None)
    assert transition is not None
    assert transition.state_from == 'StateX5'
    assert transition.state_to == '[*]'
    assert transition.transition_type == '->'
    assert transition.event is None
    assert transition.action == 'Action5'

def test_transition_no_event_06():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2[H] : /Action ', None)
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event is None
    assert transition.action == 'Action'
    assert transition.history == '[H]'

def test_transition_no_event_07():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2[H*] : / Action ', None)
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event is None
    assert transition.action == 'Action'
    assert transition.history == '[H*]'

def test_transition_no_event_08():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*][H] : / Action ', None)
    assert transition is None

def test_transition_no_event_09():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*][H*] : / Action ', None)
    assert transition is None

def test_transition_no_event_10():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H] : /Action ', 'Parent')
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'Parent'
    assert transition.transition_type == '-->'
    assert transition.event is None
    assert transition.action == 'Action'
    assert transition.history == '[H]'

def test_transition_no_event_11():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H*] : / Action ', 'Parent')
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'Parent'
    assert transition.transition_type == '-->'
    assert transition.event is None
    assert transition.action == 'Action'
    assert transition.history == '[H*]'

def test_transition_no_event_12():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H] : /Action ', None)
    assert transition is None

def test_transition_no_event_13():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H*] : / Action ', None)
    assert transition is None


def test_transition_01():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX1->StateY1:Event1/Action1', None)
    assert transition is not None
    assert transition.state_from == 'StateX1'
    assert transition.state_to == 'StateY1'
    assert transition.transition_type == '->'
    assert transition.event == 'Event1'
    assert transition.action == 'Action1'

def test_transition_02():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2   :  Event2  /  Action2', None)
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event == 'Event2'
    assert transition.action == 'Action2'

def test_transition_03():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX3  - ->  StateY3   : Event3 / Action3', None)
    assert transition is None

def test_transition_04():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  [*]  -->  StateY4  :  Event4 / Action4', None)
    assert transition is None

def test_transition_05():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*]:Event5/Action5', None)
    assert transition is not None
    assert transition.state_from == 'StateX5'
    assert transition.state_to == '[*]'
    assert transition.transition_type == '->'
    assert transition.event == 'Event5'
    assert transition.action == 'Action5'

def test_transition_06():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2[H] : Event/Action ', None)
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event == 'Event'
    assert transition.action == 'Action'
    assert transition.history == '[H]'

def test_transition_07():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2[H*] : Event / Action ', None)
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event == 'Event'
    assert transition.action == 'Action'
    assert transition.history == '[H*]'

def test_transition_08():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*][H] : Event / Action ', None)
    assert transition is None

def test_transition_09():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*][H*] : Event / Action ', None)
    assert transition is None

def test_transition_10():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H] : Event/Action ', 'Parent')
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'Parent'
    assert transition.transition_type == '-->'
    assert transition.event == 'Event'
    assert transition.action == 'Action'
    assert transition.history == '[H]'

def test_transition_11():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H*] : Event / Action ', 'Parent')
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'Parent'
    assert transition.transition_type == '-->'
    assert transition.event == 'Event'
    assert transition.action == 'Action'
    assert transition.history == '[H*]'

def test_transition_12():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H] : Event/Action ', None)
    assert transition is None

def test_transition_13():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  [H*] : Event / Action ', None)
    assert transition is None
