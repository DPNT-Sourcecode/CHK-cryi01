from solutions.SUM import sum_solution


class TestSum():
    def test_valid_sum(self):
        assert sum_solution.compute(1, 2) == 3
        assert sum_solution.compute(50, 23) == 73
        
	
    def test_invalid_sum(self):
        assert sum_solution.compute(1, 2) == 3
        assert sum_solution.compute(50, 23) == 73

