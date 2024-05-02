from cs_generator import CSGenerator
from state_machine_generator import StateMachineGenerator
from code_filter import filter_code

import glob
import os

def test_cs_generator_06_dump():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test06.puml', 'r').read()
    generator = StateMachineGenerator()
    exist_file_list = glob.glob("./test/result/*.cs")
    for file in exist_file_list:
        os.remove(file)

    files = generator.generate_for_puml(puml, cs_generator)
    for file in files:
        path = f'./test/result/{file}'
        with open(path, 'w') as f:
            f.write(filter_code(files[file]))
    
def test_cs_generator_06_01():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test06.puml', 'r').read()
    istate = open('./test/data/cs/test06/BaseState.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'BaseState.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['BaseState.cs'])
    assert expected == actual

def test_cs_generator_06_02():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test06.puml', 'r').read()
    istate = open('./test/data/cs/test06/IControllee.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'IControllee.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['IControllee.cs'])
    assert expected == actual

def test_cs_generator_06_03():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test06.puml', 'r').read()
    istate = open('./test/data/cs/test06/ConsoleOutControllee.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'ConsoleOutControllee.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['ConsoleOutControllee.cs'])
    assert expected == actual

def test_cs_generator_06_04():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test06.puml', 'r').read()
    istate = open('./test/data/cs/test06/StateController.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateController.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateController.cs'])
    assert expected == actual

def test_cs_generator_06_05():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test06.puml', 'r').read()
    istate = open('./test/data/cs/test06/Program.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'Program.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['Program.cs'])
    assert expected == actual

def test_cs_generator_06_06():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test06.puml', 'r').read()
    istate = open('./test/data/cs/test06/Statelong1.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'Statelong1.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['Statelong1.cs'])
    assert expected == actual

def test_cs_generator_06_07():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test06.puml', 'r').read()
    istate = open('./test/data/cs/test06/Statelong2.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'Statelong2.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['Statelong2.cs'])
    assert expected == actual

def test_cs_generator_06_08():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test06.puml', 'r').read()
    istate = open('./test/data/cs/test06/StateProcessData.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateProcessData.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateProcessData.cs'])
    assert expected == actual

def test_cs_generator_06_09():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test06.puml', 'r').read()
    istate = open('./test/data/cs/test06/StateState1.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateState1.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState1.cs'])
    assert expected == actual

def test_cs_generator_03_10():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test06.puml', 'r').read()
    istate = open('./test/data/cs/test06/StateState2.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateState2.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState2.cs'])
    assert expected == actual

def test_cs_generator_03_11():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test06.puml', 'r').read()
    istate = open('./test/data/cs/test06/StateState3.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateState3.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState3.cs'])
    assert expected == actual

def test_cs_generator_03_12():
    cs_generator = CSGenerator()
    puml = open('./test/data/plant_uml/test06.puml', 'r').read()
    istate = open('./test/data/cs/test06/StateState4.cs').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cs_generator)
    assert 'StateState4.cs' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState4.cs'])
    assert expected == actual
