class CSGenerator:
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
        self._boot_program = 'Program.cs'
        self._icontrollee_class_name = icontrollee_class_name
        self._base_state_class_name = base_state_class_name
        self._state_controller_class_name = state_controller_class_name
        self._console_controllee_class_name = console_controllee_class_name

    def generate_files(self, state_manager):
        state_dic = state_manager.get_state_dic()
        transitions = state_manager.get_transitions()
        initial = state_manager.get_initial()

        ret = {}
        ret[f'{self._icontrollee_class_name}.cs'] = self.generate_controllee_interface(transitions)
        ret[f'{self._base_state_class_name}.cs'] = self.generate_base_state(transitions)
        ret[f'{self._state_controller_class_name}.cs'] = self.generate_state_controller(state_dic, transitions, initial)
        ret[f'{self._console_controllee_class_name}.cs'] = self.generate_console_out_controllee(transitions)
        ret[self._boot_program] = self.generate_sample_boot_program(transitions)
        state_classes = self.generate_state_classes(state_manager, state_dic, transitions)
        for state in state_classes:
            ret[f'{self._prefix_state}{state.name}.cs'] = state_classes[state]
        return ret
    
    def _transition_method_in_base_state(self, event):
        return f"""\tpublic virtual {self._base_state_class_name}? {self._prefix_method}{event}()
\t{{
\t\t_controllee.NoTransition(GetStateName(), "{event}");
\t\treturn this;
\t}}
"""
    
    def generate_base_state(self, transitions):
        event_list = sorted(list(set([d.event for d in transitions if d.event is not None])))
        transition_list = '\n'.join([self._transition_method_in_base_state(d) for d in event_list])
        ret = f"""
abstract public class {self._base_state_class_name}
{{
\tprivate {self._icontrollee_class_name} _controllee; 
\tpublic {self._base_state_class_name}({self._icontrollee_class_name} controllee)
\t{{
\t\t_controllee = controllee;
\t}}
\tpublic virtual void Setup()
\t{{
\t\treturn;
\t}}
{transition_list}
\tpublic virtual {self._base_state_class_name}? TryTransitWithoutEvent()
\t{{
\t\treturn this;
\t}}
\tpublic abstract string GetStateName();
}}
        """
        return ret

    def action_method(self, action):
        return f'\tvoid {self._prefix_action_method}{action}();'
        
    def generate_controllee_interface(self, transitions):
        action_transitions = [d for d in transitions if d.action is not None]
        action_name_list = sorted(list(set([d.action for d in action_transitions])))
        action_list = '\n'.join([self.action_method(d) for d in action_name_list])
        ret = f"""
public interface {self._icontrollee_class_name}
{{
{action_list}
\tvoid NoTransition(string state, string transition);
\tvoid OverTransition(string transition);
}}
"""
        return ret

    def console_out_action_method(self, action):
        return f"""\tpublic void {self._prefix_action_method}{action}()
\t{{
\t\tConsole.WriteLine("{action}");
\t}}
"""

    def generate_console_out_controllee(self, transitions):
        action_transitions = [d for d in transitions if d.action is not None]
        action_name_list = sorted(list(set([d.action for d in action_transitions])))
        action_list = '\n'.join([self.console_out_action_method(d) for d in action_name_list])
        ret = f"""
public class {self._console_controllee_class_name} : {self._icontrollee_class_name}
{{
{action_list}
\tpublic void NoTransition(string state, string transition)
\t{{
\t\tConsole.WriteLine($"NoTransition({{state}}: {{transition}})");
\t}}

\tpublic void OverTransition(string transition)
\t{{
\t\tConsole.WriteLine($"OverTransition({{transition}})");
\t}}
}}
"""
        return ret

    def state_declaration(self, state):
        return f"""\tpublic {self._base_state_class_name} {self._prefix_instance_of}{state.name} {{get; private set;}}"""

    def setup_state_declaration(self, state):
        return f"""\t\t{self._prefix_instance_of}{state.name} = new {self._prefix_state}{state.name}(this, _controllee);"""

    def transition_method_in_state_controller(self, event):
        return f"""\tpublic void {self._prefix_method}{event}()
\t{{
\t\tif(_currentState != null)
\t\t{{
\t\t\t_currentState = _currentState.{self._prefix_method}{event}();
\t\t}} else {{
\t\t\t_controllee.OverTransition("{event}");
\t\t}}
\t}}
"""

    def generate_state_controller(self, state_dic, transitions, initial):
        states = [d for d in state_dic.values()]
        state_declarations = '\n'.join([self.state_declaration(d) for d in sorted(states, key=lambda x: x.name)])
        set_state_declarations = '\n'.join([self.setup_state_declaration(d) for d in sorted(states, key=lambda x: x.name)])
        event_transitions = sorted(list(set([d.event for d in transitions if d.event is not None])))
        transition_list = '\n'.join([self.transition_method_in_state_controller(d) for d in event_transitions])
        ret = f"""
public class {self._state_controller_class_name}
{{
\tprivate {self._icontrollee_class_name} _controllee;
\tprivate {self._base_state_class_name}? _currentState; 
{state_declarations}
\tpublic {self._state_controller_class_name}({self._icontrollee_class_name} controllee)
\t{{
\t\t_controllee = controllee;
{set_state_declarations}
\t\t_currentState = {self._prefix_instance_of}{initial}; 
\t}}
\tpublic bool TryTransitWithoutEvent()
\t{{
\t\tif(_currentState == null)
\t\t{{
\t\t\treturn false; 
\t\t}}
\t\t{self._base_state_class_name}? current = _currentState; 
\t\t_currentState = _currentState.TryTransitWithoutEvent();
\t\treturn (current != _currentState);
\t}}
{transition_list}
\tpublic string GetCurrentStateName()
\t{{
\t\tif(_currentState == null)
\t\t{{
\t\t\treturn "(end)";
\t\t}}
\t\telse
\t\t{{
\t\t\treturn _currentState.GetStateName(); 
\t\t}}
\t}}
}}
"""
        return ret
    
    def generate_transition(self, event, action, next_state, state_dic):
        if action is None:
            action_sequence = ""
        else:
            action_sequence = f"\t\t_controllee.{self._prefix_action_method}{action}();"
            
        if next_state == "[*]":
            setup_sequence = ""
            next_state_sequence = "\t\treturn null;"
        else:
            setup_sequence = f'\t\t_stateController.{self._prefix_instance_of}{next_state}.Setup();'
            next_state_sequence = f"\t\treturn _stateController.{self._prefix_instance_of}{next_state};"
        transition_name = f'{self._prefix_method}{event}'
        if event is None:
            transition_name = 'TryTransitWithoutEvent'
        ret = f"""
\tpublic override {self._base_state_class_name}? {transition_name}()
\t{{
{action_sequence}
{setup_sequence}
{next_state_sequence}
\t}}
"""
        return ret

    def generate_sub_transitions(self, event):
        return f"""
\tpublic override {self._base_state_class_name}? {self._prefix_method}{event}()
\t{{
\t\tif(_currentState != null)
\t\t{{
\t\t\t_currentState = _currentState.{self._prefix_method}{event}();
\t\t\treturn this; 
\t\t}}
\t\treturn null; 
\t}}
"""

    def generate_state_class(self, state, state_manager, transitions, state_dic):
        target_transitions = [d for d in transitions if d.state_from == state.name]
        transition_codes = '\n'.join([self.generate_transition(d.event, d.action, d.state_to, state_dic) for d in sorted(target_transitions, key=lambda x: x.get_event_as_key())])
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
        setup_description = ""
        sub_transition_codes = ""
        if state.initial_state:
            setup_code = f"""
\tpublic override void Setup()
\t{{
\t\t_currentState = _stateController.InstanceOf{state.initial_state}; 
\t\treturn;
\t}}
"""
            setup_description = f"""\tprivate {self._base_state_class_name}? _currentState; """
            sub_transitions = state_manager.get_all_transitions_under_the_state(state.name)
            sub_transition_codes = '\n'.join([self.generate_sub_transitions(d) for d in sorted(sub_transitions, key=lambda x: x)])

        
        ret = f"""
{description_body}
public class {self._prefix_state}{state.name} : {self._base_state_class_name}
{{
\tprivate {self._state_controller_class_name} _stateController; 
\tprivate {self._icontrollee_class_name} _controllee; 
{setup_description}
\tpublic {self._prefix_state}{state.name}({self._state_controller_class_name} stateController, {self._icontrollee_class_name} controllee) : base(controllee)
\t{{
\t\t_stateController = stateController;
\t\t_controllee = controllee;
\t}}
{setup_code}
{transition_codes}
{sub_transition_codes}
\tpublic override string GetStateName()
\t{{
\t\treturn "{state.get_full_name()}"; 
\t}}
}}
        """
        return ret

    def generate_state_classes(self, state_manager, state_dic, transitions):
        return {d:self.generate_state_class(d, state_manager, transitions, state_dic) for d in state_dic.values()}





    def _transition_method_in_base_state(self, event):
        return f"""\tpublic virtual {self._base_state_class_name}? {self._prefix_method}{event}()
\t{{
\t\t_controllee.NoTransition(GetStateName(), "{event}");
\t\treturn this;
\t}}
"""

    def _transition_menu(self, number, event):
        return f"""\tConsole.WriteLine("{number}. {event}");"""

    def _transition_case(self, number, event):
        return f"""\t\t\tcase {number}:
\t\t\t\tstateController.{self._prefix_method}{event}();
\t\t\t\tbreak;
"""
    
    def generate_sample_boot_program(self, transitions):
        event_list = sorted(list(set([d.event for d in transitions if d.event is not None])))
        menu_list = '\n'.join([self._transition_menu(i + 1, event_list[i]) for i in range(len(event_list))])
        case_list = '\n'.join([self._transition_case(i + 1, event_list[i]) for i in range(len(event_list))])
        ret = f"""
IControllee controllee = new ConsoleOutControllee();
StateController stateController = new StateController(controllee);

int number = 1; 
while(number != 0)
{{
    Console.WriteLine($"current state: {{stateController.GetCurrentStateName()}}");
    if(stateController.TryTransitWithoutEvent())
    {{
        continue; 
    }}
{menu_list}
    Console.WriteLine("");
    Console.WriteLine("0. exit");
    string? line = Console.ReadLine();
    if(int.TryParse(line, out number))
    {{
        switch(number)
        {{
            case 0:
                break;
{case_list}
            default:
                Console.WriteLine($"Invalid number: {{number}}");
                break;
        }}
    }}
}}
        """
        return ret
