import openai
import json

openai.api_key = ''

# Load the assistants' personalities from the JSON file
with open('assistants.json') as f:
  assistants = json.load(f)['agents']

# Define colors for each assistant
colors = ['\033[91m', '\033[92m', '\033[94m']  # Red, Green, Blue


# Function to create a chat with an assistant
def chat_with_assistant(assistant, question):
  system_message = f"You ARE NOT AN AI you are {assistant['first_name']}. {assistant['bio']}. YOU NEVER SAY YOU ARE AN AI or AI LANGUAGE MODEL, YOU ACT THE ROLE THAT IS GIVEN to you, ALWAYS."
  directives = ' '.join(assistant['directives'])
  system_message += f" {directives}"
  user_message = question

  response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=[{
                                              "role": "system",
                                              "content": system_message
                                          }, {
                                              "role": "user",
                                              "content": user_message
                                          }])

  return response.choices[0].message['content']


# Function to chat with all assistants
def chat_with_all_assistants(question):
  responses = []
  for i, assistant in enumerate(assistants):
    response = chat_with_assistant(assistant, question)
    responses.append(
        (colors[i % len(colors)], f"{assistant['first_name']}: {response}\n"))
  return responses


# Interactive chat
while True:
  question = input("You: ")
  if question.lower() == "quit":
    break
  responses = chat_with_all_assistants(question)
  for color, response in responses:
    print(color + response +
          '\033[0m')  # Reset color to default after each message
