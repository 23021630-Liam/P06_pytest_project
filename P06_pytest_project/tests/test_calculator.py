from Calculator.calculator import Calculator 

class TestCalculator:
    def test_add(self): 

        # arrange 

        a = 11

        b = 1

        cal = Calculator() 

    

        # act 

        result = cal.add(a, b) 

    

        # assert 

        expected = 12 

        assert result == expected 

    def test_subtract(self): 

        # arrange 

        a = 3 

        b = 2 

        cal = Calculator() 

    

        # act 

        result = cal.subtract(a, b) 

    

        # assert 

        expected = 1
        assert result == expected 

    def test_multiply(self): 

        # arrange 

        a = 3 

        b = 2 

        cal = Calculator() 

    

        # act 

        result = cal.multiply(a, b) 

    

        # assert 

        expected = 6

        assert result == expected 

    def test_divide(self): 

        # arrange 

        a = 9 

        b = 3

        cal = Calculator() 

    

        # act 

        result = cal.divide(a, b) 

    

        # assert 

        expected = 3 

        assert result == expected 