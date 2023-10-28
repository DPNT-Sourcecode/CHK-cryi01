from solutions.CHK import checkout_solution
import pytest


class TestCheckout():
    def test_valid_checkout(self):
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("CD") == 35
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("BBCD") == 80
        assert checkout_solution.checkout("BBBB") == 90
        assert checkout_solution.checkout("AAABBCD") == 210
        assert checkout_solution.checkout("AAAAAA") == 260
        assert checkout_solution.checkout("AAAAA") == 230
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("EEEEB") == 160
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("EEEB") == 120
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAAAAA") == 300
    
    def test_invalid_checkout(self):
        assert checkout_solution.checkout("-") == -1
        assert checkout_solution.checkout("AxA") == -1
        





