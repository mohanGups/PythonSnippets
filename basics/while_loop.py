"""While Loop"""

# A while loop repeats a block of code as long as a certain
# condition is true.
# A simple while loop
current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1

# Letting the user choose when to quit
message = ''
while message != 'quit':
    message = input("What's your message? ")
    if message != 'quit':
        print(message)

# Using a flag
prompt = "\nTell me something, and I'll "
prompt += "repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Using break to exit a loop
prompt = "\nWhat cities have you visited?"
prompt += "\nEnter 'quit' when you're done. "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I've been to " + city + "!")

# Using continue in a loop
banned_users = ['eve', 'fred', 'gary', 'helen']

prompt = "\nAdd a player to your team."
prompt += "\nEnter 'quit' when you're done. "

players = []
while True:
    player = input(prompt)
    if player == 'quit':
        break
    elif player in banned_users:
        print(player + " is banned!")
        continue
    else:
        players.append(player)

print("\nYour team:")
for player in players:
    print(player)

# An infinite loop
isTrue = False
while isTrue:
    name = input("\nWho are you? ")
    print("Nice to meet you, " + name + "!")

# Example
# Removing all cats from a list of pets
pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
