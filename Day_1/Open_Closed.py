from abc import ABC, abstractmethod

#Bad Design
class BadDesignDiscount:
    def get_discount(self, customer_type):
        if customer_type == "VIP":
            return 0.2
        return 0.1
#-----------------------------------------------------------
#Good Design
class DiscountStrategy(ABC):
    @abstractmethod
    def get_discount(self): 
        pass

class VIPDiscount(ABC):
    def get_discount(self):
        return 0.2
    
class NormalDiscount(ABC):
    def get_discount(self):
        return 0.1
    

class GoodDesignDiscount:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def apply_discount(self):
        return self.strategy.get_discount()
    
vipManus = VIPDiscount()
normalManus = NormalDiscount()
discountForVIP = GoodDesignDiscount(vipManus)
discountForNormal = GoodDesignDiscount(normalManus)
print(discountForVIP.apply_discount())
print(discountForNormal.apply_discount())