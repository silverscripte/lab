class Account:
    '''
    A class representing details for an account object
    '''

    def __init__(self, name: str) -> None:
        '''
        Constructor to set up initial state of the account object
        :param name: Name of account
        '''
        self.__account_name = name
        self.__account_balance = 0


    def deposit(self, amount: float) -> bool:
        '''
        Method to add money to account_balance
        :param amount: The amount to be added to the balance if it is positive
        :return: True if it worked, False if it did  not
        '''
        if amount > 0:
            self.__account_balance += amount
            return True

        else:
            return False

    def withdraw(self, amount: float) -> bool:
        '''
        Method to reduce money in the account_balance
        :param amount: The amount to be taken out of the account
        :return: False if no money was withdrawn, True if money was withdrawn
        '''
        if amount <= 0 or (amount > self.__account_balance):
            return False

        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        '''
        Method to access the balance of the account
        :return: int value of account_balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Method to access the name of the account
        :return: the string name of account_name
        '''
        return self.__account_name
