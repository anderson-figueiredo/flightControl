from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class FlightControlTower:
    def __init__(self):
        self._flights: List[Flight] = []
        self._observers: List[Observer] = []
    
    def register_flight(self, flight: "Flight"):
        self._flights.append(flight)
    
    def register_observer(self, observer: Observer):
        self._observers.append(observer)
    
    def notify_observers(self, message: str):
        for observer in self._observers:
            observer.update(message)
    
    def update_flight_status(self, flight_number: str, status: str):
        for flight in self._flights:
            if flight.flight_number == flight_number:
                flight.status = status
                self.notify_observers(f"Flight {flight_number} status updated to {status}")
                return # Exit the loop after updating the flight
            print(f"Flight {flight_number} not found.")
            raise ValueError(f"Flight {flight_number} not found.")

class Flight:
    def __init__(self, flight_number: str, airline: str, aircraft_registration: str, origin_airport: str, status: str = "Scheduled"):
        self.flight_number = flight_number
        self.airline = airline
        self.aircraft_registration = aircraft_registration
        self.origin_airport = origin_airport
        self.status = status

    def __str__(self):
        return f"Flight {self.flight_number} ({self.airline}) - {self.status} | Aircraft: {self.aircraft_registration} | Origin: {self.origin_airport}"

class FlightObserver(Observer):
    def update(self, message: str):
        print(f"[NOTIFICATION] {message}")

# Example usage
def main():
    tower = FlightControlTower()
    observer = FlightObserver()
    tower.register_observer(observer)
    
    flight1 = Flight("AB123", "AirBlue", "ABC-987", "JFK")
    flight2 = Flight("CD456", "SkyJet", "XYZ-123", "LAX")
    
    tower.register_flight(flight1)
    tower.register_flight(flight2)
    
    print(flight1)
    print(flight2)
    
    tower.update_flight_status("AB123", "Boarding")
    tower.update_flight_status("CD456", "Departed")

if __name__ == "__main__":
    main()
