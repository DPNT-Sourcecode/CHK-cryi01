from solutions.CHK import checkout
import pytest


class TestCheckout():
    def test_valid_checkout(self):
        assert checkout_solution.checkout("A, B, C, D") == "Hello, Craftsman!"

