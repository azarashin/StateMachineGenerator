from cs_generator import CSGenerator
from state_machine_generator import StateMachineGenerator
from code_filter import filter_code

import glob
import os

def test_cs_generator_04_dump():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test04.puml', 'r').read()
    generator = StateMachineGenerator()
    exist_file_list = glob.glob("./test/result/*.cs")
    for file in exist_file_list:
        os.remove(file)

    files = generator.generate_for_puml(puml, cs_generator)
    for file in files:
        path = f'./test/result/{file}'
        with open(path, 'w') as f:
            f.write(filter_code(files[file]))
    
def test_cs_generator_04_01():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test04.puml', 'r').read()
    istate = open('./test/data/cs/test04/BaseState.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'BaseState.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['BaseState.cs'])
    assert expected == actual

def test_cs_generator_04_02():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test04.puml', 'r').read()
    istate = open('./test/data/cs/test04/IControllee.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'IControllee.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['IControllee.cs'])
    assert expected == actual

def test_cs_generator_04_03():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test04.puml', 'r').read()
    istate = open('./test/data/cs/test04/ConsoleOutControllee.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'ConsoleOutControllee.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['ConsoleOutControllee.cs'])
    assert expected == actual

def test_cs_generator_04_04():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test04.puml', 'r').read()
    istate = open('./test/data/cs/test04/StateController.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateController.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateController.cs'])
    assert expected == actual

def test_cs_generator_04_05():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test04.puml', 'r').read()
    istate = open('./test/data/cs/test04/Program.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'Program.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['Program.cs'])
    assert expected == actual

def test_cs_generator_04_06():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test04.puml', 'r').read()
    istate = open('./test/data/cs/test04/StateConfiguring.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateConfiguring.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateConfiguring.cs'])
    assert expected == actual

def test_cs_generator_04_07():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test04.puml', 'r').read()
    istate = open('./test/data/cs/test04/StateEscaped.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateEscaped.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateEscaped.cs'])
    assert expected == actual

def test_cs_generator_04_08():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test04.puml', 'r').read()
    istate = open('./test/data/cs/test04/StateIdle.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateIdle.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateIdle.cs'])
    assert expected == actual

def test_cs_generator_04_09():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test04.puml', 'r').read()
    istate = open('./test/data/cs/test04/StateInitial.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateInitial.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateInitial.cs'])
    assert expected == actual

def test_cs_generator_03_10():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cs/test03/StateNotShooting.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateNotShooting.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateNotShooting.cs'])
    assert expected == actual
