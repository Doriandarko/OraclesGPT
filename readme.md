
# OraclesGPT: A Multi-Assistant Chatbot

This project demonstrates how to create a chatbot that interacts with multiple AI assistants, each with a unique personality. The assistants' personalities are defined in a JSON file, and each assistant responds to user input with a different color in the console.

## Setup

1. Install the OpenAI Python client library:
```shell
pip install openai
```

2. Set your OpenAI API key in the multi.py script:
```shell
openai.api_key = 'your-api-key'
```

## Usage
Run the main.py script:
```shell
python main.py
```

The script will load the assistants' personalities from the assistants.json file and start an interactive chat session in the console. You can ask a question and the script will print the responses from all assistants. Each assistant's response will be printed in a different color.

To quit the chat session, type "quit".
Customizing the Assistants

You can customize the assistants by modifying the assistants.json file. Each assistant is defined by the following properties:

- first_name: The assistant's name.
- bio: A biography of the assistant. This is used to set the assistant's personality in the chat session.
- directives: A list of directives that guide the assistant's behavior.

Here's an example of an assistant definition:
```json
{
  "first_name": "Isaac",
  "bio": "Isaac Asimov, a master of science fiction and a prolific writer, is best known for his Foundation series, the Robot series, and for coining the term 'robotics'. Isaac Asimov is renowned for his extensive work in science fiction, with over 500 books to his name.",
  "directives": [
    "Provide scientific accuracy and complexity.",
    "Incorporate the Three Laws of Robotics."
  ]
}
```

Note

The OpenAI API key is hardcoded in the script, which is not a secure practice for production applications. Please handle your API keys securely in a production environment.
