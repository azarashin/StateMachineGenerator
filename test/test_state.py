from state import StateManager

    
def find_transition(transitions, state_from, state_to, event, action):
    return len([d for d in transitions if d.state_from == state_from and d.state_to == state_to and d.event == event and d.action == action]) == 1

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
    state_list = state_manager.get_state_dic().keys()
    
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

def test_state_02():
    source = """@startuml
scale 350 width
[*] --> Initial


state NotShooting {
  [*] --> Idle
  Idle --> Configuring : EvConfig / Action1
  Configuring --> Idle : EvConfig / Action2
}

Initial --> NotShooting : GoInTo / Action0

NotShooting --> Escaped : Escape / Action3

@enduml
"""
    state_manager = StateManager(source)
    state_list = state_manager.get_state_dic().keys()
    
    assert len(state_list) == 5
    assert 'Initial' in state_list
    assert 'Idle' in state_list
    assert 'Configuring' in state_list
    assert 'NotShooting' in state_list
    assert 'Escaped' in state_list

    initial = state_manager.get_state('Initial')
    idle = state_manager.get_state('Idle')
    configuring = state_manager.get_state('Configuring')
    not_shooting = state_manager.get_state('NotShooting')
    escaped = state_manager.get_state('Escaped')

    assert initial.name == 'Initial'
    assert initial.parent is None
    assert len(initial.children) == 0

    assert idle.name == 'Idle'
    assert idle.parent == not_shooting
    assert len(idle.children) == 0

    assert configuring.name == 'Configuring'
    assert configuring.parent == not_shooting
    assert len(configuring.children) == 0

    assert not_shooting.name == 'NotShooting'
    assert not_shooting.parent is None
    assert len(not_shooting.children) == 2
    assert idle in not_shooting.children
    assert configuring in not_shooting.children

    assert escaped.name == 'Escaped'
    assert escaped.parent is None
    assert len(escaped.children) == 0

def test_state_03():
    source = """@startuml
scale 350 width
[*] --> Initial

Configuring --> Idle : EvConfig / Action2

state NotShooting {
  [*] --> Idle
  Idle --> Configuring : EvConfig / Action1
}


Initial --> NotShooting : GoInTo / Action0

NotShooting --> Escaped : Escape / Action3

@enduml
"""
    state_manager = StateManager(source)
    state_list = state_manager.get_state_dic().keys()
    
    assert len(state_list) == 5
    assert 'Initial' in state_list
    assert 'Idle' in state_list
    assert 'Configuring' in state_list
    assert 'NotShooting' in state_list
    assert 'Escaped' in state_list

    initial = state_manager.get_state('Initial')
    idle = state_manager.get_state('Idle')
    configuring = state_manager.get_state('Configuring')
    not_shooting = state_manager.get_state('NotShooting')
    escaped = state_manager.get_state('Escaped')

    assert initial.name == 'Initial'
    assert initial.parent is None
    assert len(initial.children) == 0
    assert initial.initial_state is None

    assert idle.name == 'Idle'
    assert idle.parent is None
    assert len(idle.children) == 0
    assert idle.initial_state is None

    assert configuring.name == 'Configuring'
    assert configuring.parent is None
    assert len(configuring.children) == 0
    assert configuring.initial_state is None

    assert not_shooting.name == 'NotShooting'
    assert not_shooting.parent is None
    assert len(not_shooting.children) == 0
    assert not_shooting.initial_state == 'Idle'

    assert escaped.name == 'Escaped'
    assert escaped.parent is None
    assert len(escaped.children) == 0
    assert escaped.initial_state is None

def test_state_04():
    source = """@startuml
[*] --> Initial

Initial --> Second : Command1 / Action1

state Second {
  [*] --> IdleSecond
  state Third {
    [*] --> IdleThird
  }
  IdleSecond --> Third : Command2 / Action2
}

Second --> Escaped : Command3 / Action3

@enduml
"""
    state_manager = StateManager(source)
    state_list = state_manager.get_state_dic().keys()
    
    assert len(state_list) == 6
    assert 'Initial' in state_list
    assert 'Second' in state_list
    assert 'Third' in state_list
    assert 'Escaped' in state_list
    assert 'IdleSecond' in state_list
    assert 'IdleThird' in state_list

    initial = state_manager.get_state('Initial')
    second = state_manager.get_state('Second')
    third = state_manager.get_state('Third')
    escaped = state_manager.get_state('Escaped')
    idle_second = state_manager.get_state('IdleSecond')
    idle_third = state_manager.get_state('IdleThird')

    assert initial.name == 'Initial'
    assert initial.parent is None
    assert len(initial.children) == 0
    assert initial.initial_state is None

    assert second.name == 'Second'
    assert second.parent is None
    assert len(second.children) == 2 # Third, IdleSecond
    assert second.initial_state == 'IdleSecond'

    assert third.name == 'Third'
    assert third.parent == second
    assert len(third.children) == 1 # IdleThird
    assert third.initial_state == 'IdleThird'

    assert escaped.name == 'Escaped'
    assert escaped.parent is None
    assert len(escaped.children) == 0
    assert escaped.initial_state is None

    assert idle_second.name == 'IdleSecond'
    assert idle_second.parent == second
    assert len(idle_second.children) == 0
    assert idle_second.initial_state is None

    assert idle_third.name == 'IdleThird'
    assert idle_third.parent is third
    assert len(idle_third.children) == 0
    assert idle_third.initial_state is None

    transitions = state_manager.get_transitions()
    assert len(transitions) == 9
    assert find_transition(transitions, 'Initial', 'Second', 'Command1', 'Action1')
    assert find_transition(transitions, 'IdleSecond', 'Third', 'Command2', 'Action2')
    assert find_transition(transitions, 'Second', 'Escaped', 'Command3', 'Action3')
    assert not find_transition(transitions, 'IdleSecond', 'Escaped', 'Command3', 'Action3')
    assert not find_transition(transitions, 'Third', 'Escaped', 'Command3', 'Action3')
    assert not find_transition(transitions, 'IdleThird', 'Escaped', 'Command3', 'Action3')
    assert find_transition(transitions, None, 'Initial', None, None)
    assert find_transition(transitions, None, 'IdleSecond', None, None)
    assert find_transition(transitions, None, 'IdleThird', None, None)
