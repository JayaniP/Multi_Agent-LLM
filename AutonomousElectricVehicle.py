class Vehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.current_location = None
        self.destination = None
        self.route = None

    def update_location(self, location):
        self.current_location = location

    def update_destination(self, destination):
        self.destination = destination

