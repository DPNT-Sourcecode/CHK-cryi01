from solutions.HLO import hello_solution
import pytest


class TestHello():
    def test_valid_hello(self):
        assert hello_solution.hello("Craftsman") == "Hello, Craftsman!"
        assert hello_solution.hello("Mr. X") == "Hello, Mr. X!"
        assert hello_solution.hello("John") == "Hello, John!"




