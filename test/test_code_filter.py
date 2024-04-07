from code_filter import filter_code

def test_01():
    source = 'line1'
    expected = 'line1'
    assert filter_code(source) == expected

def test_02():
    source = """line1

line2
"""
    expected = """line1
line2"""
    assert filter_code(source) == expected

def test_03():
    source = """
line1

line2

"""
    expected = """line1
line2"""
    assert filter_code(source) == expected


def test_04():
    source = """

  line1
    
    line2

"""
    expected = """  line1
    line2"""
    assert filter_code(source) == expected
