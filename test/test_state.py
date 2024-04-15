from state import StateManager

def test_state_01():
    source = """@startuml

[*] --> State1
State1 --> [*]
State1 : this is a string
State1 : this is another string

State1 -> State2
State2 --> [*]

@enduml"""
    state_manager = StateManager(source)
    state_list = state_manager.get_state_list()
    
    assert len(state_list) == 2
    assert 'State1' in state_list
    assert 'State2' in state_list
    assert not 'State' in state_list

    state1 = state_manager.get_state('State1')
    assert state1.name == 'State1'
    assert state1.description == 'this is a string\nthis is another string\n'

    state2 = state_manager.get_state('State2')
    assert state2.name == 'State2'
    assert state2.description == ''

    state = state_manager.get_state('State')
    assert state is None
