class TransportSystem:
    class Vehicle:
        def __init__(self, number, type, seats):
            self.number = number
            self.type = type
            self.seats = seats

    class Route:
        def __init__(self, name, stops, travel_times):
            self.name = name
            self.stops = stops
            self.travel_times = travel_times

    def __init__(self):
        self.vehicles = []
        self.routes = []

    def add_vehicle(self, number, type, seats):
        vehicle = self.Vehicle(number, type, seats)
        self.vehicles.append(vehicle)

    def add_route(self, name, stops, travel_times):
        route = self.Route(name, stops, travel_times)
        self.routes.append(route)

    def find_vehicle_by_number(self, number):
        for vehicle in self.vehicles:
            if vehicle.number == number:
                return vehicle
        return None

    def find_route_by_name(self, name):
        for route in self.routes:
            if route.name == name:
                return route
        return None



ts = TransportSystem()
ts.add_vehicle('AB 7777 AH', 'Car', 5)
ts.add_route('Kyiv-Vinitsa', ['Lviv', 'Ternopil', 'Yaremche'], [10, 15])

vehicle = ts.find_vehicle_by_number('AB 7777 AH')
if vehicle is not None:
    print(f'Nice, vehicle: {vehicle.number}')
else:
    print(f'Not found vehicle')


route = ts.find_route_by_name('Kyiv-Vinitsa')
if route is not None:
    print(f'Nice, route: {route.name}')
else:
    print(f'Not found route')
