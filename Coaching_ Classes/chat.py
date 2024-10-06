import openai

# Set your API key here
# openai.api_key = "sk-6mAFM4nFbOfihnsx-AgLQ3UeELxVYLvzwTE3kHQGfBT3BlbkFJ-ajrtuS1ylq3iBB2XJJ0J1dUjoNBZoicAsrTvB7fEA" 

messages = [{'role': 'system', 'content': "For assistant"}]

while True:
    query = input("User: ")

    # Prepare prompt for text-davinci model
    prompt = "\n".join([message['content'] for message in messages if message['role'] == 'user'])

    # Generate response using text-davinci-003
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,  # You can adjust the number of tokens based on your needs
        temperature=0.7  # You can adjust the temperature for more creative or deterministic responses
    )

    # Extract the assistant's reply from the response
    reply = response['choices'][0]['text'].strip()

    # Print the assistant's reply
    print(f"ChatGPT: {reply}")

    # Add the user's query and assistant's reply to the conversation
    messages.append({"role": "user", "content": query})
    messages.append({"role": "assistant", "content": reply})
