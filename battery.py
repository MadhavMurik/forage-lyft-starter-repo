from abc import ABC, abstractmethod
from utils import add_years_to_date

class Battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
    
    
class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return add_years_to_date(self.last_service_date, 3) < self.current_date


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return add_years_to_date(self.last_service_date, 4) < self.current_date
