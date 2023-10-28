from solutions.CHK import checkout_solution
import pytest


class TestCheckout():
    def test_valid_checkout(self):
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("AAABBCD") == 210
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("BBCD") == 80
        assert checkout_solution.checkout("CD") == 35
        
    def test_raise_errors(self):
        with pytest.raises(ValueError):
            checkout_solution.checkout("-")




