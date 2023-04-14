import openai
import os

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up prompt and parameters
prompt = "Hello, how are you?"
model = "text-davinci-002"
temperature = 0.5
max_tokens = 100

# Generate response using OpenAI API
response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens
)

# Print response
print(response.choices[0].text)
