from abc import ABC, abstractmethod
import datetime

class Battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
    
    
class SpindlerBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return self.current_date - self.last_service_date >= 730


class NubbinBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return self.current_date - self.last_service_date >= 1460
