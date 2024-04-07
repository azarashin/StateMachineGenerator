from state_machine_generator import StateMachineGenerator

def test_initial_transition_01():
    gen = StateMachineGenerator()
    result, state, transition = gen.is_initial_transition('[*] --> State1')
    assert result
    assert state == 'State1'
    assert transition == '-->'

def test_initial_transition_02():
    gen = StateMachineGenerator()
    result, state, transition = gen.is_initial_transition(' [*]  ->  State2  ')
    assert result
    assert state == 'State2'
    assert transition == '->'

def test_initial_transition_03():
    gen = StateMachineGenerator()
    result, _, _ = gen.is_initial_transition(' [*]  - -> State3  ')
    assert not result

def test_initial_transition_04():
    gen = StateMachineGenerator()
    result, _, _ = gen.is_initial_transition(' StateX  --> State4  ')
    assert not result

def test_transition_no_event_no_action_01():
    gen = StateMachineGenerator()
    result, state_from, state_to, transition, event, action = gen.is_transition('StateX1->StateY1')
    assert result
    assert state_from == 'StateX1'
    assert state_to == 'StateY1'
    assert transition == '->'
    assert event is None
    assert action is None

def test_transition_no_event_no_action_02():
    gen = StateMachineGenerator()
    result, state_from, state_to, transition, event, action = gen.is_transition('  StateX2  -->  StateY2  ')
    assert result
    assert state_from == 'StateX2'
    assert state_to == 'StateY2'
    assert transition == '-->'
    assert event is None
    assert action is None

def test_transition_no_event_no_action_03():
    gen = StateMachineGenerator()
    result, _, _, _, _, _ = gen.is_transition('  StateX3  - ->  StateY3  ')
    assert not result

def test_transition_no_event_no_action_04():
    gen = StateMachineGenerator()
    result, _, _, _, _, _ = gen.is_transition('  [*]  -->  StateY4  ')
    assert not result

def test_transition_no_event_no_action_05():
    gen = StateMachineGenerator()
    result, state_from, state_to, transition, event, action = gen.is_transition('StateX5->[*]')
    assert result
    assert state_from == 'StateX5'
    assert state_to == '[*]'
    assert transition == '->'
    assert event is None
    assert action is None


def test_transition_no_action_01():
    gen = StateMachineGenerator()
    result, state_from, state_to, transition, event, action = gen.is_transition('StateX1->StateY1:Event1')
    assert result
    assert state_from == 'StateX1'
    assert state_to == 'StateY1'
    assert transition == '->'
    assert event == 'Event1'
    assert action is None

def test_transition_no_action_02():
    gen = StateMachineGenerator()
    result, state_from, state_to, transition, event, action = gen.is_transition('  StateX2  -->  StateY2   :  Event2  ')
    assert result
    assert state_from == 'StateX2'
    assert state_to == 'StateY2'
    assert transition == '-->'
    assert event == 'Event2'
    assert action is None

def test_transition_no_action_03():
    gen = StateMachineGenerator()
    result, _, _, _, _, _ = gen.is_transition('  StateX3  - ->  StateY3   : Event3')
    assert not result

def test_transition_no_action_04():
    gen = StateMachineGenerator()
    result, _, _, _, _, _ = gen.is_transition('  [*]  -->  StateY4  :  Event4')
    assert not result

def test_transition_no_action_05():
    gen = StateMachineGenerator()
    result, state_from, state_to, transition, event, action = gen.is_transition('StateX5->[*]:Event5')
    assert result
    assert state_from == 'StateX5'
    assert state_to == '[*]'
    assert transition == '->'
    assert event == 'Event5'
    assert action is None

def test_transition_01():
    gen = StateMachineGenerator()
    result, state_from, state_to, transition, event, action = gen.is_transition('StateX1->StateY1:Event1/Action1')
    assert result
    assert state_from == 'StateX1'
    assert state_to == 'StateY1'
    assert transition == '->'
    assert event == 'Event1'
    assert action == 'Action1'

def test_transition_02():
    gen = StateMachineGenerator()
    result, state_from, state_to, transition, event, action = gen.is_transition('  StateX2  -->  StateY2   :  Event2  /  Action2')
    assert result
    assert state_from == 'StateX2'
    assert state_to == 'StateY2'
    assert transition == '-->'
    assert event == 'Event2'
    assert action == 'Action2'

def test_transition_03():
    gen = StateMachineGenerator()
    result, _, _, _, _, _ = gen.is_transition('  StateX3  - ->  StateY3   : Event3 / Action3')
    assert not result

def test_transition_04():
    gen = StateMachineGenerator()
    result, _, _, _, _, _ = gen.is_transition('  [*]  -->  StateY4  :  Event4 / Action4')
    assert not result

def test_transition_05():
    gen = StateMachineGenerator()
    result, state_from, state_to, transition, event, action = gen.is_transition('StateX5->[*]:Event5/Action5')
    assert result
    assert state_from == 'StateX5'
    assert state_to == '[*]'
    assert transition == '->'
    assert event == 'Event5'
    assert action == 'Action5'
