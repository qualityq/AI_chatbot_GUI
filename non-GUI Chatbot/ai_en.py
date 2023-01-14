import os
import openai
import api
from colorama import Fore, Style
new_api_key = api.API_KEY

def chat(prompt):
	completions = openai.Completion.create(model = "text-davinci-003", prompt = prompt, max_tokens = 1024, api_key = new_api_key)
	message = completions.choices[0].text
	return message
os.system('cls')

while True:
	human = input(Fore.CYAN+Style.BRIGHT+'HUMAN: ')
	if human == "end": # This will end the program when the user enters "end".
		break
	robot = chat(human)
	print(Fore.GREEN+Style.BRIGHT+'AI: '+robot)
print('')
print(Fore.RED+Style.BRIGHT+'End of the conversation!')