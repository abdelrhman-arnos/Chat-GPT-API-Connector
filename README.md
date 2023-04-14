# Chat-GPT API Connector
This Python application is designed to connect to the Chat-GPT API and generate responses to user input. It uses the OpenAI GPT-3.5 architecture to generate responses, making it an ideal tool for conversational AI applications.

## Installation
To install this application, follow these steps:

1. Clone the repository to your local machine
2. Install the required Python packages using pip: `pip install -r requirements.txt`
3. Set up your API credentials by following the instructions in the `config.py` file
4. Run the application by executing python `chat_gpt.py`

## Usage
Before you run this script, you'll need to set up an OpenAI API key by following the instructions here: https://beta.openai.com/docs/api-reference/authentication. Once you have an API key, you can store it as an environment variable named OPENAI_API_KEY.

To run the script, navigate to the directory containing the script in your terminal and enter the following command:
```
python chat_gpt_api.py
```
The script will send the prompt "Hello, how are you?" to the Chat-GPT API using the text-davinci-002 model. The temperature parameter controls the "creativity" of the response, and the max_tokens parameter determines the maximum length of the response. The script prints the generated response to the console.

Of course, you can modify the script to prompt the user for input, use a different model, or generate more than one response.

## Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Before doing so, please review the contributing guidelines for this project.

## License
This project is licensed under the [MIT License](https://raw.githubusercontent.com/abdelrhman-arnos/Chat-GPT-API-Connector/main/LICENSE).
