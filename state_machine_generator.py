import sys
import os
import argparse
from code_filter import filter_code

from state import StateManager
from cs_generator import CSGenerator

class StateMachineGenerator:
    
    def __init__(self):
        self._tab = ' ' * 4
    
    def generate(self, pumls):
        return {
            'file_path': 'source_body', 
            'file_path2': 'source_body2', 
            'file_path3': 'source_body3', 
            'file_path4': 'source_body4', 
            'ConsoleOutControllee.cs': 'source_body4', 
            }

    def generate_for_puml(self, puml_body, generator):
        lines = filter_code(puml_body).split('\n')
        if len(lines) <= 2:
            return (False, 'puml does not contains @startuml or/and @enduml.')
        if lines[0] != '@startuml':
            return (False, 'beginning of puml does not match to @startuml.')
        if lines[-1] != '@enduml':
            return (False, 'end of puml does not match to @enduml.')
        state_manager = StateManager(puml_body)
        files = generator.generate_files(state_manager)
        files = {d: files[d].replace('\t', self._tab) for d in files}
        return files

def get_args():
    parser = argparse.ArgumentParser()

    if sys.stdin.isatty():
        parser.add_argument("puml", help="path to .puml file", type=str)

    parser.add_argument("--mode", type=str, required=True, help="cs: C#\n")
    parser.add_argument("--output", type=str, required=True, help="path to output directory")

    args = parser.parse_args()

    return(args)

if __name__ == '__main__':
    args = get_args()
    if hasattr(args, 'puml'):
        puml_path = args.puml
        puml = open(puml_path, 'r').read()
    else:
        puml = sys.stdin.read()
    

    mode = args.mode
    output_dir = args.output
    generator = StateMachineGenerator()
    code_generator = None
    

    if mode == 'cs':
        code_generator = CSGenerator()

    if code_generator is not None:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        files = generator.generate_for_puml(puml, code_generator)
        for relative_path in files:
            path = os.path.join(output_dir, relative_path)
            with open(path, 'w') as f:
                f.write(files[relative_path])
