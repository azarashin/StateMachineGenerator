from cpp_generator import CPPGenerator
from state_machine_generator import StateMachineGenerator
from code_filter import filter_code

import glob
import os

def test_cpp_generator_05_dump():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test05.puml', 'r').read()
    generator = StateMachineGenerator()
    exist_file_list = glob.glob("./test/result/*.cpp")
    for file in exist_file_list:
        os.remove(file)

    files = generator.generate_for_puml(puml, cpp_generator)
    for file in files:
        path = f'./test/result/{file}'
        with open(path, 'w') as f:
            f.write(filter_code(files[file]))
    
def test_cpp_generator_05_01():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test05.puml', 'r').read()
    istate = open('./test/data/cpp/test05/BaseState.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'BaseState.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['BaseState.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test05/BaseState.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'BaseState.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['BaseState.h'])
    assert expected == actual

def test_cpp_generator_05_02():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test05.puml', 'r').read()
    istate = open('./test/data/cpp/test05/IControllee.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'IControllee.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['IControllee.h'])
    assert expected == actual

def test_cpp_generator_05_03():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test05.puml', 'r').read()
    istate = open('./test/data/cpp/test05/ConsoleOutControllee.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'ConsoleOutControllee.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['ConsoleOutControllee.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test05/ConsoleOutControllee.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'ConsoleOutControllee.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['ConsoleOutControllee.h'])
    assert expected == actual

def test_cpp_generator_05_04():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test05.puml', 'r').read()
    istate = open('./test/data/cpp/test05/StateController.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateController.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateController.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test05/StateController.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateController.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateController.h'])
    assert expected == actual

def test_cpp_generator_05_05():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test05.puml', 'r').read()
    istate = open('./test/data/cpp/test05/Program.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'Program.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['Program.cpp'])
    assert expected == actual

def test_cpp_generator_05_06():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test05.puml', 'r').read()
    istate = open('./test/data/cpp/test05/StateState1.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateState1.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState1.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test05/StateState1.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateState1.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState1.h'])
    assert expected == actual

def test_cpp_generator_05_07():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test05.puml', 'r').read()
    istate = open('./test/data/cpp/test05/StateState2.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateState2.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState2.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test05/StateState2.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateState2.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState2.h'])
    assert expected == actual
    
def test_cpp_generator_05_08():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test05.puml', 'r').read()
    istate = open('./test/data/cpp/test05/StateState4.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateState4.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState4.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test05/StateState4.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateState4.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState4.h'])
    assert expected == actual
    
def test_cpp_generator_05_09():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test05.puml', 'r').read()
    istate = open('./test/data/cpp/test05/StateState21.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateState21.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState21.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test05/StateState21.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateState21.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState21.h'])
    assert expected == actual
    
def test_cpp_generator_05_10():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test05.puml', 'r').read()
    istate = open('./test/data/cpp/test05/StateState31.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateState31.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState31.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test05/StateState31.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateState31.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateState31.h'])
    assert expected == actual
    
