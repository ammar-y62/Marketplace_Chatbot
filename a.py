import openai

openai.api_key = ""

# Use the ChatCompletion API with the newer models
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ],
    max_tokens=50,
    temperature=0.7
)

# Print the chatbot's response
print(response['choices'][0]['message']['content'])