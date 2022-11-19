from pytest import *
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

        assert self.a1.get_balance() == 0
        assert self.a2.get_balance() == 0



    def test_deposit(self):
        #a1 test
        assert self.a1.deposit(30) is True
        assert self.a1.get_balance() == 30

        assert self.a1.deposit(-30) is False
        assert self.a1.get_balance() == 30

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 30

        #a2 test
        assert self.a2.deposit(0) is False
        assert self.a2.get_balance() == 0

        assert self.a2.deposit(-10) is False
        assert self.a2.get_balance() == 0

        assert self.a2.deposit(12) is True
        assert self.a2.get_balance() == 12

    def test_withdraw(self):
        #a1 test
        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 0

        self.a1.deposit(30)

        assert self.a1.withdraw(10) is True
        assert self.a1.get_balance() == 20

        assert self.a1.withdraw(-10) is False
        assert self.a1.get_balance() == 20

        assert self.a1.withdraw(30) is False
        assert self.a1.get_balance() == 20

        #a2 test
        self.a2.deposit(12)

        assert self.a2.withdraw(2) is True
        assert self.a2.get_balance() == 10

        assert self.a2.withdraw(0) is False
        assert self.a2.get_balance() == 10

        assert self.a2.withdraw(-2) is False
        assert self.a2.get_balance() == 10

        assert self.a2.withdraw(15) is False
        assert self.a2.get_balance() == 10







