from solutions.CHK import checkout_solution
import pytest


class TestCheckout():
    def test_valid_checkout(self):
        assert checkout_solution.checkout("A, B, C, D") == 115
        assert checkout_solution.checkout("3A, 2B, C, D") == 210
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("2B, C, D") == 80
        assert checkout_solution.checkout("C, D") == 35

