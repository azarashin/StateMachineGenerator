from typescript_generator import TypeScriptGenerator
from state_machine_generator import StateMachineGenerator
from code_filter import filter_code

import glob
import os

def test_typescript_generator_03_dump():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    generator = StateMachineGenerator()
    exist_file_list = glob.glob("./test/result/*.ts")
    for file in exist_file_list:
        os.remove(file)

    files = generator.generate_for_puml(puml, ts_generator)
    for file in files:
        path = f'./test/result/{file}'
        with open(path, 'w') as f:
            f.write(filter_code(files[file]))
    
def test_typescript_generator_03_01():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/typescript/test03/BaseState.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'BaseState.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['BaseState.ts'])
    assert expected == actual

def test_typescript_generator_03_02():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/typescript/test03/IControllee.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'IControllee.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['IControllee.ts'])
    assert expected == actual

def test_typescript_generator_03_03():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/typescript/test03/ConsoleOutControllee.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'ConsoleOutControllee.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['ConsoleOutControllee.ts'])
    assert expected == actual

def test_typescript_generator_03_04():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/typescript/test03/StateController.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'StateController.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateController.ts'])
    assert expected == actual

def test_typescript_generator_03_05():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/typescript/test03/app.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'app.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['app.ts'])
    assert expected == actual

def test_typescript_generator_03_06():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/typescript/test03/StateConfiguring.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'StateConfiguring.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateConfiguring.ts'])
    assert expected == actual

def test_typescript_generator_03_07():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/typescript/test03/StateEscaped.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'StateEscaped.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateEscaped.ts'])
    assert expected == actual

def test_typescript_generator_03_08():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/typescript/test03/StateIdle.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'StateIdle.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateIdle.ts'])
    assert expected == actual

def test_typescript_generator_03_09():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/typescript/test03/StateInitial.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'StateInitial.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateInitial.ts'])
    assert expected == actual

def test_typescript_generator_03_10():
    ts_generator = TypeScriptGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/typescript/test03/StateNotShooting.ts').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, ts_generator)
    assert 'StateNotShooting.ts' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateNotShooting.ts'])
    assert expected == actual
