

class Kmoney:
    """docstring for ."""

    def __init__(self, number=20,ndigit=2):
        self.number = number
        self.ndigit = ndigit

    def format(self,amount=0.0,number=20,ndigit=2):
        return str('{:{number},.{ndigit}f}'.format(number=number,ndigit=ndigit)).format(amount)
