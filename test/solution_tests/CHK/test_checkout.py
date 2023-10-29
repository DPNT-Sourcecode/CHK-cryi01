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
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("EEEEB") == 160
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("EEEB") == 120
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAAAAA") == 300
        assert checkout_solution.checkout("BEBEEE") == 160
        assert checkout_solution.checkout("ABCDEABCDE") == 280
        assert checkout_solution.checkout("ABCDECBAABCABBAAAEEAA") == 665
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFF") == 40
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("FFFFFFF") == 50
        assert checkout_solution.checkout("HHHHH") == 45
        assert checkout_solution.checkout("HHHHHH") == 55
        assert checkout_solution.checkout("HHHHHHHHHH") == 80
        assert checkout_solution.checkout("KK") == 150
        assert checkout_solution.checkout("NNNM") == 120
        assert checkout_solution.checkout("PPPPP") == 200
        assert checkout_solution.checkout("QQQ") == 80
        assert checkout_solution.checkout("RRRQQ") == 180
        assert checkout_solution.checkout("UUUU") == 120
        assert checkout_solution.checkout("VVV") == 130
        assert checkout_solution.checkout("VVVVV") == 220
        assert checkout_solution.checkout("STXSTXSTAAA") == 254
    
    def test_invalid_checkout(self):
        assert checkout_solution.checkout("-") == -1
        assert checkout_solution.checkout("AxA") == -1
        



