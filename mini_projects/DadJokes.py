import requests
import pyfiglet
from random import choice
from termcolor import colored
final_message = pyfiglet.figlet_format("Dad Joke 3000")
final_message_colored = colored(final_message, color="green")
print(final_message_colored)

user_input = input("Let me tell you a joke... what word do you want me to use? ")

#numerical_user_input = input("how many results do you want? ")


url = "https://icanhazdadjoke.com/search"
response = requests.get(
	url, 
	headers = {"Accept": "application/json"},
	params = {
		"term": user_input,
		#"limit": numerical_user_input
	}
)


data = response.json()
final_data = data["results"]


if len(final_data) > 0:
	print(f"Ive got {len(final_data)} jokes about {user_input}... here's one.")
	joke = choice(final_data)["joke"]
	print(joke)
else:
	print("i dont have any jokes for that...")
#print(final_data)
#print(data["results"])
#valuera = random.choice(final_data.values())
#print(valuera)