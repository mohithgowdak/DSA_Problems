class Vehicle:
    RESERVE_FUEL = 5

    def __init__(self, mileage, fuel_left):
        self.mileage = mileage
        self.fuel_left = fuel_left

    def identify_distance_that_can_be_travelled(self):
        usable_fuel = self.fuel_left - Vehicle.RESERVE_FUEL
        if usable_fuel <= 0:
            return 0
        return usable_fuel * self.mileage

    def identify_distance_travelled(self, initial_fuel):
        fuel_used = initial_fuel - self.fuel_left
        return fuel_used * self.mileage

vehicle = Vehicle(mileage=15, fuel_left=20)
print("Distance that can be travelled:", vehicle.identify_distance_that_can_be_travelled(), "kms")
initial_fuel = 30
print("Distance travelled:", vehicle.identify_distance_travelled(initial_fuel), "kms")
print(vehicle)