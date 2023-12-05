import openai

class UserAgent:
    def __init__(self, user_id, api_key):
        self.user_id = user_id
        self.user_query = None
        self.api_key = api_key
        openai.api_key = self.api_key

    def request_ride(self, current_location, destination):
        prompt = f"Generate a route plan for User {self.user_id} from {current_location} to {destination}."
        response = openai.ChatCompletion.create(model="gpt-4",
                                                messages=[{'role': 'assistant', 'content': prompt}],
                                                max_tokens=2000)
        route_plan = response["choices"][0]["message"]["content"]
        print(f"User {self.user_id}: Received route plan - {route_plan}")

    def ask_question(self, question):
        self.user_query = question
        prompt = f"User {self.user_id}: Asked a question - {self.user_query}"
        response = openai.ChatCompletion.create(model="gpt-4",
                                                messages=[{'role': 'assistant', 'content': prompt}],
                                                max_tokens=2000)
        answer = response["choices"][0]["message"]["content"]
        print(f"Received AI Assistant Reply - {answer}")
