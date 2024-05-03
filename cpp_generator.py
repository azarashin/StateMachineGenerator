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
\t_currentSubState = nullptr;
}}
{self._base_state_class_name}::~{self._base_state_class_name}()
{{

}}
void {self._base_state_class_name}::Setup(bool resume, bool deepResume)
{{
}} 
{transition_list}
{self._base_state_class_name}* {self._base_state_class_name}::TryTransitWithoutEvent()
{{
\treturn this;
}}
void {self._base_state_class_name}::SetupSubState({self._base_state_class_name}* child, bool resume)
{{
\tif(!resume)
\t{{
\t\t_currentSubState = child; 
\t}}
\tif(_currentSubState != nullptr)
\t{{
\t\t_currentSubState->Setup(false, false);
\t}}
}}
{self._base_state_class_name}* {self._base_state_class_name}::CurrentSubState()
{{
\treturn _currentSubState;
}}
{self._base_state_class_name}* {self._base_state_class_name}::TransitBySubState({self._base_state_class_name}* nextState)
{{
\tif(nextState == nullptr || _currentSubState == nullptr)
\t{{
\t\treturn nextState;
\t}}
\t{self._base_state_class_name}* parentOfNextState = _currentSubState->GetParent();
\t{self._base_state_class_name}* parentOfCurrentState = nextState->GetParent();
\tif(parentOfNextState != nullptr && parentOfCurrentState != nullptr && parentOfNextState == parentOfCurrentState)
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
\tif(parent != nullptr)
\t{{
\t\treturn parent->TransitForChild(this);
\t}}
\treturn this; 
}}
{self._base_state_class_name}* {self._base_state_class_name}::OutlineState()
{{
\t{self._base_state_class_name}* parent = GetParent();
\tif(parent != nullptr)
\t{{
\t\treturn parent->TransitForChild(this);
\t}}
\treturn this; 
}}
void {self._base_state_class_name}::ResumeSubState({self._base_state_class_name}* subState)
{{
\t_currentSubState = subState; 
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
\tvirtual void Setup(bool resume, bool deepResume); 
{transition_list}
\tvirtual {self._base_state_class_name}* TryTransitWithoutEvent();
\tvoid SetupSubState({self._base_state_class_name}* child, bool resume);
\t{self._base_state_class_name}* CurrentSubState();
\t{self._base_state_class_name}* TransitBySubState({self._base_state_class_name}* nextState);
\t{self._base_state_class_name}* TransitForChild({self._base_state_class_name}* child);
\t{self._base_state_class_name}* OutlineState();
\tvoid ResumeSubState(BaseState* subState);
\tvirtual const char* GetStateName() = 0;
\tvirtual {self._base_state_class_name}* GetParent() = 0;
\tvirtual int GetStateID() = 0;
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
\tprintf("{action}\\n");
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
\tprintf("NoTransition(%s: %s)\\n", state, transition);
}}

void {self._console_controllee_class_name}::OverTransition(const char* transition)
{{
\tprintf("OverTransition(%s)\\n", transition);
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

    def state_instance(self, state):
        return f"""\t\t{self._prefix_instance_of}{state.name}"""

    def delete_state_declaration(self, state):
        return f"""\tdelete {self._prefix_instance_of}{state.name};"""

    def state_include(self, state):
        return f"""#include "{self._prefix_state}{state.name}.h" """

    def transition_method_in_state_controller_cpp(self, event):
        return f"""void {self._state_controller_class_name}::{self._prefix_method}{event}()
{{
\tif(_currentState != nullptr)
\t{{
\t\t_currentState = _currentState->{self._prefix_method}{event}();
\t\tif(_currentState != nullptr)
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
        state_instance_list = ',\n'.join([self.state_instance(d) for d in sorted(states, key=lambda x: x.name)])
        delete_states = '\n'.join([self.delete_state_declaration(d) for d in sorted(states, key=lambda x: x.name)])

        event_transitions = sorted(list(set([d.event for d in transitions if d.event is not None])))
        transition_list = '\n'.join([self.transition_method_in_state_controller_cpp(d) for d in event_transitions])
        ret = f"""#include "{self._state_controller_class_name}.h"
#include <string.h>
{self._state_controller_class_name}::{self._state_controller_class_name}({self._icontrollee_class_name}* controllee)
{{
\t_controllee = controllee;
{set_state_declarations}
\t_currentState = {self._prefix_instance_of}{initial}; 
\t{self._base_state_class_name}* stateList[] = {{
{state_instance_list}
\t}}; 
\tmemcpy(_stateList, stateList, sizeof(BaseState*) * MaxNumberOfStateIDs); 
}}
{self._state_controller_class_name}::~{self._state_controller_class_name}()
{{
{delete_states}
}}


int {self._state_controller_class_name}::GetCurrentIdFromStateId(int parentStateId)
{{
\tif(parentStateId == -1)
\t{{
\t\treturn GetCurrentIdFromState(_currentState);
\t}}
\tif(parentStateId < -1 || parentStateId >= MaxNumberOfStateIDs)
\t{{
\t\treturn -1;
\t}}
\treturn GetCurrentIdFromState(_stateList[parentStateId]->CurrentSubState());
}}
int {self._state_controller_class_name}::GetCurrentIdFromState({self._base_state_class_name}* state)
{{
\tif(state == nullptr)
\t{{
\t\treturn -1;
\t}}
\treturn state->GetStateID();
\t}}
void {self._state_controller_class_name}::ResumeState(int parentStateId, int stateId)
{{
\t{self._base_state_class_name}* state = nullptr; 
\tif(stateId >= 0 && stateId < MaxNumberOfStateIDs)
\t{{
\t\tstate = _stateList[stateId]; 
\t}}
\tif(parentStateId == -1)
\t{{
\t\t_currentState = state;
\t\treturn;
\t}}
\tif(parentStateId < -1 || parentStateId >= MaxNumberOfStateIDs)
\t{{
\t\treturn;
\t}}
\t_stateList[parentStateId]->ResumeSubState(state);
}}
const char* {self._state_controller_class_name}::StateName(int parentStateId)
{{
\tif(parentStateId >= 0 && parentStateId < MaxNumberOfStateIDs)
\t{{
\t\treturn _stateList[parentStateId]->GetStateName();
\t}}
\treturn "(None)";
}}

bool {self._state_controller_class_name}::TryTransitWithoutEvent()
{{
\tif(_currentState == nullptr)
\t{{
\t\treturn false; 
\t}}
\t{self._base_state_class_name}* current = _currentState; 
\t_currentState = _currentState->TryTransitWithoutEvent();
\tif(_currentState != nullptr)
\t{{
\t\t_currentState = _currentState->OutlineState();
\t}}
\treturn (current != _currentState);
}}
{transition_list}
const char* {self._state_controller_class_name}::GetCurrentStateName()
{{
\tif(_currentState == nullptr)
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
public:
\tstatic const int MaxNumberOfStateIDs = {len(states)};
private:
\t{self._icontrollee_class_name}* _controllee;
\t{self._base_state_class_name}* _currentState; 
\t{self._base_state_class_name}* _stateList[MaxNumberOfStateIDs];
\tint GetCurrentIdFromState({self._base_state_class_name}* state);
public:
{state_declarations}
\t{self._state_controller_class_name}({self._icontrollee_class_name}* controllee);
\tvirtual ~{self._state_controller_class_name}();

\tint GetCurrentIdFromStateId(int parentStateId);
\tvoid ResumeState(int parentStateId, int stateId);
\tconst char* StateName(int parentStateId);

\tbool TryTransitWithoutEvent();
{transition_list}
\tconst char* GetCurrentStateName();
}}; 
"""
        return ret
    
    def generate_transition_cpp(self, state, event, action, next_state, history, state_dic):
        if history == '[H]':
            resume = 'true'
            deepResume = 'false'
        elif history == '[H*]':
            resume = 'true'
            deepResume = 'true'
        else:
            resume = 'false'
            deepResume = 'false'
        if action is None:
            action_sequence = ""
        else:
            action_sequence = f"\t_controllee->{self._prefix_action_method}{action}();"
            
        if next_state == "[*]":
            setup_sequence = ""
            next_state_sequence = "\treturn nullptr;"
        else:
            setup_sequence = f'\t_stateController->{self._prefix_instance_of}{next_state}->Setup({resume}, {deepResume});'
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
\tif(currentSubState != nullptr)
\t{{
\t\t{self._base_state_class_name}* nextState = currentSubState->{self._prefix_method}{event}();
\t\treturn TransitBySubState(nextState);
\t}}
\treturn nullptr; 
}}
"""

    def generate_sub_transitions_h(self, event):
        return f"""
\tvirtual {self._base_state_class_name}* {self._prefix_method}{event}();
"""

    def generate_state_class_cpp(self, state, index, state_manager, transitions, state_dic):
        target_transitions = [d for d in transitions if d.state_from == state.name]
        transition_codes = '\n'.join([self.generate_transition_cpp(state, d.event, d.action, d.state_to, d.history, state_dic) for d in sorted(target_transitions, key=lambda x: x.get_event_as_key())])
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
void {self._prefix_state}{state.name}::Setup(bool resume, bool deepResume)
{{
\tif(!deepResume)
\t{{
\t\tSetupSubState(_stateController->{self._prefix_instance_of}{state.initial_state}, resume);
\t}}
}}
"""
            sub_transitions = state_manager.get_all_transitions_under_the_state(state.name)
            sub_transition_codes = '\n'.join([self.generate_sub_transitions_cpp(state.name, d) for d in sorted(sub_transitions, key=lambda x: x)])
            state_name = f"""
const char* {self._prefix_state}{state.name}::GetStateName()
{{
\t{self._base_state_class_name}* currentSubState = CurrentSubState();
\tif(currentSubState == nullptr)
\t{{
\t\treturn "{state.get_full_name()}(end)";
\t}}
\treturn currentSubState->GetStateName(); 
}}
"""

        if state.parent:
            parent = f'_stateController->{self._prefix_instance_of}{state.parent.name}'
        else:
            parent = 'nullptr'
        
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
int {self._prefix_state}{state.name}::GetStateID()
{{
\treturn {index};
}}
"""
        return ret

    def generate_state_class_h(self, state, index, state_manager, transitions, state_dic):
        target_transitions = [d for d in transitions if d.state_from == state.name]
        transition_codes = '\n'.join([self.generate_transition_h(d.event) for d in sorted(target_transitions, key=lambda x: x.get_event_as_key())])
        description_body = ''
        setup_code = ""
        sub_transition_codes = ""
        if state.initial_state:
            setup_code = f"""\tvirtual void Setup(bool resume, bool deepResume); """
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
\tvirtual int GetStateID();
}};
        """
        return ret

    def generate_state_classes_cpp(self, state_manager, state_dic, transitions):
        states = [(i,k) for i,k in enumerate(sorted(state_dic.keys()))]
        return {state_dic[k]:self.generate_state_class_cpp(state_dic[k], index, state_manager, transitions, state_dic) for index, k in states}

    def generate_state_classes_h(self, state_manager, state_dic, transitions):
        states = [(i,k) for i,k in enumerate(sorted(state_dic.keys()))]
        return {state_dic[k]:self.generate_state_class_h(state_dic[k], index, state_manager, transitions, state_dic) for index, k in states}

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


\t{self._icontrollee_class_name}* controllee = new ConsoleOutControllee();
\t{self._state_controller_class_name}* stateController = new {self._state_controller_class_name}(controllee);

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
\t\tprintf("-1. ShowStateIDs then resume\\n");
\t\tscanf_s("%d", &number);
\t\tswitch(number)
\t\t{{
\t\t\tcase 0:
\t\t\t\tbreak;
{case_list}

\t\t\tcase -1:
\t\t\t{{
\t\t\t\tint stateId = stateController->GetCurrentIdFromStateId(-1);
\t\t\t\tprintf("Top State ID: %d - %s\\n", stateId, stateController->StateName(stateId));
\t\t\t\tint* subStateIds = new int[stateController->MaxNumberOfStateIDs];
\t\t\t\tfor(int i=0;i<stateController->MaxNumberOfStateIDs;i++)
\t\t\t\t{{
\t\t\t\t\tsubStateIds[i] = stateController->GetCurrentIdFromStateId(i);
\t\t\t\t\tprintf("Sub State ID: %d - %s\\n", subStateIds[i], stateController->StateName(subStateIds[i]));
\t\t\t\t}}

\t\t\t\tdelete stateController; 
\t\t\t\tstateController = new StateController(controllee);
\t\t\t\tprintf("StateController has been reset.\\n");

\t\t\t\tstateController->ResumeState(-1, stateId); 
\t\t\t\tfor(int i=0;i<stateController->MaxNumberOfStateIDs;i++)
\t\t\t\t{{
\t\t\t\t\tstateController->ResumeState(i, subStateIds[i]);
\t\t\t\t}}

\t\t\t\tstateId = stateController->GetCurrentIdFromStateId(-1);
\t\t\t\tprintf("Top State ID: %d - %s\\n", stateId, stateController->StateName(stateId));
\t\t\t\tfor(int i=0;i<stateController->MaxNumberOfStateIDs;i++)
\t\t\t\t{{
\t\t\t\t\tsubStateIds[i] = stateController->GetCurrentIdFromStateId(i);
\t\t\t\t\tprintf("Sub State ID: %d - %s\\n", subStateIds[i], stateController->StateName(subStateIds[i]));
\t\t\t\t}}
\t\t\t\tdelete[] subStateIds; 
\t\t\t}}
\t\t\tbreak;
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
