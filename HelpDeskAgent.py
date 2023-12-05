import openai

class HelpDeskAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def handle_user_query(self, vehicle_id, user_query):
        """
        Handles user queries and provides relevant information using the Large Language Model.
        """
        prompt = f"Handle user query for Vehicle {vehicle_id}: {user_query}."
        response = openai.ChatCompletion.create(model="gpt-4",
                                                messages=[{'role': 'assistant', 'content': prompt}],
                                                max_tokens=2000)
        query_response = response["choices"][0]["message"]["content"]
        print(f"Received Response - {query_response.strip()}")

