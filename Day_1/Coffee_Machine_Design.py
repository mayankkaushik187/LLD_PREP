from abc import ABC, abstractmethod


class Grinder(ABC):
    @abstractmethod
    def grind(self):
        pass

class Brewer(ABC):
    @abstractmethod
    def brew(self):
        pass

class Storage(ABC):
    @abstractmethod
    def add_beans(self, amount: int) -> None:
        pass
    
    @abstractmethod
    def get_beans(self, amount: int) -> int:
        pass

    @abstractmethod
    def get_available(self) -> int:
        pass


class BasicGrinder(Grinder):
    def grind(self, beans: int) -> int:
        print(f"Grinding {beans}g of beans right now!")
        return beans
    
class BasicBrewer(Brewer):
    def brew(self, grounds: int) -> None:
        print(f"Brewing {grounds}g of grounded beans!")

class BasicStorage(Storage):
    def __init__(self):
        self._beans = 0

    def add_beans(self, amount) -> None:
        if amount < 0:
            raise ValueError("Amount cannot be negative!")
        self._beans += amount

    def get_beans(self, amount) -> int:
        taken = min(amount, self._beans)
        self._beans -= taken
        return taken
    def get_available(self) -> int:
        return self._beans
    
class CoffeeMachine:
    def __init__(self, grinder: Grinder, brewer: Brewer, storage: Storage):
        self.grinder = grinder
        self.brewer = brewer
        self.storage = storage

    def make_coffee(self, required_beans: int) -> None:
        if self.storage.get_available() < required_beans:
            raise ValueError("Not enough beans available!")
        
        beans = self.storage.get_beans(required_beans)
        grounded_beans = self.grinder.grind(beans)
        self.brewer.brew(grounded_beans)
        
# if __name__ == "main":
grinder = BasicGrinder()
brewer = BasicBrewer()
storage = BasicStorage()

storage.add_beans(200)
coffee_machine = CoffeeMachine(grinder, brewer, storage)
coffee_machine.make_coffee(30)
print(f"Remaining beans: {storage.get_available()}g")