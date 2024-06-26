class TypeScriptGenerator:
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
        self._boot_program = 'app.ts'
        self._icontrollee_class_name = icontrollee_class_name
        self._base_state_class_name = base_state_class_name
        self._state_controller_class_name = state_controller_class_name
        self._console_controllee_class_name = console_controllee_class_name

    def generate_files(self, state_manager):
        state_dic = state_manager.get_state_dic()
        transitions = state_manager.get_transitions()
        initial = state_manager.get_initial()

        ret = {}
        ret[f'{self._icontrollee_class_name}.ts'] = self.generate_controllee_interface(transitions)
        ret[f'{self._base_state_class_name}.ts'] = self.generate_base_state(transitions)
        ret[f'{self._state_controller_class_name}.ts'] = self.generate_state_controller(state_dic, transitions, initial)
        ret[f'{self._console_controllee_class_name}.ts'] = self.generate_console_out_controllee(transitions)
        ret[self._boot_program] = self.generate_sample_boot_program(transitions)
        state_classes = self.generate_state_classes(state_manager, state_dic, transitions)
        for state in state_classes:
            ret[f'{self._prefix_state}{state.name}.ts'] = state_classes[state]
        return ret
    
    def _transition_method_in_base_state(self, event):
        return f"""\tpublic {self._prefix_method}{event}(): {self._base_state_class_name} | null
\t{{
\t\tthis._controllee.NoTransition(this.GetStateName(), "{event}");
\t\treturn this;
\t}}
"""
    
    def generate_base_state(self, transitions):
        event_list = sorted(list(set([d.event for d in transitions if d.event is not None])))
        transition_list = '\n'.join([self._transition_method_in_base_state(d) for d in event_list])
        ret = f"""
import {{{self._icontrollee_class_name}}} from "./{self._icontrollee_class_name}"

export abstract class {self._base_state_class_name}
{{
\tprivate _controllee: {self._icontrollee_class_name}; 
\tprivate _currentSubState: {self._base_state_class_name} | null; 
\tpublic constructor(controllee: {self._icontrollee_class_name})
\t{{
\t\tthis._controllee = controllee;
\t\tthis._currentSubState = null; 
\t}}
\tpublic Setup(resume: boolean, deepResume: boolean): void
\t{{
\t\treturn;
\t}}
{transition_list}
\tpublic TryTransitWithoutEvent(): {self._base_state_class_name}
\t{{
\t\treturn this;
\t}}
\tpublic SetupSubState(child: {self._base_state_class_name}, resume: boolean): void
\t{{
\t\tif(!resume)
\t\t{{
\t\t\tthis._currentSubState = child; 
\t\t}}
\t\tif(this._currentSubState != null)
\t\t{{
\t\t\tthis._currentSubState.Setup(false, false);
\t\t}}
\t}}
\tpublic CurrentSubState(): {self._base_state_class_name} | null
\t{{
\t\treturn this._currentSubState;
\t}}
\tpublic TransitBySubState(nextState: {self._base_state_class_name} | null): {self._base_state_class_name} | null
\t{{
\t\tif(nextState == null || this._currentSubState == null)
\t\t{{
\t\t\treturn nextState;
\t\t}}
\t\tlet parentOfNextState: {self._base_state_class_name} | null = this._currentSubState.GetParent();
\t\tlet parentOfCurrentState: {self._base_state_class_name} | null = nextState.GetParent();
\t\tif(parentOfNextState != null && parentOfCurrentState != null && parentOfNextState == parentOfCurrentState)
\t\t{{
\t\t\tthis._currentSubState = nextState;
\t\t\treturn this;
\t\t}}
\t\treturn nextState;
\t}}
\tpublic TransitForChild(child: {self._base_state_class_name}): {self._base_state_class_name}
\t{{
\t\tthis._currentSubState = child;
\t\tlet parent: {self._base_state_class_name} | null = this.GetParent();
\t\tif(parent != null)
\t\t{{
\t\t\treturn parent.TransitForChild(this);
\t\t}}
\t\treturn this; 
\t}}
\tpublic OutlineState(): {self._base_state_class_name}
\t{{
\t\tlet parent: {self._base_state_class_name} | null = this.GetParent();
\t\tif(parent != null)
\t\t{{
\t\t\treturn parent.TransitForChild(this);
\t\t}}
\t\treturn this; 
\t}}
\tpublic ResumeSubState(subState: BaseState | null): void
\t{{
\t\tthis._currentSubState = subState; 
\t}}
\tpublic abstract GetStateName(): string;
\tpublic abstract GetParent(): {self._base_state_class_name} | null;
\tpublic abstract GetStateID(): number;
}}
        """
        return ret

    def action_method(self, action):
        return f'\t{self._prefix_action_method}{action}(): void'
        
    def generate_controllee_interface(self, transitions):
        action_transitions = [d for d in transitions if d.action is not None]
        action_name_list = sorted(list(set([d.action for d in action_transitions])))
        action_list = '\n'.join([self.action_method(d) for d in action_name_list])
        ret = f"""
export interface {self._icontrollee_class_name}
{{
{action_list}
\tNoTransition(state: string, transition: string): void
\tOverTransition(transition: string): void
}}
"""
        return ret

    def console_out_action_method(self, action):
        return f"""\tpublic {self._prefix_action_method}{action}(): void
\t{{
\t\tconsole.log("{action}");
\t}}
"""

    def generate_console_out_controllee(self, transitions):
        action_transitions = [d for d in transitions if d.action is not None]
        action_name_list = sorted(list(set([d.action for d in action_transitions])))
        action_list = '\n'.join([self.console_out_action_method(d) for d in action_name_list])
        ret = f"""
import {{{self._icontrollee_class_name}}} from "./{self._icontrollee_class_name}"
export class {self._console_controllee_class_name} implements {self._icontrollee_class_name}
{{
{action_list}
\tpublic NoTransition(state: string, transition: string): void
\t{{
\t\tconsole.log(`NoTransition(${{state}}: ${{transition}})`);
\t}}
\tpublic OverTransition(transition: string): void
\t{{
\t\tconsole.log(`OverTransition(${{transition}})`);
\t}}
}}
"""
        return ret

    def state_declaration(self, state):
        return f"""\treadonly {self._prefix_instance_of}{state.name}: {self._base_state_class_name};"""

    def setup_state_declaration(self, state):
        return f"""\t\tthis.{self._prefix_instance_of}{state.name} = new {self._prefix_state}{state.name}(this, this._controllee);"""

    def state_instance(self, state):
        return f"""\t\t\tthis.{self._prefix_instance_of}{state.name}"""

    def import_state_class(self, state):
        return f"""import {{{self._prefix_state}{state.name}}} from "./{self._prefix_state}{state.name}" """

    def transition_method_in_state_controller(self, event):
        return f"""\tpublic {self._prefix_method}{event}(): void
\t{{
\t\tif(this._currentState != null)
\t\t{{
\t\t\tthis._currentState = this._currentState.{self._prefix_method}{event}();
\t\t\tif(this._currentState != null)
\t\t\t{{
\t\t\t\tthis._currentState = this._currentState.OutlineState();
\t\t\t}}
\t\t}} else {{
\t\t\tthis._controllee.OverTransition("{event}");
\t\t}}
\t}}
"""

    def generate_state_controller(self, state_dic, transitions, initial):
        states = [d for d in state_dic.values()]
        state_declarations = '\n'.join([self.state_declaration(d) for d in sorted(states, key=lambda x: x.name)])
        set_state_declarations = '\n'.join([self.setup_state_declaration(d) for d in sorted(states, key=lambda x: x.name)])
        state_instance_list = ',\n'.join([self.state_instance(d) for d in sorted(states, key=lambda x: x.name)])
        event_transitions = sorted(list(set([d.event for d in transitions if d.event is not None])))
        transition_list = '\n'.join([self.transition_method_in_state_controller(d) for d in event_transitions])
        import_list = '\n'.join([self.import_state_class(d) for d in sorted(states, key=lambda x: x.name)])
        ret = f"""
import {{{self._icontrollee_class_name}}} from "./{self._icontrollee_class_name}"
import {{{self._base_state_class_name}}} from "./{self._base_state_class_name}"
{import_list}

export class {self._state_controller_class_name}
{{
\tprivate  _controllee: {self._icontrollee_class_name};
\tprivate _currentState: {self._base_state_class_name} | null; 
\tprivate _stateList: {self._base_state_class_name}[];
{state_declarations}
\treadonly MaxNumberOfStateIDs: number = {len(states)}; 
\tpublic constructor(controllee: {self._icontrollee_class_name})
\t{{
\t\tthis._controllee = controllee;
{set_state_declarations}
\t\tthis._currentState = this.{self._prefix_instance_of}{initial}; 
\t\tthis._stateList = [
{state_instance_list}
\t\t]; 
\t}}

\tpublic GetCurrentIdFromStateId(parentStateId: number): number
\t{{
\t\tif(parentStateId == -1)
\t\t{{
\t\t\treturn this.GetCurrentIdFromState(this._currentState);
\t\t}}
\t\tif(parentStateId < -1 || parentStateId >= this.MaxNumberOfStateIDs)
\t\t{{
\t\t\treturn -1;
\t\t}}
\t\treturn this.GetCurrentIdFromState(this._stateList[parentStateId].CurrentSubState());
\t}}
\tprivate GetCurrentIdFromState(state: {self._base_state_class_name} | null): number
\t{{
\t\tif(state == null)
\t\t{{
\t\t\treturn -1;
\t\t}}
\treturn state.GetStateID();
\t}}
\tpublic ResumeState(parentStateId: number, stateId: number): void
\t{{
\t\tlet state: {self._base_state_class_name} | null = null; 
\t\tif(stateId >= 0 && stateId < this.MaxNumberOfStateIDs)
\t\t{{
\t\t\tstate = this._stateList[stateId]; 
\t\t}}
\t\tif(parentStateId == -1)
\t\t{{
\t\t\tthis._currentState = state;
\t\t\treturn;
\t\t}}
\t\tif(parentStateId < -1 || parentStateId >= this.MaxNumberOfStateIDs)
\t\t{{
\t\t\treturn;
\t\t}}
\t\tthis._stateList[parentStateId].ResumeSubState(state);
\t}}
\tpublic StateName(parentStateId: number): string
\t{{
\t\tif(parentStateId >= 0 && parentStateId < this.MaxNumberOfStateIDs)
\t\t{{
\t\t\treturn this._stateList[parentStateId].GetStateName();
\t\t}}
\t\treturn "(None)";
\t}}

\tpublic TryTransitWithoutEvent(): boolean
\t{{
\t\tif(this._currentState == null)
\t\t{{
\t\t\treturn false; 
\t\t}}
\t\tlet current: {self._base_state_class_name} | null = this._currentState; 
\t\tthis._currentState = this._currentState.TryTransitWithoutEvent();
\t\tif(this._currentState != null)
\t\t{{
\t\t\tthis._currentState = this._currentState.OutlineState();
\t\t}}
\t\treturn (current != this._currentState);
\t}}
{transition_list}
\tpublic GetCurrentStateName(): string
\t{{
\t\tif(this._currentState == null)
\t\t{{
\t\t\treturn "(end)";
\t\t}}
\t\telse
\t\t{{
\t\t\treturn this._currentState.GetStateName(); 
\t\t}}
\t}}
}}
"""
        return ret
    
    def generate_transition(self, event, action, next_state, history, state_dic):
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
            action_sequence = f"\t\tthis._controlleeImp.{self._prefix_action_method}{action}();"
            
        if next_state == "[*]":
            setup_sequence = ""
            next_state_sequence = "\t\treturn null;"
        else:
            setup_sequence = f'\t\tthis._stateController.{self._prefix_instance_of}{next_state}.Setup({resume}, {deepResume});'
            next_state_sequence = f"\t\treturn this._stateController.{self._prefix_instance_of}{next_state};"
        transition_name = f'{self._prefix_method}{event}'
        if event is None:
            transition_name = 'TryTransitWithoutEvent'
        ret = f"""
\tpublic {transition_name}(): {self._base_state_class_name} | null
\t{{
{action_sequence}
{setup_sequence}
{next_state_sequence}
\t}}
"""
        return ret

    def generate_sub_transitions(self, event):
        return f"""
\tpublic {self._prefix_method}{event}(): {self._base_state_class_name} | null
\t{{
\t\tlet currentSubState: BaseState | null = this.CurrentSubState();
\t\tif(currentSubState != null)
\t\t{{
\t\t\tlet nextState: {self._base_state_class_name} | null = currentSubState.{self._prefix_method}{event}();
\t\t\treturn this.TransitBySubState(nextState);
\t\t}}
\t\treturn null; 
\t}}
"""

    def generate_state_class(self, state, index, state_manager, transitions, state_dic):
        target_transitions = [d for d in transitions if d.state_from == state.name]
        transition_codes = '\n'.join([self.generate_transition(d.event, d.action, d.state_to, d.history, state_dic) for d in sorted(target_transitions, key=lambda x: x.get_event_as_key())])
        description_body = ''
        if state.description is None or state.description.strip() == '':
            pass
        else:
            description_list = state.description.split('\n')
            description_body = '/// <summary>\n'
            for description in description_list:
                if description.strip() != '':
                    description_body += f'/// {description.strip()}\n'
            description_body += '/// </summary>\n'
        setup_code = ""
        sub_transition_codes = ""
        state_name = f"""
\tpublic  GetStateName(): string
\t{{
\t\treturn "{state.get_full_name()}"; 
\t}}
"""
        if state.initial_state:
            setup_code = f"""
\tpublic Setup(resume: boolean, deepResume: boolean): void
\t{{
\t\tif(!deepResume)
\t\t{{
\t\t\tthis.SetupSubState(this._stateController.{self._prefix_instance_of}{state.initial_state}, resume);
\t\t}}
\t}}
"""
            sub_transitions = state_manager.get_all_transitions_under_the_state(state.name)
            sub_transition_codes = '\n'.join([self.generate_sub_transitions(d) for d in sorted(sub_transitions, key=lambda x: x)])
            state_name = f"""
\tpublic GetStateName(): string
\t{{
\t\tlet currentSubState: {self._base_state_class_name} | null = this.CurrentSubState();
\t\tif(currentSubState == null)
\t\t{{
\t\t\treturn "{state.get_full_name()}(end)";
\t\t}}
\t\treturn currentSubState.GetStateName(); 
\t}}
"""

        if state.parent:
            parent = f'this._stateController.{self._prefix_instance_of}{state.parent.name}'
        else:
            parent = 'null'
        
        
        ret = f"""
import {{{self._base_state_class_name}}} from "./{self._base_state_class_name}"
import {{{self._icontrollee_class_name}}} from "./{self._icontrollee_class_name}"
import {{{self._state_controller_class_name}}} from "./{self._state_controller_class_name}"

{description_body}
export class {self._prefix_state}{state.name} extends {self._base_state_class_name}
{{
\tprivate _stateController: {self._state_controller_class_name}; 
\tprivate _controlleeImp: {self._icontrollee_class_name}; 
\tpublic constructor(stateController: {self._state_controller_class_name}, controllee: {self._icontrollee_class_name})
\t{{
\t\tsuper(controllee);
\t\tthis._stateController = stateController;
\t\tthis._controlleeImp = controllee;
\t}}
{setup_code}
{transition_codes}
{sub_transition_codes}
{state_name}
\tpublic GetParent(): BaseState | null
\t{{
\t\treturn {parent}; 
\t}}
\tpublic GetStateID(): number
\t{{
\t\treturn {index}; 
\t}}
}}
        """
        return ret

    def generate_state_classes(self, state_manager, state_dic, transitions):
        states = [(i,k) for i,k in enumerate(sorted(state_dic.keys()))]
        return {state_dic[k]:self.generate_state_class(state_dic[k], index, state_manager, transitions, state_dic) for index, k in states}

    def _transition_menu(self, number, event):
        return f"""\t\tconsole.log("{number}. {event}");"""

    def _transition_case(self, number, event):
        return f"""\t\t\t\tcase {number}:
\t\t\t\t\tthis._stateController.{self._prefix_method}{event}();
\t\t\t\t\tthis.Step();;
\t\t\t\t\tbreak;
"""
    
    def generate_sample_boot_program(self, transitions):
        event_list = sorted(list(set([d.event for d in transitions if d.event is not None])))
        menu_list = '\n'.join([self._transition_menu(i + 1, event_list[i]) for i in range(len(event_list))])
        case_list = '\n'.join([self._transition_case(i + 1, event_list[i]) for i in range(len(event_list))])
        ret = f"""
import * as readline from "readline";
import {{{self._console_controllee_class_name}}} from "./{self._console_controllee_class_name}"
import {{{self._state_controller_class_name}}} from "./{self._state_controller_class_name}"


class TestApp
{{
\tprivate _stateController: {self._state_controller_class_name} = new {self._state_controller_class_name}( new ConsoleOutControllee());

\tpublic Run(): void
\t{{
\t\tthis.Step();
\t}}

\tprivate Step(): void
\t{{
\t\tconsole.log(`current state: ${{this._stateController.GetCurrentStateName()}}`);
\t\tif(this._stateController.TryTransitWithoutEvent())
\t\t{{
\t\t\tthis.Step();
\t\t}}
{menu_list}
\t\tconsole.log("");
\t\tconsole.log("0. exit");
\t\tconsole.log("-1. ShowStateIDs then resume");
\t\tconst rl = readline.createInterface({{
\t\t\tinput: process.stdin,
\t\t\toutput: process.stdout
\t\t}});
\t\tlet idStr: string | null = null;
\t\trl.question('order: ', (answer) => {{
\t\t\trl.close();
\t\t\tthis.Transit(Number(answer));
\t\t}});
\t}}

\tprivate Transit(id: number): void
\t{{
\t\tif(id)
\t\t{{
\t\t\tswitch(id)
\t\t\t{{
\t\t\t\tcase 0:
\t\t\t\t\tbreak;
{case_list}

\t\t\t\tcase -1:
\t\t\t\t{{
\t\t\t\t\tlet stateId: number = this._stateController.GetCurrentIdFromStateId(-1);
\t\t\t\t\tconsole.log(`Top State ID: ${{stateId}} - ${{this._stateController.StateName(stateId)}}`);
\t\t\t\t\tlet subStateIds: number[] = new Array(this._stateController.MaxNumberOfStateIDs);
\t\t\t\t\tfor(let i: number = 0;i<this._stateController.MaxNumberOfStateIDs;i++)
\t\t\t\t\t{{
\t\t\t\t\t\tsubStateIds[i] = this._stateController.GetCurrentIdFromStateId(i);
\t\t\t\t\t\tconsole.log(`Sub State ID: ${{subStateIds[i]}} - ${{this._stateController.StateName(subStateIds[i])}}`);
\t\t\t\t\t}}

\t\t\t\t\tthis._stateController = new {self._state_controller_class_name}( new ConsoleOutControllee());
\t\t\t\t\tconsole.log(`StateController has been reset.`);

\t\t\t\t\tthis._stateController.ResumeState(-1, stateId); 
\t\t\t\t\tfor(let i: number = 0;i<this._stateController.MaxNumberOfStateIDs;i++)
\t\t\t\t\t{{
\t\t\t\t\t\tthis._stateController.ResumeState(i, subStateIds[i]);
\t\t\t\t\t}}

\t\t\t\t\tstateId = this._stateController.GetCurrentIdFromStateId(-1);
\t\t\t\t\tconsole.log(`Top State ID: ${{stateId}} - ${{this._stateController.StateName(stateId)}}`);
\t\t\t\t\tfor(let i: number = 0;i<this._stateController.MaxNumberOfStateIDs;i++)
\t\t\t\t\t{{
\t\t\t\t\t\tsubStateIds[i] = this._stateController.GetCurrentIdFromStateId(i);
\t\t\t\t\t\tconsole.log(`Sub State ID: ${{subStateIds[i]}} - ${{this._stateController.StateName(subStateIds[i])}}`);
\t\t\t\t\t}}
\t\t\t\t}}

\t\t\t\tdefault:
\t\t\t\t\tconsole.log(`Invalid number: ${{id}}`);
\t\t\t\t\tthis.Step();
\t\t\t\t\tbreak;
\t\t\t}}
\t\t}}
\t}}

}}

let app: TestApp = new TestApp();
app.Run();
"""
        return ret
