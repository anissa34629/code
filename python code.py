!pip install openai
!pip install openai==0.28
# Import necessary libraries
import os
import openai

# Set up your OpenAI API key
os.environ['OPENAI_API_KEY'] = 'sk-proj-EbCtju6bMikvDkw20GG9T3BlbkFJZB4hYcOSOAQOZ8RyY4LC'  # Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Store conversation history to maintain context
conversation_history = []

# Function to set the initial context for the chatbot
def initialize_chat():
    # Set the initial context to orient the chatbot
    conversation_history.append({"role": "system", "content": "You are a helpful assistant knowledgeable in organizational change management."})

# Function to send prompts to ChatGPT and receive responses using the updated API for newer versions
def ask_chatgpt(prompt):
    conversation_history.append({"role": "user", "content": prompt})
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",  # Specify the model you are using, for example, "gpt-4"
            messages=conversation_history
        )
        answer = response.choices[0].message['content']
        conversation_history.append({"role": "system", "content": answer})
        return answer
    except Exception as e:
        return f"An error occurred: {str(e)}"  # Enhanced error handling with user-friendly message

# Function to interactively test the chatbot
def test_chatbot():
    print("Chatbot initialized. Type 'exit' to stop.")
    initialize_chat()  # Initialize chat with the set context before starting
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting chatbot.")
            break
        response = ask_chatgpt(user_input)
        print("ChatGPT:", response)

# Call the test function to start interacting with the chatbot
test_chatbot()