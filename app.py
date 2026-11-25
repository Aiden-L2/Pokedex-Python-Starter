import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
move_file = open("./moves.json", encoding="utf8")
moves = json.load(move_file)
#print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

def list(z):

    while True:
        user_input = input("Enter the pokemon you were looking for: ").strip()
        
        if user_input == 0:
            print("try again")
        else:
            matches = [item for item in z if item.lower() == user_input.lower()]
            if matches:
                return matches[0]
            else:
                print("Invalid. Try again.")



def pokemon():
    global language

    print("Which lanuage will you choose?")
    print("Lanuage: 1. English 2. Chinese 3. Japanese 4. French")
    choice = input("enter your choice: ").strip()

    language = {
        "1": "english",
        "2": "chinese",
        "3": "japanese",
        "4": "french"
    }

    language = language.get(choice, "English")

    print(f"You chose {language}.")

    for item in data:
        pokemon=item["name"]
        print(pokemon[language])
    
pokemon()

    
def find():
    global finding
    global matches

    matches = []

    finding = input("what pokemon are you looking for: ")



    for i in range(len(data)):
        if finding.capitalize() in data[i]["type"]:
            matches.append(data[i]["name"][language])




find()

def tp():
    global choice
    global finding

    for pokemon in data:
        if not isinstance(pokemon, dict):
            continue
        names = pokemon.get("name", {})

        if language == "english":
            name = names.get("english", "")
        elif language == "chinese":
            name = names.get("chinese", "")
        elif language == "japanese":
            name = names.get("japanese", "")
        elif language == "french":
            name = names.get("french", "")
        else:
            continue


        if name.lower().startswith(finding.lower()):
            matches.append(name)

    if matches:
        print("matches found")
        for name in matches:
            print(name)
        choice = list(matches)
        print(f"Pokemon choosen: {choice}")


    else:
        print(f"no pkemon found matching '{finding}'.")
        print("restart")
tp()

def mov():

    for penguin in range(len(data)):

        if choice in data[penguin]["name"][language]:
            type = data[penguin]["type"]           

            for s in type:

                for penguin in range(len(moves)):

                    if s == moves[penguin]["type"]:
                        
                        print(moves[penguin]["ename"])
mov()
          



