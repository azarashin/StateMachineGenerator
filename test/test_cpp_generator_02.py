from cpp_generator import CPPGenerator
from state_machine_generator import StateMachineGenerator
from code_filter import filter_code

import glob
import os

def test_cpp_generator_02_dump():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test02.puml', 'r').read()
    generator = StateMachineGenerator()
    exist_file_list = glob.glob("./test/result/*.cpp")
    for file in exist_file_list:
        os.remove(file)

    files = generator.generate_for_puml(puml, cpp_generator)
    for file in files:
        path = f'./test/result/{file}'
        with open(path, 'w') as f:
            f.write(filter_code(files[file]))
    
def test_cpp_generator_02_01():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test02.puml', 'r').read()
    istate = open('./test/data/cpp/test02/BaseState.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'BaseState.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['BaseState.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test02/BaseState.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'BaseState.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['BaseState.h'])
    assert expected == actual

def test_cpp_generator_02_02():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test02.puml', 'r').read()
    istate = open('./test/data/cpp/test02/IControllee.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'IControllee.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['IControllee.h'])
    assert expected == actual

def test_cpp_generator_02_03():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test02.puml', 'r').read()
    istate = open('./test/data/cpp/test02/ConsoleOutControllee.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'ConsoleOutControllee.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['ConsoleOutControllee.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test02/ConsoleOutControllee.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'ConsoleOutControllee.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['ConsoleOutControllee.h'])
    assert expected == actual

def test_cpp_generator_02_04():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test02.puml', 'r').read()
    istate = open('./test/data/cpp/test02/StateController.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateController.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateController.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test02/StateController.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateController.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateController.h'])
    assert expected == actual

def test_cpp_generator_02_05():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test02.puml', 'r').read()
    istate = open('./test/data/cpp/test02/Program.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'Program.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['Program.cpp'])
    assert expected == actual

def test_cpp_generator_02_06():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test02.puml', 'r').read()
    istate = open('./test/data/cpp/test02/StateState1.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateState1.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState1.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test02/StateState1.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateState1.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState1.h'])
    assert expected == actual

def test_cpp_generator_02_07():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test02.puml', 'r').read()
    istate = open('./test/data/cpp/test02/StateState2.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateState2.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState2.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test02/StateState2.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateState2.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState2.h'])
    assert expected == actual
    
