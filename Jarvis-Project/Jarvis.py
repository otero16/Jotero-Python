import openai

# Set your OpenAI API key here
api_key = ''

# Initialize the OpenAI API client
openai.api_key = api_key

def ask_jarvis(question):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",  # You can use GPT-3 or GPT-4 if available
            prompt=f"Hey Jarvis, {question}",
            max_tokens=200  # Adjust the response length as needed
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Introduction and context setting
print("Welcome to your virtual assistant. I am Jarvis, your AI assistant designed to imitate the responses and style of the AI from the first Iron Man movie.")
print("I'm here to assist you, Mr. Stark. Feel free to ask me any questions or request assistance. Type 'exit' to quit.")

# Main loop
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = ask_jarvis(user_input)
        print(f"Jarvis: {response}")

#this was the first attemtp i got it working in plain text quite well. 
