import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from state_machine_generator import StateMachineGenerator
from code_filter import filter_code

def test_01():
    generator = StateMachineGenerator()
    pumls = [
        open('./test/data/plant_uml/test01.puml', 'r').read()
    ]
    
    expected_path = './test/data/cs/test01/'
    expected_files = [
        'ConsoleOutControllee.cs', 
        'IControllee.cs', 
        'IState.cs', 
        'StateController.cs', 
        'StateState1.cs', 
        'StateState2.cs', 
    ]
    
    files = generator.Generate(pumls)
    
    for file in expected_files:
        assert file in files
        path = f'{expected_path}{file}'
        source_content = open(path, 'r').read()
        
        content_lines = filter_code(source_content).split()
        actual_lines = filter_code(files[file]).split()
        
        assert len(content_lines) == len(actual_lines)

        for i in range(len(content_lines)):
            if not actual_lines[i] == content_lines[i]:
                print(f'PATH: {path}, LINE:{i}')
                print(f'Actual: {actual_lines[i]}')
                print(f'Expected: {content_lines[i]}')
            assert content_lines[i] == actual_lines[i]
