import openai

class MaintenanceAgent:
    def __init__(self, vehicle, api_key):
        self.vehicle = vehicle
        self.api_key = api_key
        openai.api_key = self.api_key

    def monitor_vehicle_health(self):
        health_report = self.generate_health_report()
        print(f"Vehicle {self.vehicle.vehicle_id}: Health report - {health_report}")
        if "critical" in health_report.lower():
            self.schedule_maintenance()

    def generate_health_report(self):
        prompt = f"Generate a health report for vehicle {self.vehicle.vehicle_id}."
        response = openai.ChatCompletion.create(model="gpt-4",
                                                messages=[{'role': 'assistant', 'content': prompt}],
                                                max_tokens=2000)
        health_report = response["choices"][0]["message"]["content"]
        return health_report.strip()

    def schedule_maintenance(self):
        maintenance_plan = self.generate_maintenance_plan()
        print(f"Vehicle {self.vehicle.vehicle_id}: Scheduling maintenance - {maintenance_plan}")

    def generate_maintenance_plan(self):
        prompt = f"Generate a maintenance plan for vehicle {self.vehicle.vehicle_id}."
        response = openai.ChatCompletion.create(model="gpt-4",
                                                messages=[{'role': 'assistant', 'content': prompt}],
                                                max_tokens=2000)
        maintenance_plan = response["choices"][0]["message"]["content"]
        return maintenance_plan.strip()