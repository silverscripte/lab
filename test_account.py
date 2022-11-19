import pytest
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('Jane')
        self.a2 = Account('John')

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == 'Jane'
        assert self.a2.get_name() == 'John'



    def test_deposit(self):
        pass

    def test_withdraw(self):
        pass





