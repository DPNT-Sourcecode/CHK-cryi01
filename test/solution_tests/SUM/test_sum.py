from solutions.SUM import sum_solution
import pytest


class TestSum():
    def test_valid_sum(self):
        assert sum_solution.compute(1, 2) == 3
        assert sum_solution.compute(50, 23) == 73
        assert sum_solution.compute(0, 0) == 0
        assert sum_solution.compute(100, 100) == 200
        
    def test_raise_errors(self):
        with pytest.raises(ValueError):
            # test usage of non-positive numbers
            sum_solution.compute(-5, 10)
            # test out of limits inputs
            sum_solution.compute(120, 10)

