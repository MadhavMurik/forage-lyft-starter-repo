
from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage >= 30,000


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        # Implement logic specific to WilloughbyEngine
        # For example, consider the warning light status along with mileage for service decision
        return self.current_mileage - self.last_service_mileage >= 60000

class StermanEngine(Engine):
    def __init__(self, warning_light: bool):
        self.warning_light = warning_light

    def needs_service(self) -> bool:
        # Implement logic specific to WilloughbyEngine
        # For example, consider the warning light status along with mileage for service decision
        return  self.warning_light == False