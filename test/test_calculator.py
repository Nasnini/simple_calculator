from simple_calculator.calculator import Calculations

#Instance of the
calculator = Calculations()


#Testing two numbers using addition
def test_adding_two_numbers():
    assert calculator.add(1, 3) == 4

#Testing multiple numbers using addition
def test_adding_multiple_numbers():
    assert calculator.add(1, 3, 6, 9, 3) == 22

#Testing two numbers using multiplication
def test_multiplying_two_numbers():
    assert calculator.multiply(1, 3) == 3
    
#Testing multiple numbers using multiplication
def test_multiplying_multiple_numbers():
     assert calculator.multiply(8, 2) == 16
