import openai

class CentralizedControlAgent:
    def __init__(self, fleet, api_key):
        self.fleet = fleet
        self.api_key = api_key
        openai.api_key = self.api_key

    def plan_route_for_vehicle(self, vehicle, current_location, destination, preferences):
        """
        Plans a route for a specific vehicle based on the destination and user preferences.
        """
        prompt = f"Generate a route for vehicle {vehicle.vehicle_id} from {current_location} to {destination} with preferences: {preferences}."
        response = openai.ChatCompletion.create(model="gpt-4",
                                                messages=[{'role': 'assistant', 'content': prompt}],
                                                max_tokens=3000)
        route_plan = response["choices"][0]["message"]["content"]
        vehicle.route = route_plan.strip()
        print(f"Vehicle {vehicle.vehicle_id}: Route planned - {route_plan}")

    def allocate_resources(self):
        """
        Allocates resources (such as charging stations) to vehicles based on their planned routes.
        """
        for vehicle in self.fleet:
            if vehicle.route is not None:
                resource_allocation = self.allocate_resources_for_vehicle(vehicle)
                print(f"Vehicle {vehicle.vehicle_id}: Resources allocated - {resource_allocation}")

    def allocate_resources_for_vehicle(self, vehicle):
        """
        Allocates resources for a specific vehicle based on its planned route.
        """
        prompt = f"Allocate resources for vehicle {vehicle.vehicle_id} with route: {vehicle.route}."
        response = openai.ChatCompletion.create(model="gpt-4",
                                                messages=[{'role': 'system', 'content': prompt}],
                                                max_tokens=1500)
        resource_allocation = response["choices"][0]["message"]["content"]
        return resource_allocation.strip()


    def allocate_resources_for_vehicle(self, vehicle):
        """
        Allocates resources for a specific vehicle based on its planned route.
        """
        prompt = f"Allocate resources for vehicle {vehicle.vehicle_id} with route: {vehicle.route}."
        response = openai.ChatCompletion.create(model="gpt-4",
                                                messages=[{'role': 'assistant', 'content': prompt}],
                                                max_tokens=1500)
        resource_allocation = response["choices"][0]["message"]["content"]
        return resource_allocation.strip()
