from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

with model.chat_session():    
    model.generate(prompt='give me JSON of array of 5 fruits', temp=0)    
    print(model.current_chat_session)
