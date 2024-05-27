#Task 1:


class Bus:
    # Class variables
    city_name = "YourCity"
    base_fare = 2.50

    def __init__(self, route_number, passenger_capacity):
        # Instance variables
        self.route_number = route_number
        self.passenger_capacity = passenger_capacity

    def display_info(self):
        print(f"City: {Bus.city_name}")
        print(f"Base Fare: ${Bus.base_fare}")
        print(f"Route Number: {self.route_number}")
        print(f"Passenger Capacity: {self.passenger_capacity}")


if __name__ == "__main__":
    
    # Create bus instances
    bus1 = Bus("101", 50)
    bus2 = Bus("102", 45)

    # Display class variables
    print("Class Variables:")
    print(f"City Name: {Bus.city_name}")
    print(f"Base Fare: ${Bus.base_fare}")

    # Display instance attributes
    print("\nBus 1 Attributes:")
    bus1.display_info()
    print("\nBus 2 Attributes:")
    bus2.display_info()
