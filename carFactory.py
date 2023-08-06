from abc import ABC, abstractmethod
from battery import SpindlerBattery, NubbinBattery
from engine import CapuletEngine, WilloughbyEngine, StermanEngine


import datetime

class Car(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
    
class Calliope(Car):
    def __init__(self,current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        self.engine = CapuletEngine(last_service_mileage, current_mileage)
        self.battery = SpindlerBattery(last_service_date, current_date)

    def needs_service(self):
        return (self.battery.needs_service and self.engine.needs_service)
    
class Glissade(Car):
    def __init__(self,current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        self.engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.battery = SpindlerBattery(last_service_date, current_date)

    def needs_service(self):
        return (self.battery.needs_service and self.engine.needs_service)
    
class Palindrome(Car):
    def __init__(self,current_date: datetime, last_service_date: datetime, warning_light_on: bool):
        self.engine = StermanEngine(warning_light_on)
        self.battery = SpindlerBattery(last_service_date, current_date)

    def needs_service(self):
        return (self.battery.needs_service and self.engine.needs_service)
    
class Rorschach(Car):
    def __init__(self,current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        self.engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.battery = NubbinBattery(last_service_date, current_date)

    def needs_service(self):
        return (self.battery.needs_service and self.engine.needs_service)
    
class Thovex(Car):
    def __init__(self,current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        self.engine = CapuletEngine(last_service_mileage, current_mileage)
        self.battery = NubbinBattery(last_service_date, current_date)
        
    def needs_service(self):
        return (self.battery.needs_service and self.engine.needs_service)