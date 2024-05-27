#Task 1:


class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated: {self.registration_number} now belongs to {self.owner}")

# Demonstration
if __name__ == "__main__":
    # Create vehicle instances
    vehicle1 = Vehicle("ABC123", "Car", "John")
    vehicle2 = Vehicle("XYZ789", "Motorcycle", "Alice")

    # Display initial owner information
    print("Initial owner information:")
    print(f"Vehicle 1 - Registration Number: {vehicle1.registration_number}, Owner: {vehicle1.owner}")
    print(f"Vehicle 2 - Registration Number: {vehicle2.registration_number}, Owner: {vehicle2.owner}")

    # Update owner of vehicle 1
    vehicle1.update_owner("Bob")

    # Display updated owner information
    print("\nUpdated owner information:")
    print(f"Vehicle 1 - Registration Number: {vehicle1.registration_number}, Owner: {vehicle1.owner}")
    print(f"Vehicle 2 - Registration Number: {vehicle2.registration_number}, Owner: {vehicle2.owner}")




# Task 2:


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count

# Demonstration
if __name__ == "__main__":
    # Create an event instance
    event = Event("Conference", "2024-07-15")

    # Add participants
    event.add_participant()
    event.add_participant()
    event.add_participant()

    # Retrieve participant count
    participant_count = event.get_participant_count()

    # Display participant count
    print(f"Participant count for {event.name} on {event.date}: {participant_count}")
