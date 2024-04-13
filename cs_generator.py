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
        self._icontrollee_class_name = icontrollee_class_name
        self._base_state_class_name = base_state_class_name
        self._state_controller_class_name = state_controller_class_name
        self._console_controllee_class_name = console_controllee_class_name

    def generate_files(self, states, transitions):
        ret = {}
        ret[f'{self._icontrollee_class_name}.cs'] = self.generate_controllee_interface(transitions)
        ret[f'{self._base_state_class_name}.cs'] = self.generate_base_state(transitions)
        ret[f'{self._state_controller_class_name}.cs'] = self.generate_state_controller(states, transitions)
        ret[f'{self._console_controllee_class_name}.cs'] = self.generate_console_out_controllee(transitions)
        state_classes = self.generate_state_classes(states, transitions)
        for state in state_classes:
            ret[f'{self._prefix_state}{state.name}.cs'] = state_classes[state]
        return ret
    
    def transition_method(self, event):
        return f"""\tpublic virtual {self._base_state_class_name}? {self._prefix_method}{event}()
\t{{
\t\t_controllee.NoTransition(GetStateName(), "{event}");
\t\treturn this;
\t}}
"""
    
    def generate_base_state(self, transitions):
        state_list = '\n'.join([self.transition_method(d.event) for d in transitions if d.event is not None])
        ret = f"""
abstract public class {self._base_state_class_name}
{{
\tprivate IControllee _controllee; 
\tpublic BaseState(IControllee controllee)
\t{{
\t\t_controllee = controllee;
\t}}
{state_list}
\tprotected abstract string GetStateName();
}}
        """
        return ret

    def action_method(self, action):
        return f'\tvoid {self._prefix_action_method}{action}();'
        
    def generate_controllee_interface(self, transitions):
        action_transitions = [d for d in transitions if d.action is not None]
        action_transitions = sorted(action_transitions, key=lambda x: x.action)
        action_list = '\n'.join([self.action_method(d.action) for d in action_transitions])
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
        action_list = '\n'.join([self.console_out_action_method(d.action) for d in transitions if d.action is not None])
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

    def action_execution_method(self, event):
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

    def generate_state_controller(self, states, transitions):
        initials = [d.state_to for d in transitions if d.state_from is None]
        state_declarations = '\n'.join([self.state_declaration(d) for d in sorted(states, key=lambda x: x.name)])
        set_state_declarations = '\n'.join([self.setup_state_declaration(d) for d in sorted(states, key=lambda x: x.name)])
        event_transitions = [d for d in transitions if d.event is not None]
        event_transitions = sorted(event_transitions, key=lambda x: x.action)
        action_execution_list = '\n'.join([self.action_execution_method(d.event) for d in event_transitions])
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
\t\t_currentState = {self._prefix_instance_of}{initials[0]}; 
\t}}
{action_execution_list}
}}
"""
        return ret
    
    def generate_transition(self, event, action, next_state):
        if action is None:
            action_sequence = ""
        else:
            action_sequence = f"\t\t_controllee.{self._prefix_action_method}{action}();"
        if next_state == "[*]":
            next_state_sequence = "\t\treturn null;"
        else:
            next_state_sequence = f"\t\treturn _stateController.{self._prefix_instance_of}{next_state};"
        ret = f"""
\tpublic override {self._base_state_class_name}? {self._prefix_method}{event}()
\t{{
{action_sequence}
{next_state_sequence}
\t}}
"""
        return ret

    def generate_state_class(self, state, transitions):
        target_transitions = [d for d in transitions if d.state_from == state.name]
        transition_codes = '\n'.join([self.generate_transition(d.event, d.action, d.state_to) for d in sorted(target_transitions, key=lambda x: x.event)])
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
        
        ret = f"""
{description_body}
public class {self._prefix_state}{state.name} : BaseState
{{
\tprivate {self._state_controller_class_name} _stateController; 
\tprivate {self._icontrollee_class_name} _controllee; 
\tpublic {self._prefix_state}{state.name}({self._state_controller_class_name} stateController, {self._icontrollee_class_name} controllee) : base(controllee)
\t{{
\t\t_stateController = stateController;
\t\t_controllee = controllee;
\t}}
{transition_codes}
\tprotected override string GetStateName()
\t{{
\t\treturn "{state.name}"; 
\t}}
}}
        """
        return ret

    def generate_state_classes(self, states, transitions):
        return {d:self.generate_state_class(d, transitions) for d in states}

