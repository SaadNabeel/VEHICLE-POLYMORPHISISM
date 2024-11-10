
class BMW:
    def start(self):
        print("BMW car starting")

    def speed(self):
        print("BMW speed is 240 km/h.")

    def fuel_type(self):
        print("BMW runs on petrol.")


class Ferrari:
    def start(self):
        print("Ferrari car starting")

    def speed(self):
        print("Ferrari speed is 300 km/h.")

    def fuel_type(self):
        print("Ferrari runs on high-octane petrol.")


def vehicle_info(vehicle):
    vehicle.start()
    vehicle.speed()
    vehicle.fuel_type()


bmw_car = BMW()
ferrari_car = Ferrari()


for car in (bmw_car, ferrari_car):
    vehicle_info(car)
