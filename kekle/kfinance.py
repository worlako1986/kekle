

class Kmoney:
    """
    Kmoney format currency
    Abbreviation: kmy
    """

    def __init__(self):
        pass

    @staticmethod
    def mformat(amount=0.00,ndecimal=2,num=20):
        """
        mformat, take the amount format it and return the string copy,
        ndecimal is the number of decimal point, and is optional
        num is the of digit to accept.
        mformat(amount=0.00,ndecimal=2,num=20)
        """
        try:
            return str( '{:'+str(num)+',.'+str(ndecimal)+'f}' ).format(amount).strip()
        except Exception as e:
            return str(e)
