from transition import TransitionManager

def test_initial_transition_01():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition('[*] --> State1')
    assert transition is not None
    assert transition.state_to == 'State1'
    assert transition.transition_type == '-->'

def test_initial_transition_02():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition(' [*]  ->  State2  ')
    assert transition is not None
    assert transition.state_to == 'State2'
    assert transition.transition_type == '->'

def test_initial_transition_03():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition(' [*]  - -> State3  ')
    assert transition is None

def test_initial_transition_04():
    transition_manager = TransitionManager()
    transition = transition_manager.is_initial_transition(' StateX  --> State4  ')
    assert transition is None

def test_transition_no_event_no_action_01():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX1->StateY1')
    assert transition is not None
    assert transition.state_from == 'StateX1'
    assert transition.state_to == 'StateY1'
    assert transition.transition_type == '->'
    assert transition.event is None
    assert transition.action is None

def test_transition_no_event_no_action_02():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2  ')
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event is None
    assert transition.action is None

def test_transition_no_event_no_action_03():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX3  - ->  StateY3  ')
    assert transition is None

def test_transition_no_event_no_action_04():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  [*]  -->  StateY4  ')
    assert transition is None

def test_transition_no_event_no_action_05():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*]')
    assert transition is not None
    assert transition.state_from == 'StateX5'
    assert transition.state_to == '[*]'
    assert transition.transition_type == '->'
    assert transition.event is None
    assert transition.action is None


def test_transition_no_action_01():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX1->StateY1:Event1')
    assert transition is not None
    assert transition.state_from == 'StateX1'
    assert transition.state_to == 'StateY1'
    assert transition.transition_type == '->'
    assert transition.event == 'Event1'
    assert transition.action is None

def test_transition_no_action_02():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2   :  Event2  ')
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event == 'Event2'
    assert transition.action is None

def test_transition_no_action_03():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX3  - ->  StateY3   : Event3')
    assert transition is None

def test_transition_no_action_04():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  [*]  -->  StateY4  :  Event4')
    assert transition is None

def test_transition_no_action_05():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*]:Event5')
    assert transition is not None
    assert transition.state_from == 'StateX5'
    assert transition.state_to == '[*]'
    assert transition.transition_type == '->'
    assert transition.event == 'Event5'
    assert transition.action is None

def test_transition_01():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX1->StateY1:Event1/Action1')
    assert transition is not None
    assert transition.state_from == 'StateX1'
    assert transition.state_to == 'StateY1'
    assert transition.transition_type == '->'
    assert transition.event == 'Event1'
    assert transition.action == 'Action1'

def test_transition_02():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX2  -->  StateY2   :  Event2  /  Action2')
    assert transition is not None
    assert transition.state_from == 'StateX2'
    assert transition.state_to == 'StateY2'
    assert transition.transition_type == '-->'
    assert transition.event == 'Event2'
    assert transition.action == 'Action2'

def test_transition_03():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  StateX3  - ->  StateY3   : Event3 / Action3')
    assert transition is None

def test_transition_04():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('  [*]  -->  StateY4  :  Event4 / Action4')
    assert transition is None

def test_transition_05():
    transition_manager = TransitionManager()
    transition = transition_manager.is_transition('StateX5->[*]:Event5/Action5')
    assert transition is not None
    assert transition.state_from == 'StateX5'
    assert transition.state_to == '[*]'
    assert transition.transition_type == '->'
    assert transition.event == 'Event5'
    assert transition.action == 'Action5'
