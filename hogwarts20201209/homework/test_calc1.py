# -*- coding: UTF-8 -*-

import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_method(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_method(self):
        print("结束计算")

    @pytest.mark.parametrize("a", [-100, -1, 0, 1, 100],
                             ids=[f" a={i} " for i in [-100, -1, 0, 1, 100]])
    @pytest.mark.parametrize("b", [-100, -1, 0, 1, 100],
                             ids=[f" b={i} " for i in [-100, -1, 0, 1, 100]])
    def test_add(self, a, b):
        res = self.calc.add(a, b)
        real = a + b
        print(f"计算: {a} + {b}")
        print(f"程序结果为：{res}")
        print(f"实际结果为：{real}")
        assert res == real

    @pytest.mark.parametrize("a", [-100, -1, 0, 1, 100],
                             ids=[f" a={i} " for i in [-100, -1, 0, 1, 100]])
    @pytest.mark.parametrize("b", [-100, -1, 0, 1, 100],
                             ids=[f" b={i} " for i in [-100, -1, 0, 1, 100]])
    def test_sub(self, a, b):
        res = self.calc.sub(a, b)
        real = a - b
        print(f"计算: {a} - {b}")
        print(f"程序结果为：{res}")
        print(f"实际结果为：{real}")
        assert res == real

    @pytest.mark.parametrize("a", [-100, -1, 0, 1, 100],
                             ids=[f" a={i} " for i in [-100, -1, 0, 1, 100]])
    @pytest.mark.parametrize("b", [-100, -1, 0, 1, 100],
                             ids=[f" b={i} " for i in [-100, -1, 0, 1, 100]])
    def test_mul(self, a, b):
        res = self.calc.mul(a, b)
        real = a * b
        print(f"计算: {a} * {b}")
        print(f"程序结果为：{res}")
        print(f"实际结果为：{real}")
        assert res == real

    @pytest.mark.parametrize("a", [-100, -1, 0, 1, 100],
                             ids=[f" a={i} " for i in [-100, -1, 0, 1, 100]])
    @pytest.mark.parametrize("b", [-100, -1, 1, 100],
                             ids=[f" b={i} " for i in [-100, -1, 1, 100]])
    def test_div(self, a, b):
        res = self.calc.div(a, b)
        real = a / b
        print(f"计算: {a} / {b}")
        print(f"程序结果为：{res}")
        print(f"实际结果为：{real}")
        assert res == real


if __name__ == '__main__':
    pytest.main(["-sv", "hogwarts-20201209/homework/test_calc.py"])
