from dataclasses import dataclass
import random   

@dataclass
class Characters:
    char_type: str
    char_maxhp: int
    char_atk: int
    char_def: int
    char_ability: bool
    char_spd: int
    
class Enemies:
    enm_type: str
    enm_maxhp: int
    enm_atk: int
    enm_def: int
    # enm_ablilty: bool
    enm_spd: int

items = ["Sandwich", "Cloak", "Bomb"]
# player_score = 

def game_start():
    print("Greetings weary traveler, come rest by the fire and I will tell you a story.")
    choice = input("What would you like to hear?\n >New Story\n >Continue Story\n >Forget\n >Leave\n >").capitalize()
    if choice == "New" or choice == "New story" or choice == "New Story":
        return "New"
    elif choice == "Continue" or "C":
        character = input("Who's story should I continue?\n >Knight\n >Wizard\n >Archer\n >").capitalize()
        story = game_continue(character)   
        return story
    elif choice == "Leave":
        quit()

def game_continue(character):
    while True:
            if character == "Knight":
                try:
                    with open(f"Knight's-story.txt", 'r') as file:
                        story = file.read()
                        print(story)
                        return story
                except FileNotFoundError:
                    print("I have not told you a story about them.")
                    character = input("Who's story should I continue?\n >Knight\n >Wizard\n >Archer\n >").capitalize()
            elif character == "Wizard":
                try:
                    with open(f"Wizard's-story.txt", 'r') as file:
                        story = file.read()
                        print(story)
                        return story
                except FileNotFoundError:
                    print("I have not told you a story about them.")
                    character = input("Who's story should I continue?\n >Knight\n >Wizard\n >Archer\n >").capitalize()
            elif character == "Archer":
                try:
                    with open(f"Archer's-story.txt", 'r') as file:
                        story = file.read()
                        print(story)
                        return story
                except FileNotFoundError:
                    print("I have not told you a story about them.")
                    character = input("Who's story should I continue?\n >Knight\n >Wizard\n >Archer\n >").capitalize()
            else:
                print("I do not know who that is.")
                character = input("Who's story should I continue?\n >Knight\n >Wizard\n >Archer\n >").capitalize()


def character_validator():
    name = input("Who's story should I tell?\n >Knight\n >Wizard\n >Archer\n >").capitalize()
    while True:
        # try:
        #     with open(f"Knight's-Story.txt", 'r') as file:
        #         story = file.read
        #         print(name)
        #         print(story)
        #         if story == name:
        #             confirm = input("There is already a story for this character. Begin another?\n >Yes\n >No").capitalize()
        #             if confirm == "No":
        #                 confirm2 = input(f"Would you like to hear the {name}'s story were we left off?\n Yes")
        #                 if confirm2 == "Yes":
        #                     game_continue(name)
        # except FileNotFoundError:
        #     print("It no work :(")
        classes = ["Knight", "Wizard", "Archer"]
        if name in classes:
            return name
        else:
            print("Not a valid choice. You're choices are Knight, Wizard, and Archer.")
            name = input("> ")
def player_fill(name):
    if name == "Knight":
        Characters.char_maxhp = 50
        Characters.char_atk = 5
        Characters.char_def = 5
        Characters.char_spd = 1
    elif name == "Wizard":
        Characters.char_maxhp = 50
        Characters.char_atk = 9
        Characters.char_def = 1
        Characters.char_spd = 2
    elif name == "Archer":
        Characters.char_maxhp = 50
        Characters.char_atk = 7
        Characters.char_def = 3
        Characters.char_spd = 3
    return

def save_create(name):
    with open(f"{name}'s-Story.txt", 'w') as file:
            file.write(name)
            print("Save created")

def base_camp():
    choice = input("You are resting from your journey.\n What will you do?\n >Relax\n >Explore\n >Sleep (Save and Quit)\n >").capitalize()
    return choice

def hp_restore():
    Characters.char_maxhp == 50
    return

def enemy_roll():
    enemies = ["goblin", "undead", "bandit"]
    enemy_type_number = random.randint(0,2)
    if enemy_type_number == 0:
        enemy = enemies[0]
    elif enemy_type_number == 1:
        enemy = enemies[1]
    elif enemy_type_number == 2:
        enemy = enemies[2]
    Enemies.enm_type = enemy
    return enemy

def enemy_fill(name):
    if name == "goblin":
        Enemies.enm_maxhp = 50
        Enemies.enm_atk = 9
        Enemies.enm_def = 1
        Enemies.enm_spd = 2
    elif name == "undead":
        Enemies.enm_maxhp = 50
        Enemies.enm_atk = 5
        Enemies.enm_def = 5
        Enemies.enm_spd = 1
    elif name == "bandit":
        Enemies.enm_maxhp = 50
        Enemies.enm_atk = 7
        Enemies.enm_def = 3
        Enemies.enm_spd = 3
    return


def environmental():
    environment = ["plains", "mountains", "desert", "arctic", "forest"]
    environment_type_number = random.randint(0, 4)
    if environment_type_number == 0:
        element = environment[0]
    elif environment_type_number == 1:
        element = environment[1]
    elif environment_type_number == 2:
        element = environment[2]
    elif environment_type_number == 3:
        element = environment[3]
    elif environment_type_number == 4:
        element = environment[4]
    return element

def environmental_advantage_player(element):
    if element == "plains":
        return Characters.char_atk
    elif element == "mountains":
        if Characters.char_type == "Wizard":
            player_advantage = Characters.char_atk + 2
            return player_advantage
        elif Characters.char_type == "Knight":
            player_advantage = Characters.char_atk - 2
            return player_advantage
        else:
            return Characters.char_atk
    elif element == "forest":
        if Characters.char_type == "Knight":
            player_advantage = Characters.char_atk + 2
            return player_advantage
        elif Characters.char_type == "Archer":
            player_advantage = Characters.char_atk - 2
            return player_advantage
        else:
            return Characters.char_atk
    elif element == "desert":
        if Characters.char_type == "Archer":
            player_advantage = Characters.char_atk + 2
            return player_advantage
        elif Characters.char_type == "Wizard":
            player_advantage = Characters.char_atk - 2
            return player_advantage
        else:
            return Characters.char_atk
    elif element == "arctic":
        return Characters.char_atk
    
def environmental_advantage_enemy(element):
    if element == "plains":
        return Enemies.enm_atk
    elif element == "mountains":
        if Enemies.enm_type == "goblin":
            enemy_advantage = Enemies.enm_atk + 2
            return enemy_advantage
        elif Enemies.enm_type == "undead":
            enemy_advantage = Enemies.enm_atk - 2
            return enemy_advantage
        else:
            return Enemies.enm_atk
    elif element == "forest":
        if Enemies.enm_type == "bandit":
            enemy_advantage = Enemies.enm_atk + 2
            return enemy_advantage
        elif Enemies.enm_type == "goblin":
            enemy_advantage = Enemies.enm_atk - 2
            return enemy_advantage
        else:
            return Enemies.enm_atk
    elif element == "desert":
        if Enemies.enm_type == "undead":
            enemy_advantage = Enemies.enm_atk + 2
            return enemy_advantage
        elif Enemies.enm_type == "bandit":
            enemy_advantage = Enemies.enm_atk - 2
            return enemy_advantage
        else:
            return Enemies.enm_atk
    elif element == "arctic":
        return Enemies.enm_atk
        
def enemy_move(attack, counter):
    while True:
        move = random.randint(0,2)
        if move == 0:
            print(f"The {Enemies.enm_type} attacks")
            atk_def_enemy(attack)
            return
        if move == 1:
            print(f"The {Enemies.enm_type} defends")
            enemy_defend()
            return
        if move == 2 and counter <= 0:
            print(f"The {Enemies.enm_type} uses their ability")
            enemy_ability(attack, counter)
            return
        else:
            print("Enemy can't use ability")
            move = random.randint(0,1)
    
def atk_def_player(attack):
    miss = dodge_chance_enemy()
    if miss == True:
        return
    var = random.randint(-5, 5)
    damage = attack + var - Enemies.enm_def
    if damage <= 0:
        print("You did 0 damage")
        return
    else:
        print(f"You did {damage} damage")
        health = Enemies.enm_maxhp - damage
        Enemies.enm_maxhp = health
        return
    
def dodge_chance_player():
    speed = Characters.char_spd
    var = random.randint(1, 20)
    if speed >= var:
        print("You dodge")
        return True
    else:
        print("You did not dodge")
        return False


def dodge_chance_enemy():
    speed = Enemies.enm_spd
    var = random.randint(1, 20)
    if speed >= var:
        print(f"The {Enemies.enm_type} dodges")
        return True
    else:
        return False

def atk_def_enemy(attack):
    miss = dodge_chance_player()
    if miss == True:
        return
    var = random.randint(-5, 5)
    damage = attack + var - Characters.char_def
    if damage <= 0:
        print("You took 0 damage")
        return
    else:
        print(f"You took {damage} damage")
        health = Characters.char_maxhp - damage
        Characters.char_maxhp = health
        return

def player_defend():
    print("You defend")
    var = random.randint(0,2)
    Characters.char_def = 3 + var
    return

def enemy_defend():
    var = random.randint(0,2)
    Enemies.enm_def = 3 + var
    return

def player_ability(attack, counter):
    if Characters.char_type == "Knight":
        while True:
            choice = input("Which ability would you like to use?\n >1 (Dual Strike)\n >2 (Shield Bash)\n >")
            if choice == "1":
                print("You use Dual Strike")
                atk_def_player(attack)
                atk_def_player(attack)
                return
            elif choice == 2:
                print("You use Shield Bash")
                ability_shield()
                return "Stunned"
            else:
                print("Not an option")
    elif Characters.char_type == "Wizard":
        while True:
            choice = input("Which ability would you like to use?\n >1 (Fireball)\n >2 (Heal Spell)\n >")
            if choice == "1":
                print("You cast Fireball")
                atk_def_player(attack)
                wizard_fireball()
                DOT = "DOT"
                return DOT

def ability_shield():
    Enemies.enm_maxhp -= 3
    print("You did 3 damage")
    return
    
def wizard_fireball():
    print(f"You have burned {Enemies.enm_type}")
    DOT = 3
    return


def enemy_ability(attack, counter):
    atk_def_enemy(attack)
    atk_def_enemy(attack)
    return

# def item_choice():
#     print("You're items are:")
#     for item in items:
#         print(item)
#     while True:
#         choice = input("Which would you like to use?\n >").capitalize()
#         if choice in items:
#             print(f"You use {choice}")
#         else:
#             print("Not an option. Returning.")
#             return "Back"

def dot_effect():
    var = random.randint(1,3)
    Enemies.enm_maxhp = Enemies.enm_maxhp - var
    print(f"The {Enemies.enm_type} took {var} damage from burn")
    return

def main():
    save = game_start()
    if save == "Knight" or save == "Wizard" or save == "Archer":
        Characters.char_type = save
        player_fill(save)
        # THIS IS WHERE WE IMPLEMENT SAVED SCORE
    elif save == "New":
        player_score = 0
        player_char = character_validator()
        Characters.char_type = player_char
        player_fill(player_char)
        save_create(player_char)
    while player_score < 10:
        while True:
            home = base_camp()
            if home == "Relax":
                print("You relax and tend to your wounds")
                hp_restore()
            elif home == "Explore":
                break
            else:
                print("I don't know try again.")
        enemy = enemy_roll()
        enemy_fill(enemy)
        element = environmental()
        print(f"You encounter {enemy} in the {element}")
        player_attack = environmental_advantage_player(element)
        enemy_attack = environmental_advantage_enemy(element)
        counter = 2
        enemy_counter = 2
        DOT = 0
        while Enemies.enm_maxhp > 0 or Characters.char_maxhp > 0:
            while DOT != 0:
                dot_effect()
                DOT -= 1
                break
            print(f"{Enemies.enm_type} has {Enemies.enm_maxhp} health")
            print(f"You have {Characters.char_maxhp} health")
            counter -= 1
            enemy_counter -= 1
            if counter <= 0:
                Characters.char_ability = True
            else:
                Characters.char_ability = False
            if Characters.char_ability == True:
                status = "ready"
            else:
                status = "not ready"
            move = input(f"What will you do? Your ability is {status}\n>Attack\n>Defend\n>Ability\n>").capitalize()
            while True:
                if move == "Attack":
                    player_turn = atk_def_player(player_attack)
                    enemy_turn = enemy_move(enemy_attack, enemy_counter)
                    break
                elif move == "Defend":
                    player_turn = player_defend()
                    enemy_turn = enemy_move(enemy_attack, enemy_counter)
                    break
                elif move == "Ability":
                    if Characters.char_ability == True:
                        player_turn = player_ability(player_attack, counter)
                        if player_turn == "Stunned":
                            break
                        elif player_turn == "DOT":
                            DOT = 3
                            enemy_turn = enemy_move(enemy_attack, enemy_counter)
                            counter = 3
                            break
                        else:
                            enemy_turn = enemy_move(enemy_attack, enemy_counter)
                            counter = 3
                            break
                    else:
                        print(f"Ability not ready. Ability will be ready in {counter} turns.")
                # ONLY IF WANTED NOT NECESSARY
                # elif move == "Item":
                #     item = item_choice()
                #     if item != "Back":
                #         break
                #     else:
                #         move = input(f"What will you do? Your ability is {status}\n>Attack\n>Defend\n>Ability\n>").capitalize()
                else:
                    print("Not an option")
            if Enemies.enm_maxhp <= 0:
                print("YOU WIN!")
                player_score += 1
                break
            elif Characters.char_maxhp <= 0:
                print("you lose...")
                break


if __name__ == "__main__":
    main()