from solutions.HLO import hello_solution
import pytest


class TestSum():
    def test_valid_sum(self):
        assert hello_solution.hello("Craftsman") == "Hello, World!"
        assert hello_solution.hello("Mr. X") == "Hello, World!"


