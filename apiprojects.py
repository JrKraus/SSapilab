import requests
#menu https://chatgpt.com/share/588e2342-232a-4620-b296-729c72fce4f3

def main_menu():
    print("Welcome to the Main Menu Of the DND")
    print("1. look up all avaible monters ")
    print("2. look up details about spells")
    print("3. look up equiment in our equipment catalog ")
    print("4. look up detials about classes in our class compendium ")
    print("5. look up traits for races")
    print("6. Exit")

def option_1():
    url = "https://www.dnd5eapi.co/api/monsters"
    headers = {'Accept': 'application/json'}
    
    try:
        response = requests.get(url, headers=headers)
        
        badguys = response.json()
        monsters = badguys['results']

        print("Welcome to the monster handbook")

        while True:
            lookup = input("Please enter a monster you would like to know about or enter Q to go back: ").lower()
            if lookup == 'q':
                print("Returning to main menu.")
                break
            if not lookup.replace(" ", "").isalpha():
                print("Invalid input. Please enter only alphabetic characters.")
                continue

            found = False
            for monster in monsters:
                if lookup in monster["name"].lower():
                    monster_url = f"https://www.dnd5eapi.co{monster['url']}"
                    monster_response = requests.get(monster_url, headers=headers)
                    monster_response.raise_for_status()
                    monster_data = monster_response.json()

                    print(f"\nDetails for {monster_data['name']}:")
                    print(f"Type: {monster_data['type']}")
                    print(f"Size: {monster_data['size']}")
                    print(f"Alignment: {monster_data['alignment']}")
                    print(f"Armor Class: {monster_data['armor_class']}")
                    print(f"Hit Points: {monster_data['hit_points']} ({monster_data['hit_dice']})")
                    
                    found = True
                    break

            if not found:
                print("Monster not found. Please try again.")

   
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
    except KeyError as e:
        print(f"Error: Missing expected data field: {e}")
        
    
def option_2():
    url = "https://www.dnd5eapi.co/api/spells"
    headers = {'Accept': 'application/json'}
    
    try:
        response = requests.get(url, headers=headers)
      
        spellbook = response.json()
        spells = spellbook['results']

        print("Welcome to the spellbook")

        while True:
            lookup = input("Please enter a spell you would like to know about or enter Q to go back: ").lower()
            if lookup == 'q':
                print("Returning to main menu.")
                break
            if not lookup.replace(" ", "").isalpha():
                print("Invalid input. Please enter only alphabetic characters.")
                continue

            found = False
            for spell in spells:
                if lookup in spell["name"].lower():
                    spell_url = f"https://www.dnd5eapi.co{spell['url']}"
                    spell_response = requests.get(spell_url, headers=headers)
                   
                    spell_data = spell_response.json()

                    print(f"\nDetails for {spell_data['name']}:")
                    print(f"Level: {spell_data['level']}")
                    print(f"School: {spell_data['school']['name']}")
                    print(f"Casting Time: {spell_data['casting_time']}")
                    print(f"Range: {spell_data['range']}")
                    print(f"Components: {', '.join(spell_data['components'])}")
                    print(f"Duration: {spell_data['duration']}")
                    print("\nDescription:")
                    for desc in spell_data['desc']:
                        print(desc)
                    if 'higher_level' in spell_data:
                        print("\nAt Higher Levels:")
                        for higher in spell_data['higher_level']:
                            print(higher)
                    
                    found = True
                    break

            if not found:
                print("Spell not found. Please try again.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
    except KeyError as e:
        print(f"Error: Missing expected data field: {e}")
   

def option_3():
    url = "https://www.dnd5eapi.co/api/equipment"
    headers = {'Accept': 'application/json'}
    
    try:
        response = requests.get(url, headers=headers)
       
        equipment_list = response.json()
        items = equipment_list['results']

        print("Welcome to the equipment catalog")

        while True:
            lookup = input("Please enter an equipment item you would like to know about or enter Q to go back: ").lower()
            if lookup == 'q':
                print("Returning to main menu.")
                break
            if not lookup.replace(" ", "").isalpha():
                print("Invalid input. Please enter only alphabetic characters.")
                continue

            found = False
            for item in items:
                if lookup in item["name"].lower():
                    item_url = f"https://www.dnd5eapi.co{item['url']}"
                    item_response = requests.get(item_url, headers=headers)
                    item_data = item_response.json()

                    print(f"\nDetails for {item_data['name']}:")
                    print(f"Equipment Category: {item_data['equipment_category']['name']}")
                    if 'weapon_category' in item_data:
                        print(f"Weapon Category: {item_data['weapon_category']}")
                    if 'weapon_range' in item_data:
                        print(f"Weapon Range: {item_data['weapon_range']}")
                    if 'category_range' in item_data:
                        print(f"Category Range: {item_data['category_range']}")
                    print(f"Cost: {item_data['cost']['quantity']} {item_data['cost']['unit']}")
                    if 'damage' in item_data:
                        print(f"Damage: {item_data['damage']['damage_dice']} {item_data['damage']['damage_type']['name']}")
                    if 'range' in item_data:
                        print(f"Range: Normal - {item_data['range']['normal']}")
                        if 'long' in item_data['range']:
                            print(f"        Long - {item_data['range']['long']}")
                    print(f"Weight: {item_data['weight']} lbs")
                    if 'properties' in item_data:
                        properties = ", ".join([prop['name'] for prop in item_data['properties']])
                        print(f"Properties: {properties}")
                    
                    found = True
                    break

            if not found:
                print("Equipment item not found. Please try again.")

    
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
    except KeyError as e:
        print(f"Error: Missing expected data field: {e}")

def option_4():
    url = "https://www.dnd5eapi.co/api/classes"
    headers = {'Accept': 'application/json'}
    
    try:
        response = requests.get(url, headers=headers)
        class_list = response.json()
        classes = class_list['results']

        print("Welcome to the class compendium")

        while True:
            lookup = input("Please enter a class you would like to know about or enter Q to go back: ").lower()
            if lookup == 'q':
                print("Returning to main menu.")
                break
            if not lookup.replace(" ", "").isalpha():
                print("Invalid input. Please enter only alphabetic characters.")
                continue

            found = False
            for class_item in classes:
                if lookup in class_item["name"].lower():
                    class_url = f"https://www.dnd5eapi.co{class_item['url']}"
                    class_response = requests.get(class_url, headers=headers)
                    class_data = class_response.json()

                    print(f"\nDetails for {class_data['name']}:")
                    print(f"Hit Die: d{class_data['hit_die']}")
                    
                    print("\nProficiencies:")
                    for prof in class_data['proficiencies']:
                        print(f"- {prof['name']}")
                    
                    print("\nSaving Throws:")
                    for save in class_data['saving_throws']:
                        print(f"- {save['name']}")
                    
                    print("\nStarting Equipment:")
                    for equipment in class_data['starting_equipment']:
                        print(f"- {equipment['equipment']['name']} (Quantity: {equipment['quantity']})")
                    
                    print("\nSubclasses:")
                    for subclass in class_data['subclasses']:
                        print(f"- {subclass['name']}")

                   
                    
                    found = True
                    break

            if not found:
                print("Class not found. Please try again.")

    
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
    except KeyError as e:
        print(f"Error: Missing expected data field: {e}")
        
def option_5():
    url = "https://www.dnd5eapi.co/api/races"
    headers = {'Accept': 'application/json'}
    
    try:
        response = requests.get(url, headers=headers)
       
        race_list = response.json()
        races = race_list['results']

        print("Welcome to the race compendium")

        while True:
            lookup = input("Please enter a race you would like to know about or enter Q to go back: ").lower()
            if lookup == 'q':
                print("Returning to main menu.")
                break
            if not lookup.replace(" ", "").isalpha():
                print("Invalid input. Please enter only alphabetic characters.")
                continue

            found = False
            for race_item in races:
                if lookup in race_item["name"].lower():
                    race_url = f"https://www.dnd5eapi.co{race_item['url']}"
                    race_response = requests.get(race_url, headers=headers)
                    race_data = race_response.json()

                    print(f"\nDetails for {race_data['name']}:")
                    print(f"Speed: {race_data['speed']}")
                    print("\nAbility Bonuses:")
                    for bonus in race_data['ability_bonuses']:
                        print(f"- {bonus['ability_score']['name']}: +{bonus['bonus']}")
                    
                    print("\nStarting Proficiencies:")
                    for prof in race_data['starting_proficiencies']:
                        print(f"- {prof['name']}")
                    
                    if 'languages' in race_data:
                        print("\nLanguages:")
                        for lang in race_data['languages']:
                            print(f"- {lang['name']}")
                    
                    if 'traits' in race_data:
                        print("\nTraits:")
                        for trait in race_data['traits']:
                            print(f"- {trait['name']}")
                    
                    if 'subraces' in race_data and race_data['subraces']:
                        print("\nSubraces:")
                        for subrace in race_data['subraces']:
                            print(f"- {subrace['name']}")
                    
                    found = True
                    break

            if not found:
                print("Race not found. Please try again.")

    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
    except KeyError as e:
        print(f"Error: Missing expected data field: {e}")

def exit_menu():
    print("Exiting the menu. Goodbye!")
    exit()

def menu():
    while True:
        main_menu()
        choice = input("Please select an option (1-6): ")
        
        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()
        elif choice == "4":
            option_4()
        elif choice == "5":
            option_5()
        elif choice == "6":
            exit_menu()
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    menu()



