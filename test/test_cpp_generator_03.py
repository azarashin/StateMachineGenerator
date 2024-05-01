from cpp_generator import CPPGenerator
from state_machine_generator import StateMachineGenerator
from code_filter import filter_code

import glob
import os

def test_cpp_generator_03_dump():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    generator = StateMachineGenerator()
    exist_file_list = glob.glob("./test/result/*.cpp")
    for file in exist_file_list:
        os.remove(file)

    files = generator.generate_for_puml(puml, cpp_generator)
    for file in files:
        path = f'./test/result/{file}'
        with open(path, 'w') as f:
            f.write(filter_code(files[file]))
    
def test_cpp_generator_03_01():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cpp/test03/BaseState.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'BaseState.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['BaseState.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test03/BaseState.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'BaseState.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['BaseState.h'])
    assert expected == actual

def test_cpp_generator_03_02():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cpp/test03/IControllee.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'IControllee.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['IControllee.h'])
    assert expected == actual

def test_cpp_generator_03_03():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cpp/test03/ConsoleOutControllee.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'ConsoleOutControllee.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['ConsoleOutControllee.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test03/ConsoleOutControllee.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'ConsoleOutControllee.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['ConsoleOutControllee.h'])
    assert expected == actual

def test_cpp_generator_03_04():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cpp/test03/StateController.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateController.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateController.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test03/StateController.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateController.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateController.h'])
    assert expected == actual

def test_cpp_generator_03_05():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cpp/test03/Program.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'Program.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['Program.cpp'])
    assert expected == actual

def test_cpp_generator_03_06():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cpp/test03/StateConfiguring.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateConfiguring.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateConfiguring.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test03/StateConfiguring.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateConfiguring.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateConfiguring.h'])
    assert expected == actual

def test_cpp_generator_03_07():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cpp/test03/StateEscaped.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateEscaped.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateEscaped.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test03/StateEscaped.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateEscaped.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateEscaped.h'])
    assert expected == actual
    
def test_cpp_generator_03_08():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cpp/test03/StateIdle.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateIdle.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateIdle.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test03/StateIdle.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateIdle.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateIdle.h'])
    assert expected == actual
    
def test_cpp_generator_03_09():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cpp/test03/StateInitial.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateInitial.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateInitial.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test03/StateInitial.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateInitial.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateInitial.h'])
    assert expected == actual
    
def test_cpp_generator_03_10():
    cpp_generator = CPPGenerator()
    puml = open('./test/data/plant_uml/test03.puml', 'r').read()
    istate = open('./test/data/cpp/test03/StateNotShooting.cpp').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateNotShooting.cpp' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateNotShooting.cpp'])
    assert expected == actual

    istate = open('./test/data/cpp/test03/StateNotShooting.h').read()
    generator = StateMachineGenerator()
    files = generator.generate_for_puml(puml, cpp_generator)
    assert 'StateNotShooting.h' in files
    expected = filter_code(istate)
    actual = filter_code(files['StateNotShooting.h'])
    assert expected == actual
    
