class Ticker:
    def __init__(self, symbol: str):
        self.symbol = symbol
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self,other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.symbol)