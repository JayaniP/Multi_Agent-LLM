import openai

class ChargingStation:
    def __init__(self, station_id):
        self.station_id = station_id
        self.available = True  # Assume all stations are initially available

    def is_available(self):
        return self.available

class EnergyManagementAgent:
    def __init__(self, vehicle, charging_stations, api_key):
        self.vehicle = vehicle
        self.charging_stations = charging_stations
        self.api_key = api_key
        openai.api_key = self.api_key

    def optimize_charging_schedule(self):
        """
        Optimizes the charging schedule for the vehicle based on energy needs and charging station availability.
        """
        energy_needs = self.estimate_energy_needs()
        available_charging_stations = self.find_available_charging_stations()

        if not available_charging_stations:
            print(f"Vehicle {self.vehicle.vehicle_id}: No available charging stations. Cannot optimize charging schedule.")
            return

        best_charging_station = self.find_best_charging_station(available_charging_stations)
        charging_schedule = self.generate_charging_schedule(energy_needs, best_charging_station)
        print(f"Vehicle {self.vehicle.vehicle_id}: Optimized charging schedule - {charging_schedule}")

    def estimate_energy_needs(self):
        """
        Estimates the energy needs of the vehicle based on the planned route and user preferences.
        """
        prompt = f"Estimate energy needs for Vehicle {self.vehicle.vehicle_id} based on planned route and user preferences."
        response = openai.ChatCompletion.create(model="gpt-4",
                                                messages=[{'role': 'assistant', 'content': prompt}],
                                                max_tokens=2500)
        energy_needs = response["choices"][0]["message"]["content"]
        return energy_needs.strip()

    def find_available_charging_stations(self):
        """
        Finds available charging stations within the vehicle's range.
        """
        available_charging_stations = [station for station in self.charging_stations if station.is_available()]
        return available_charging_stations

    def find_best_charging_station(self, available_charging_stations):
        """
        Finds the best charging station based on factors such as proximity and charging speed.
        """
        # assume the first available charging station is the best
        best_charging_station = available_charging_stations[0]
        return best_charging_station

    def generate_charging_schedule(self, energy_needs, charging_station):
        """
        Generates a charging schedule based on energy needs and charging station characteristics.
        """
        prompt = f"Generate charging schedule for Vehicle {self.vehicle.vehicle_id} with energy needs: {energy_needs} at Charging Station {charging_station.station_id}."
        response = openai.ChatCompletion.create(model="gpt-4",
                                                messages=[{'role': 'assistant', 'content': prompt}],
                                                max_tokens=2500)
        charging_schedule = response["choices"][0]["message"]["content"]
        return charging_schedule.strip()