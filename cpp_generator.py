class CPPGenerator:
    def __init__(self, 
                 icontrollee_class_name = 'IControllee', 
                 base_state_class_name = 'BaseState', 
                 state_controller_class_name = 'StateController', 
                 console_controllee_class_name = "ConsoleOutControllee"):
        self._prefix_instance_of = 'InstanceOf'
        self._prefix_method = 'Transit'
        self._prefix_action_method = 'Do'
        self._prefix_execution_action_method = 'Exec'
        self._prefix_state = 'State'
        self._boot_program = 'Program.cpp'
        self._icontrollee_class_name = icontrollee_class_name
        self._base_state_class_name = base_state_class_name
        self._state_controller_class_name = state_controller_class_name
        self._console_controllee_class_name = console_controllee_class_name

    def generate_files(self, state_manager):
        state_dic = state_manager.get_state_dic()
        transitions = state_manager.get_transitions()
        initial = state_manager.get_initial()

        ret = {}
        ret[f'{self._icontrollee_class_name}.h'] = self.generate_controllee_interface(transitions)
        ret[f'{self._base_state_class_name}.cpp'] = self.generate_base_state_cpp(transitions)
        ret[f'{self._base_state_class_name}.h'] = self.generate_base_state_h(transitions)
        ret[f'{self._state_controller_class_name}.cpp'] = self.generate_state_controller_cpp(state_dic, transitions, initial)
        ret[f'{self._state_controller_class_name}.h'] = self.generate_state_controller_h(state_dic, transitions, initial)
        ret[f'{self._console_controllee_class_name}.cpp'] = self.generate_console_out_controllee_cpp(transitions)
        ret[f'{self._console_controllee_class_name}.h'] = self.generate_console_out_controllee_h(transitions)
        ret[self._boot_program] = self.generate_sample_boot_program(transitions)
        state_classes = self.generate_state_classes_cpp(state_manager, state_dic, transitions)
        for state in state_classes:
            ret[f'{self._prefix_state}{state.name}.cpp'] = state_classes[state]
        state_classes = self.generate_state_classes_h(state_manager, state_dic, transitions)
        for state in state_classes:
            ret[f'{self._prefix_state}{state.name}.h'] = state_classes[state]
        return ret
    
    def _transition_method_in_base_state_cpp(self, event):
        return f"""{self._base_state_class_name}* {self._base_state_class_name}::{self._prefix_method}{event}()
{{
\t_controllee->NoTransition(GetStateName(), "{event}");
\treturn this;
}}
"""

    def _transition_method_in_base_state_h(self, event):
        return f"""\tvirtual {self._base_state_class_name}* {self._prefix_method}{event}();
"""
    
    def generate_base_state_cpp(self, transitions):
        event_list = sorted(list(set([d.event for d in transitions if d.event is not None])))
        transition_list = '\n'.join([self._transition_method_in_base_state_cpp(d) for d in event_list])
        ret = f"""#include "{self._base_state_class_name}.h"
        
{self._base_state_class_name}::{self._base_state_class_name}({self._icontrollee_class_name}* controllee)
{{
\t_controllee = controllee;
}}
{self._base_state_class_name}::~{self._base_state_class_name}()
{{

}}
void {self._base_state_class_name}::Setup()
{{
}} 
{transition_list}
{self._base_state_class_name}* {self._base_state_class_name}::TryTransitWithoutEvent()
{{
\treturn this;
}}
void {self._base_state_class_name}::SetupSubState({self._base_state_class_name}* child)
{{
\t_currentSubState = child; 
\tif(_currentSubState != 0)
\t{{
\t\t_currentSubState->Setup();
\t}}
}}
{self._base_state_class_name}* {self._base_state_class_name}::CurrentSubState()
{{
\treturn _currentSubState;
}}
{self._base_state_class_name}* {self._base_state_class_name}::TransitBySubState({self._base_state_class_name}* nextState)
{{
\tif(nextState == 0 || _currentSubState == 0)
\t{{
\t\treturn nextState;
\t}}
\t{self._base_state_class_name}* parentOfNextState = _currentSubState->GetParent();
\t{self._base_state_class_name}* parentOfCurrentState = nextState->GetParent();
\tif(parentOfNextState != 0 && parentOfCurrentState != 0 && parentOfNextState == parentOfCurrentState)
\t{{
\t\t_currentSubState = nextState;
\t\treturn this;
\t}}
\treturn nextState;
}}
{self._base_state_class_name}* {self._base_state_class_name}::TransitForChild({self._base_state_class_name}* child)
{{
\t_currentSubState = child;
\t{self._base_state_class_name}* parent = GetParent();
\tif(parent != 0)
\t{{
\t\treturn parent->TransitForChild(this);
\t}}
\treturn this; 
}}
{self._base_state_class_name}* {self._base_state_class_name}::OutlineState()
{{
\t{self._base_state_class_name}* parent = GetParent();
\tif(parent != 0)
\t{{
\t\treturn parent->TransitForChild(this);
\t}}
\treturn this; 
}}
        """
        return ret

    def generate_base_state_h(self, transitions):
        event_list = sorted(list(set([d.event for d in transitions if d.event is not None])))
        transition_list = '\n'.join([self._transition_method_in_base_state_h(d) for d in event_list])
        ret = f"""#pragma once

#include "{self._icontrollee_class_name}.h"

class {self._base_state_class_name}
{{
private:
\t{self._icontrollee_class_name}* _controllee; 
\t{self._base_state_class_name}* _currentSubState;
public:
\t{self._base_state_class_name}({self._icontrollee_class_name}* controllee);
\tvirtual ~{self._base_state_class_name}();
\tvirtual void Setup(); 
{transition_list}
\tvirtual {self._base_state_class_name}* TryTransitWithoutEvent();
\tvoid SetupSubState({self._base_state_class_name}* child);
\t{self._base_state_class_name}* CurrentSubState();
\t{self._base_state_class_name}* TransitBySubState({self._base_state_class_name}* nextState);
\t{self._base_state_class_name}* TransitForChild({self._base_state_class_name}* child);
\t{self._base_state_class_name}* OutlineState();
\tvirtual const char* GetStateName() = 0;
\tvirtual {self._base_state_class_name}* GetParent() = 0;
}};
        """
        return ret

    def action_method(self, action):
        return f'\tvirtual void {self._prefix_action_method}{action}() = 0;'
        
    def generate_controllee_interface(self, transitions):
        action_transitions = [d for d in transitions if d.action is not None]
        action_name_list = sorted(list(set([d.action for d in action_transitions])))
        action_list = '\n'.join([self.action_method(d) for d in action_name_list])
        ret = f"""#pragma once
        
class {self._icontrollee_class_name}
{{
public: 
{action_list}
\tvirtual void NoTransition(const char* state, const char* transition) = 0;
\tvirtual void OverTransition(const char* transition) = 0;
}};
"""
        return ret

    def console_out_action_method_cpp(self, action):
        return f"""void {self._console_controllee_class_name}::{self._prefix_action_method}{action}()
{{
\tprintf("{action}");
}}
"""

    def console_out_action_method_h(self, action):
        return f"""\tvirtual void {self._prefix_action_method}{action}();
"""

    def generate_console_out_controllee_cpp(self, transitions):
        action_transitions = [d for d in transitions if d.action is not None]
        action_name_list = sorted(list(set([d.action for d in action_transitions])))
        action_list = '\n'.join([self.console_out_action_method_cpp(d) for d in action_name_list])
        ret = f"""#include "{self._console_controllee_class_name}.h"
#include <stdio.h>
{self._console_controllee_class_name}::{self._console_controllee_class_name}()
{{
    
}}
{self._console_controllee_class_name}::~{self._console_controllee_class_name}()
{{
    
}}
{action_list}
void {self._console_controllee_class_name}::NoTransition(const char* state, const char* transition)
{{
\tprintf("NoTransition(%s: %s)", state, transition);
}}

void {self._console_controllee_class_name}::OverTransition(const char* transition)
{{
\tprintf("OverTransition(%s)", transition);
}}
"""
        return ret

    def generate_console_out_controllee_h(self, transitions):
        action_transitions = [d for d in transitions if d.action is not None]
        action_name_list = sorted(list(set([d.action for d in action_transitions])))
        action_list = '\n'.join([self.console_out_action_method_h(d) for d in action_name_list])
        ret = f"""#pragma once

#include "{self._icontrollee_class_name}.h"


class {self._console_controllee_class_name} : public {self._icontrollee_class_name}
{{
public:
\t{self._console_controllee_class_name}();
\tvirtual ~{self._console_controllee_class_name}();
{action_list}
\tvirtual void NoTransition(const char* state, const char* transition);
\tvirtual void OverTransition(const char* transition);
}};
"""
        return ret

    def state_declaration(self, state):
        return f"""\t{self._base_state_class_name}* {self._prefix_instance_of}{state.name};"""

    def setup_state_declaration(self, state):
        return f"""\t{self._prefix_instance_of}{state.name} = new {self._prefix_state}{state.name}(this, _controllee);"""

    def delete_state_declaration(self, state):
        return f"""\tdelete {self._prefix_instance_of}{state.name};"""

    def state_include(self, state):
        return f"""#include "{self._prefix_state}{state.name}.h" """

    def transition_method_in_state_controller_cpp(self, event):
        return f"""void {self._state_controller_class_name}::{self._prefix_method}{event}()
{{
\tif(_currentState != 0)
\t{{
\t\t_currentState = _currentState->{self._prefix_method}{event}();
\t\tif(_currentState != 0)
\t\t{{
\t\t\t_currentState = _currentState->OutlineState();
\t\t}}
\t}} else {{
\t\t_controllee->OverTransition("{event}");
\t}}
}}
"""
    def transition_method_in_state_controller_h(self, event):
        return f"""\tvoid {self._prefix_method}{event}();
"""

    def generate_state_controller_cpp(self, state_dic, transitions, initial):
        states = [d for d in state_dic.values()]
        set_state_declarations = '\n'.join([self.setup_state_declaration(d) for d in sorted(states, key=lambda x: x.name)])
        delete_states = '\n'.join([self.delete_state_declaration(d) for d in sorted(states, key=lambda x: x.name)])

        event_transitions = sorted(list(set([d.event for d in transitions if d.event is not None])))
        transition_list = '\n'.join([self.transition_method_in_state_controller_cpp(d) for d in event_transitions])
        ret = f"""#include "{self._state_controller_class_name}.h"
{self._state_controller_class_name}::{self._state_controller_class_name}({self._icontrollee_class_name}* controllee)
{{
\t_controllee = controllee;
{set_state_declarations}
\t_currentState = {self._prefix_instance_of}{initial}; 
}}
{self._state_controller_class_name}::~{self._state_controller_class_name}()
{{
{delete_states}
}}
bool {self._state_controller_class_name}::TryTransitWithoutEvent()
{{
\tif(_currentState == 0)
\t{{
\t\treturn false; 
\t}}
\t{self._base_state_class_name}* current = _currentState; 
\t_currentState = _currentState->TryTransitWithoutEvent();
\tif(_currentState != 0)
\t{{
\t\t_currentState = _currentState->OutlineState();
\t}}
\treturn (current != _currentState);
}}
{transition_list}
const char* {self._state_controller_class_name}::GetCurrentStateName()
{{
\tif(_currentState == 0)
\t{{
\t\treturn "(end)";
\t}}
\telse
\t{{
\t\treturn _currentState->GetStateName(); 
\t}}
}}
"""
        return ret


    def generate_state_controller_h(self, state_dic, transitions, initial):
        states = [d for d in state_dic.values()]
        state_declarations = '\n'.join([self.state_declaration(d) for d in sorted(states, key=lambda x: x.name)])
        state_include =  '\n'.join([self.state_include(d) for d in sorted(states, key=lambda x: x.name)])

        event_transitions = sorted(list(set([d.event for d in transitions if d.event is not None])))
        transition_list = '\n'.join([self.transition_method_in_state_controller_h(d) for d in event_transitions])
        ret = f"""#pragma once

class {self._state_controller_class_name};

#include "{self._icontrollee_class_name}.h"
#include "{self._base_state_class_name}.h"
{state_include}

class {self._state_controller_class_name}
{{
private:
\t{self._icontrollee_class_name}* _controllee;
\t{self._base_state_class_name}* _currentState; 
public:
{state_declarations}
\t{self._state_controller_class_name}({self._icontrollee_class_name}* controllee);
\tvirtual ~{self._state_controller_class_name}();
\tbool TryTransitWithoutEvent();
{transition_list}
\tconst char* GetCurrentStateName();
}}; 
"""
        return ret
    
    def generate_transition_cpp(self, state, event, action, next_state, state_dic):
        if action is None:
            action_sequence = ""
        else:
            action_sequence = f"\t_controllee->{self._prefix_action_method}{action}();"
            
        if next_state == "[*]":
            setup_sequence = ""
            next_state_sequence = "\treturn 0;"
        else:
            setup_sequence = f'\t_stateController->{self._prefix_instance_of}{next_state}->Setup();'
            next_state_sequence = f"\treturn _stateController->{self._prefix_instance_of}{next_state};"
        transition_name = f'{self._prefix_method}{event}'
        if event is None:
            transition_name = 'TryTransitWithoutEvent'
        ret = f"""
{self._base_state_class_name}* {self._prefix_state}{state.name}::{transition_name}()
{{
{action_sequence}
{setup_sequence}
{next_state_sequence}
}}
"""
        return ret

    def generate_transition_h(self, event):
        transition_name = f'{self._prefix_method}{event}'
        if event is None:
            transition_name = 'TryTransitWithoutEvent'
        ret = f"""
\tvirtual {self._base_state_class_name}* {transition_name}();
"""
        return ret

    def generate_sub_transitions_cpp(self, state_name, event):
        return f"""
{self._base_state_class_name}* {self._prefix_state}{state_name}::{self._prefix_method}{event}()
{{
\t{self._base_state_class_name}* currentSubState = CurrentSubState();
\tif(currentSubState != 0)
\t{{
\t\t{self._base_state_class_name}* nextState = currentSubState->{self._prefix_method}{event}();
\t\treturn TransitBySubState(nextState);
\t}}
\treturn 0; 
}}
"""

    def generate_sub_transitions_h(self, event):
        return f"""
\tvirtual {self._base_state_class_name}* {self._prefix_method}{event}();
"""

    def generate_state_class_cpp(self, state, state_manager, transitions, state_dic):
        target_transitions = [d for d in transitions if d.state_from == state.name]
        transition_codes = '\n'.join([self.generate_transition_cpp(state, d.event, d.action, d.state_to, state_dic) for d in sorted(target_transitions, key=lambda x: x.get_event_as_key())])
        setup_code = ""
        sub_transition_codes = ""
        state_name = f"""
const char* {self._prefix_state}{state.name}::GetStateName()
{{
\treturn "{state.get_full_name()}"; 
}}
"""
        if state.initial_state:
            setup_code = f"""
void {self._prefix_state}{state.name}::Setup()
{{
\t\tSetupSubState(_stateController->InstanceOf{state.initial_state});
}}
"""
            sub_transitions = state_manager.get_all_transitions_under_the_state(state.name)
            sub_transition_codes = '\n'.join([self.generate_sub_transitions_cpp(state.name, d) for d in sorted(sub_transitions, key=lambda x: x)])
            state_name = f"""
const char* {self._prefix_state}{state.name}::GetStateName()
{{
\t{self._base_state_class_name}* currentSubState = CurrentSubState();
\tif(currentSubState == 0)
\t{{
\t\treturn "{state.get_full_name()}(end)";
\t}}
\treturn currentSubState->GetStateName(); 
}}
"""

        if state.parent:
            parent = f'_stateController->{self._prefix_instance_of}{state.parent.name}'
        else:
            parent = '0'
        
        ret = f"""#include "{self._prefix_state}{state.name}.h"

{self._prefix_state}{state.name}::{self._prefix_state}{state.name}({self._state_controller_class_name}* stateController, {self._icontrollee_class_name}* controllee) : {self._base_state_class_name}(controllee)
{{
\t_stateController = stateController;
\t_controllee = controllee;
}}
{self._prefix_state}{state.name}::~{self._prefix_state}{state.name}()
{{
    
}}
{setup_code}
{transition_codes}
{sub_transition_codes}
{state_name}
{self._base_state_class_name}* {self._prefix_state}{state.name}::GetParent()
{{
\treturn {parent};
}}
"""
        return ret

    def generate_state_class_h(self, state, state_manager, transitions, state_dic):
        target_transitions = [d for d in transitions if d.state_from == state.name]
        transition_codes = '\n'.join([self.generate_transition_h(d.event) for d in sorted(target_transitions, key=lambda x: x.get_event_as_key())])
        description_body = ''
        setup_code = ""
        sub_transition_codes = ""
        if state.initial_state:
            setup_code = f"""\tvirtual void Setup(); """
            sub_transitions = state_manager.get_all_transitions_under_the_state(state.name)
            sub_transition_codes = '\n'.join([self.generate_sub_transitions_h(d) for d in sorted(sub_transitions, key=lambda x: x)])
            

        if state.description is None or state.description.strip() == '':
            pass
        else:
            description_list = state.description.split('\n')
            description_body = '/// <summary>\n'
            for description in description_list:
                if description.strip() != '':
                    description_body += f'/// {description.strip()}\n'
            description_body += '/// </summary>\n'
        
        ret = f"""#pragma once

#include "{self._base_state_class_name}.h"
#include "{self._state_controller_class_name}.h"

{description_body}
class {self._prefix_state}{state.name} : public {self._base_state_class_name}
{{
private:
\t{self._state_controller_class_name}* _stateController; 
\t{self._icontrollee_class_name}* _controllee; 
public:
\t{self._prefix_state}{state.name}({self._state_controller_class_name}* stateController, {self._icontrollee_class_name}* controllee);
\tvirtual ~{self._prefix_state}{state.name}();
{setup_code}
{transition_codes}
{sub_transition_codes}
\tvirtual const char* GetStateName();
\tvirtual {self._base_state_class_name}* GetParent();
}};
        """
        return ret

    def generate_state_classes_cpp(self, state_manager, state_dic, transitions):
        return {d:self.generate_state_class_cpp(d, state_manager, transitions, state_dic) for d in state_dic.values()}

    def generate_state_classes_h(self, state_manager, state_dic, transitions):
        return {d:self.generate_state_class_h(d, state_manager, transitions, state_dic) for d in state_dic.values()}




    def _transition_method_in_base_state(self, event):
        return f"""\tpublic virtual {self._base_state_class_name}? {self._prefix_method}{event}()
\t{{
\t\t_controllee.NoTransition(GetStateName(), "{event}");
\t\treturn this;
\t}}
"""

    def _transition_menu(self, number, event):
        return f"""\t\tprintf("{number}. {event}\\n");"""

    def _transition_case(self, number, event):
        return f"""\t\t\tcase {number}:
\t\t\t\tstateController->{self._prefix_method}{event}();
\t\t\t\tbreak;
"""
    
    def generate_sample_boot_program(self, transitions):
        event_list = sorted(list(set([d.event for d in transitions if d.event is not None])))
        menu_list = '\n'.join([self._transition_menu(i + 1, event_list[i]) for i in range(len(event_list))])
        case_list = '\n'.join([self._transition_case(i + 1, event_list[i]) for i in range(len(event_list))])
        ret = f"""#include "{self._console_controllee_class_name}.h"
#include "{self._state_controller_class_name}.h"
#include <stdio.h>
int main(int argc, const char** argv)
{{


\tIControllee* controllee = new ConsoleOutControllee();
\tStateController* stateController = new StateController(controllee);

\tint number = 1; 
\twhile(number != 0)
\t{{
\t\tprintf("current state: %s\\n", stateController->GetCurrentStateName());
\t\tif(stateController->TryTransitWithoutEvent())
\t\t{{
\t\t\tcontinue; 
\t\t}}
{menu_list}
\t\tprintf("\\n");
\t\tprintf("0. exit\\n");
\t\tscanf_s("%d", &number);
\t\tswitch(number)
\t\t{{
\t\t\tcase 0:
\t\t\t\tbreak;
{case_list}
\t\t\tdefault:
\t\t\t\tprintf("Invalid number: %d\\n", number);
\t\t\t\tbreak;
\t\t}}
\t}}
\tdelete controllee; 
\tdelete stateController; 
}}
        """
        return ret
