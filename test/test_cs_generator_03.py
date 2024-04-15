from cs_generator import CSGenerator
from state_machine_generator import StateMachineGenerator
from code_filter import filter_code

import glob
import os

def test_cs_generator_03_dump():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    generator = StateMachineGenerator()
    exist_file_list = glob.glob("./test/result/*.cs")
    for file in exist_file_list:
        os.remove(file)

    files = generator.generate_for_puml(puml, cs_generator)
    for file in files:
        path = f'./test/result/{file}'
        with open(path, 'w') as f:
            f.write(filter_code(files[file]))
    
def test_cs_generator_03_01():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cs/test03/BaseState.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'BaseState.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['BaseState.cs'])
    assert expected == actual

def test_cs_generator_03_03():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cs/test03/IControllee.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'IControllee.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['IControllee.cs'])
    assert expected == actual

def test_cs_generator_03_03():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cs/test03/ConsoleOutControllee.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'ConsoleOutControllee.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['ConsoleOutControllee.cs'])
    assert expected == actual

def test_cs_generator_03_04():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cs/test03/StateController.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateController.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateController.cs'])
    assert expected == actual

def test_cs_generator_03_05():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cs/test03/StateConfiguring.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateConfiguring.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateConfiguring.cs'])
    assert expected == actual

def test_cs_generator_03_06():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cs/test03/StateEscaped.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateEscaped.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateEscaped.cs'])
    assert expected == actual

def test_cs_generator_03_07():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cs/test03/StateIdle.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateIdle.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateIdle.cs'])
    assert expected == actual

def test_cs_generator_03_08():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cs/test03/StateInitial.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateInitial.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateInitial.cs'])
    assert expected == actual
