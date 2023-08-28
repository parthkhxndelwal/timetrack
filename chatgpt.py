def ChatGPT(message):
    import openai
    openai.api_key = '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'
    messages = [ {"role": "system", "content": 
              "You are an intelligent assistant."} ]
    try:
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages = messages
            )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return(f"{reply}")
        
    except: 
        print("Server Error \n Prompt: {message} \n Input Response Manually: ")

ChatGPT("Hi!")