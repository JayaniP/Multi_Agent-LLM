import openai

class CommunicationAgent:
    def __init__(self, vehicle, api_key):
        self.vehicle = vehicle
        self.neighbor_vehicles = []  # List of neighboring vehicles
        self.api_key = api_key
        openai.api_key = self.api_key

    def update_neighbors(self, neighboring_vehicles):
        """
        Updates the list of neighboring vehicles for communication.
        Neighboring vehicles are those within the communication range of the current vehicle.
        """
        self.neighbor_vehicles = neighboring_vehicles
        print(f"Vehicle {self.vehicle.vehicle_id}: Neighbors updated - {self.neighbor_vehicles}")

    def share_traffic_info(self):
        """
        Shares traffic information with neighboring vehicles.
        """
        for neighbor_vehicle in self.neighbor_vehicles:
            traffic_info = self.generate_traffic_info()
            print(f"Vehicle {self.vehicle.vehicle_id}: Sharing traffic info with Vehicle {neighbor_vehicle.vehicle_id} - {traffic_info}")

    def receive_traffic_info(self, traffic_info):
        """
        Receives traffic information from neighboring vehicles.
        This information can be used for local navigation and route planning.
        """
        print(f"Vehicle {self.vehicle.vehicle_id}: Received traffic info - {traffic_info}")

    def generate_traffic_info(self):
        """
        Generates traffic information using the Large Language Model.
        """
        prompt = f"Generate traffic information for Vehicle {self.vehicle.vehicle_id}."
        response = openai.ChatCompletion.create(model="gpt-4",
                                                messages=[{'role': 'assistant', 'content': prompt}],
                                                max_tokens=3000)
        traffic_info = response["choices"][0]["message"]["content"]
        return traffic_info.strip()