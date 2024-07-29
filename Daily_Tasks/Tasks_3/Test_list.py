import pytest

@pytest.fixture
def sample_data():
    return [('Raj', 'Hello'), ('Aman', 'Hi'), ('Sushil', 'Hey')]

def sort_list_of_tuples(data, by_name=True):
    if len(data) > 0:
        if by_name:
            sortpos = 0 
        else:
            sortpos = 1  
        sortedData = sorted(data, key=lambda x: x[sortpos])
    else:
        sortedData = []  
    return sortedData

def test_sort_by_message(sample_data):
    sorted_data = sort_list_of_tuples(sample_data, by_name=False)
    assert sorted_data == [('Raj', 'Hello'), ('Sushil', 'Hey'), ('Aman', 'Hi')]

def test_sort_by_name(sample_data):
    assert sort_list_of_tuples(sample_data) == [('Aman', 'Hi'), ('Raj', 'Hello'), ('Sushil', 'Hey')]

def test_empty_list():
    assert sort_list_of_tuples([]) == []
