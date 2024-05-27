#Task 1:


class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def save_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.name},{self.floors}\n")

    @staticmethod
    def load_from_file(filename):
        buildings = []
        with open(filename, 'r') as file:
            for line in file:
                name, floors = line.strip().split(',')
                buildings.append(Building(name, int(floors)))
        return buildings

# Demonstration
if __name__ == "__main__":
    # Create building instances
    building1 = Building("Empire State Building", 102)
    building2 = Building("Burj Khalifa", 163)
    building3 = Building("Shanghai Tower", 128)

    # Save buildings to file
    building1.save_to_file("buildings.txt")
    building2.save_to_file("buildings.txt")
    building3.save_to_file("buildings.txt")

    # Load buildings from file
    loaded_buildings = Building.load_from_file("buildings.txt")

    # Display loaded buildings
    print("Loaded Buildings:")
    for building in loaded_buildings:
        print(f"Name: {building.name}, Floors: {building.floors}")
