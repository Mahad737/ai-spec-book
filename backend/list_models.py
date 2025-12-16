from google.genai import Client

# Use your API key
client = Client(api_key="AIzaSyBteKtLt-G5_EyIH7pQ4xrWR99_YmeyqYk")

# List all models available for your key
for m in client.models.list():
    print(m.name, m.supported_actions)
