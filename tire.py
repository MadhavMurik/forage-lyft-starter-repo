from abc import ABC, abstractmethod

class Tire(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
    
class Carrigan(Tire):
    def __init__(self, tireArray):
        self.tireArray = tireArray

    def needs_service(self) -> bool:
        for num in self.tireArray:
            if num >= 0.9:
                return True
        return False
    
class Octoprime(Tire):
    def __init__(self, tireArray):
        self.tireArray = tireArray

    def needs_service(self) -> bool:
        return sum(self.tireArray) >= 3