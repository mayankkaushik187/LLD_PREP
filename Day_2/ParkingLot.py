"""
A parking lot consists of Vehicle, ParkingSpot, Ticket, ParkingLot

Vehicle can have multiple  types it could be Either a Bike or a Car or a Truck.

Essentially indicating three types of vehicles (heavy, light and medium)

Parking Spot will give us three things type of spot so it can accomodate diff types of vehicles like a parking spot can have either vacancy for a bike or a car or a truck
So we get the size of the parking spot, we need to know whether this spot is taken or not. 


Parking ticket will have an exit time and an entry time and it will have the vehicle number plate and the ticket id.


Methods for each entity

Parking lot can issue a ticket, it can add a parkingSpot, release a ticket, also it should tell me which spots are empty right now.

ParkingTicket should have close the ticket and display essentials like entry, exit time and the vehicle id and the ticket id.

ParkingSpot should be able to tell us the availability, the type of vehicle we can park there and we can occupy a spot and vacate a spot when we issue or release a ticket.

Vehicles should have a number plate and the type of that vehicle.

"""

from abc import ABC, abstractmethod
import time

class Vehicle(ABC):
    def __init__(self, number_plate: str):
        self.number_plate = number_plate

    @abstractmethod
    def get_type(self) -> str:
        pass
    

#Creating concrete classes for the different types of vehicles.
class Car(Vehicle):
    def get_type(self) -> str:
        return "Car"
    
class Bike(Vehicle):
    def get_type(self) -> str:
        return "Bike"

class Truck(Vehicle):
    def get_type(self) -> str:
        return "Truck"
    
#Create the ParkingSpot Abstract class.

class ParkingSpot(ABC):
    def __init__(self, spot_id: int):
        self.spot_id = spot_id
        self.occupied = False

    @abstractmethod
    def get_spot_type(self) -> str:
        pass

    def is_available(self) -> bool:
        return not self.occupied
    
    def vacate(self):
        self.occupied = False

    def occupy(self):
        self.occupied = True

#Create concrete classes for different Parking Spots.

class SmallSpot(ParkingSpot):
    def get_spot_type(self) -> str:
        return "Small"
    
class MediumSpot(ParkingSpot):
    def get_spot_type(self) -> str:
        return "Medium"
    
class BigSpot(ParkingSpot):
    def get_spot_type(self) -> str:
        return "Big"
    

#Create the Parking Ticket Class

class ParkingTicket:
    def __init__(self, vehicle: Vehicle, spot_id: int, ticket_id: int):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot_id = spot_id
        self.entry_time = time.time()
        self.exit_time = None
    
    def close_ticket(self):
        self.exit_time = time.time()

    def __str__(self):
        entry_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.entry_time))
        exit_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.exit_time))

        return f"Ticket Id: {self.ticket_id}, Vehicle: {self.vehicle.number_plate}, Spot: {self.spot_id} " \
              f"Entry Time: {entry_time_str}, Exit Time: {exit_time_str}"
    

class ParkingLot: 
    def __init__(self):
        self.spots = {}
        self.vehicle_ticket_map = {}
        self.tickets = {}
        self.ticket_counter = 1

    def add_parking_spot(self, spot: ParkingSpot, spot_id: int):
        self.spots[spot_id] = spot

    def issue_ticket(self, vehicle: Vehicle) -> bool:
        for spot_id, spot in self.spots.items():
            if spot.is_available():
                spot.occupy()
                ticket = ParkingTicket(vehicle, spot_id, self.ticket_counter)
                self.tickets[self.ticket_counter] = ticket
                self.vehicle_ticket_map[vehicle.number_plate] = self.ticket_counter
                print (f"Ticket Issued: {ticket}")
                self.ticket_counter += 1
                return True
        print("No spots available")
        return False
    
    def release_ticket(self, number_plate: str) -> bool:
        if number_plate not in self.vehicle_ticket_map:
            print(f"Vehicle {number_plate} not found")
            return False
        ticket_id = self.vehicle_ticket_map[number_plate]
        self.vehicle_ticket_map.pop(number_plate)
        ticket = self.tickets[ticket_id]
        ticket.close_ticket()
        self.spots[ticket.spot_id].vacate()
        print(f"Released ticket: {ticket}")
        return True
    
    def get_available_spots(self):
        available_spots = [f"#{spot_id} ({spot.get_spot_type()})"for spot_id, spot in self.spots.items() if spot.is_available()]
        print (f"Available parking spots are : {' '.join(available_spots)}")


if __name__ == "__main__":
    parking_lot = ParkingLot()
    parking_lot.add_parking_spot(SmallSpot(1), 1)
    parking_lot.add_parking_spot(MediumSpot(2), 2)
    parking_lot.add_parking_spot(BigSpot(3), 3)

    car = Car("HSADH")
    bike = Bike("AsdDSA")
    truck = Truck("sdrfs")

    parking_lot.get_available_spots()

    parking_lot.issue_ticket(car)
    parking_lot.issue_ticket(bike)
    parking_lot.issue_ticket(truck)

    parking_lot.get_available_spots()

    parking_lot.release_ticket(car.number_plate)

    parking_lot.release_ticket(truck.number_plate)
    parking_lot.get_available_spots()