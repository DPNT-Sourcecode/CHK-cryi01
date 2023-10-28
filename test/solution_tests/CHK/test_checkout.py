from solutions.CHK import checkout_solution
import pytest


class TestCheckout():
    def test_valid_checkout(self):
        #assert checkout_solution.checkout("A, B, C, D") == ""
        #assert checkout_solution.checkout("D") == 145
        #assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("2B, C, D") == ""
        assert checkout_solution.checkout("C, D") == 35






