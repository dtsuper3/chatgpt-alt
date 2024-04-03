
from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

def generateText():    
    return model.generate(prompt='give me JSON array of 5 number', temp=0)    
        
