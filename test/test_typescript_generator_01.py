from typescript_generator import TypeScriptGenerator
from state_machine_generator import StateMachineGenerator
from code_filter import filter_code

import glob
import os

def test_typescript_generator_01_dump():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test01.puml', 'r').read()
    generator = StateMachineGenerator()
    exist_file_list = glob.glob("./test/result/*.ts")
    for file in exist_file_list:
        os.remove(file)

    files = generator.generate_for_puml(puml, ts_generator)
    for file in files:
        path = f'./test/result/{file}'
        with open(path, 'w') as f:
            f.write(filter_code(files[file]))
    
def test_typescript_generator_01_01():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test01.puml', 'r').read()
    istate = open('./test/data/typescript/test01/BaseState.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'BaseState.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['BaseState.ts'])
    assert expected == actual

def test_typescript_generator_01_02():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test01.puml', 'r').read()
    istate = open('./test/data/typescript/test01/IControllee.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'IControllee.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['IControllee.ts'])
    assert expected == actual

def test_typescript_generator_01_03():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test01.puml', 'r').read()
    istate = open('./test/data/typescript/test01/ConsoleOutControllee.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'ConsoleOutControllee.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['ConsoleOutControllee.ts'])
    assert expected == actual

def test_typescript_generator_01_04():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test01.puml', 'r').read()
    istate = open('./test/data/typescript/test01/StateController.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'StateController.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateController.ts'])
    assert expected == actual

def test_typescript_generator_01_05():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test01.puml', 'r').read()
    istate = open('./test/data/typescript/test01/app.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'app.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['app.ts'])
    assert expected == actual

def test_typescript_generator_01_06():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test01.puml', 'r').read()
    istate = open('./test/data/typescript/test01/StateState1.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'StateState1.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState1.ts'])
    assert expected == actual

def test_typescript_generator_01_07():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test01.puml', 'r').read()
    istate = open('./test/data/typescript/test01/StateState2.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'StateState2.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState2.ts'])
    assert expected == actual

    
