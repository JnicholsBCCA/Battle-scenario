from dataclasses import dataclass
from time import sleep
import random  
import os

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

def find_highest_score(files):
    highest_score = -1
    highest_scoring_class = None

    for file in files:
        try:
            with open(file, 'r') as f:
                class_name = f.readline().strip()
                score = int(f.readline().strip())
                if score > highest_score:
                    highest_score = score
                    highest_scoring_class = class_name
        except FileNotFoundError:
            continue

    return highest_scoring_class, highest_score

def game_start():
        print("Greetings weary traveler, come rest by the fire and I will tell you a story.")
        files = ["Knight's-Story.txt", "Archer's-Story.txt", "Wizard's-Story.txt"]
        existing_files = [file for file in files if os.path.exists(file)]
        highest_scoring_class, highest_score = find_highest_score(files)
        if not existing_files:
            print("I have no old tales to tell, perhaps you would like to start a new one?")

        elif highest_score == 0:
            pass
        elif highest_scoring_class:
            print(f"Would you like to hear about the {highest_scoring_class}, who has slain {highest_score} enemies?\nOr maybe you want to hear the tale of another hero? ")
        files = ["Knight's-Story.txt", "Archer's-Story.txt", "Wizard's-Story.txt"]
        choice = input("What would you like to hear?\n >New Story\n >Continue Story\n >Leave\n >").capitalize()
        if choice == "New" or choice == "New story" or choice == "New Story":
            return "New"
        elif choice == "Continue" or "C":
            character = input("Who's story should I continue?\n >Knight\n >Wizard\n >Archer\n >").capitalize()
            story = game_continue(character)   
            return story
        elif choice == "Leave":
            quit()
        else:
            print("Placeholder for in-character comment")
            choice = input("What would you like to hear?\n >New Story\n >Continue Story\n >Leave\n >").capitalize()

def game_continue(character):
    while True:
            if character == "Knight":
                try:
                    with open(f"Knight's-story.txt", 'r') as file:
                        progress = file.readlines()
                        score = progress[1]
                        if score.isdigit():
                            score = int(score)
                        save = [character, score]
                        return save
                except FileNotFoundError:
                    print("I have not told you a story about them.")
                    character = input("Who's story should I continue?\n >Knight\n >Wizard\n >Archer\n >").capitalize()
            elif character == "Wizard":
                try:
                    with open(f"Wizard's-story.txt", 'r') as file:
                        progress = file.readlines()
                        score = progress[1]
                        if score.isdigit():
                            score = int(score)
                        save = [character, score]
                        return save
                except FileNotFoundError:
                    print("I have not told you a story about them.")
                    character = input("Who's story should I continue?\n >Knight\n >Wizard\n >Archer\n >").capitalize()
            elif character == "Archer":
                try:
                    with open(f"Archer's-story.txt", 'r') as file:
                        progress = file.readlines()
                        score = progress[1]
                        if score.isdigit():
                            score = int(score)
                        save = [character, score]
                        return save
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
        #         reading = file.readlines()
        #         story = reading[0]
        #         print(name.strip())
        #         print(story.strip())
        #     if story == name:
        #         confirm = input("There is already a story for this character. Begin another?\n >Yes\n >No").capitalize()
        #         if confirm == "No":
        #             confirm2 = input(f"Would you like to hear the {name}'s story were we left off?\n Yes")
        #             if confirm2 == "Yes":
        #                 game_continue(name)
        # except FileNotFoundError:
        #     print("It no work :(")
        classes = ["Knight", "Wizard", "Archer"]
        if name in classes:
            return name
        else:
            print("Not a valid choice. Your choices are Knight, Wizard, and Archer.")
            name = input("> ")
    
def player_fill(name):
    if name == "Knight":
        Characters.char_maxhp = 60
        Characters.char_atk = 10
        Characters.char_def = 7
        Characters.char_spd = 1
    elif name == "Wizard":
        Characters.char_maxhp = 45
        Characters.char_atk = 14
        Characters.char_def = 5
        Characters.char_spd = 2
    elif name == "Archer":
        Characters.char_maxhp = 50
        Characters.char_atk = 11
        Characters.char_def = 4
        Characters.char_spd = 3
    return


def base_camp():
    choice = input("You are resting from your journey.\n What will you do?\n >Relax\n >Explore\n >Sleep (Save and Quit)\n >").capitalize()
    return choice

def save_and_quit(score):
    name = Characters.char_type
    with open(f"{name}'s-Story.txt", 'w') as file:
        file.write(name)
        print("Save created")
        score = str(score)
        file.write(f"\n{score}")
    quit()
def hp_restore():
    if Characters.char_type == "Knight":
        Characters.char_maxhp = 60
    elif Characters.char_type == "Wizard":
        Characters.char_maxhp = 45
    elif Characters.char_type == "Archer":
        Characters.char_maxhp = 50

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
        Enemies.enm_maxhp = 40
        Enemies.enm_atk = 13
        Enemies.enm_def = 4
        Enemies.enm_spd = 2
    elif name == "undead":
        Enemies.enm_maxhp = 50
        Enemies.enm_atk = 9
        Enemies.enm_def = 6
        Enemies.enm_spd = 1
    elif name == "bandit":
        Enemies.enm_maxhp = 50
        Enemies.enm_atk = 11
        Enemies.enm_def = 5
        Enemies.enm_spd = 3
    return

def enemy_fill_boss(boss):
    Enemies.enm_type = boss
    Enemies.enm_maxhp = 100
    Enemies.enm_atk = 15
    Enemies.enm_def = Characters.char_atk - 5
    Enemies.enm_spd = 7
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
            counter = 3
            return counter
        else:
            move = random.randint(0,1)
    

def atk_def_player(attack):
    miss = dodge_chance_enemy()
    if miss == True:
        return
    var = random.randint(-2, 5)
    damage = attack + var - Enemies.enm_def
    if damage <= 0:
        print("You did 0 damage")
        sleep(.3)
        return
    else:
        print(f"You did {damage} damage")
        sleep(.3)
        health = Enemies.enm_maxhp - damage
        Enemies.enm_maxhp = health
        return
    
def dodge_chance_player():
    speed = Characters.char_spd
    var = random.randint(1, 20)
    if speed >= var:
        sleep(.3)
        print("You dodge")
        sleep(.3)
        return True
    else:
        return False


def dodge_chance_enemy():
    speed = Enemies.enm_spd
    var = random.randint(1, 20)
    if speed >= var:
        sleep(.3)
        print(f"{Enemies.enm_type} dodges")
        sleep(.3)
        return True
    else:
        return False

def atk_def_enemy(attack):
    miss = dodge_chance_player()
    if miss == True:
        return
    var = random.randint(-2, 3)
    damage = attack + var - Characters.char_def
    if damage <= 0:
        print("You took 0 damage")
        sleep(.3)
        return
    else:
        print(f"You took {damage} damage")
        sleep(.3)
        health = Characters.char_maxhp - damage
        Characters.char_maxhp = health
        return

def player_defend():
    print("You defend")
    sleep(.3)
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
                sleep(.3)
                atk_def_player(attack)
                sleep(.3)
                return
            elif choice == 2:
                print("You use Shield Bash")
                ability_shield()
                sleep(.3)
                return "Stunned"
            else:
                print("Not an option")
                sleep(.3)
                choice = input("Which ability would you like to use?\n >1 (Dual Strike)\n >2 (Shield Bash)\n >")
    elif Characters.char_type == "Wizard":
        while True:
            choice = input("Which ability would you like to use?\n >1 (Fireball)\n >2 (Heal Spell)\n >")
            if choice == "1":
                print("You cast Fireball")
                sleep(.3)
                atk_def_player(attack)
                DOT_fire()
                DOT = "DOT"
                return DOT
            if choice == "2":
                print("You cast heal spell")
                sleep(.3)
                heal_spell()
                return

def ability_shield():
    Enemies.enm_maxhp -= 3
    print("You did 3 damage")
    sleep(.3)
    return
    
def DOT_fire():
    print(f"You have burned {Enemies.enm_type}")
    sleep(.3)
    DOT = 3
    return

def heal_spell():
    if Characters.char_maxhp < 45:
        Characters.char_maxhp = Characters.char_maxhp + 10
        if Characters.char_maxhp > 45:
            Characters.char_maxhp = 45
    if Characters.char_maxhp < 45:
        Characters.char_maxhp = Characters.char_maxhp + 15
        if Characters.char_maxhp > 45:
            Characters.char_maxhp = 45
    else:
        print("Health is full. Congratulations, you wasted your turn.")
    return


def enemy_ability(attack, counter):
    atk_def_enemy(attack)
    sleep(.3)
    atk_def_enemy(attack)
    return

# def item_choice():
#     print("You're items are:")
#     for item in items:
#         print("> " + item)
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
    print(f"{Enemies.enm_type} took {var} damage from burn")
    sleep(.3)
    return

def boss_battle():
    print("It's dark and quiet. You think about turning back.")
    sleep(5)
    print("You wander for what seems like hours.")
    sleep(5)
    print("You look up, the floor bends.")
    sleep(5)
    print("You try to remember what they look like.")
    sleep(5)
    print(f"There is no {Characters.char_type}.")
    sleep(8)
    boss_var = random.randint(1,2)
    if boss_var == 1:
        boss = "Trey"
    elif boss_var == 2:
        boss = "Logan"
    print(f"{boss} attacks")
    sleep(2)
    enemy_fill_boss(boss)
    print(f"You encounter {boss} in the Void")
    sleep(.3)
    counter = 2
    enemy_counter = 2
    DOT = 0
    boss_count = 2
    while True:
        while boss_count != 0:
            if Characters.char_type == "Knight":
                Characters.char_def = 7
            elif Characters.char_type == "Wizard":
                Characters.char_def = 5
            elif Characters.char_type == "Archer":
                Characters.char_def = 4
            while DOT != 0:
                dot_effect()
                DOT -= 1
                break
            if Enemies.enm_maxhp <= 0:
                player_victory()
                break
            print(f"{Enemies.enm_type} has {Enemies.enm_maxhp} health")
            sleep(.3)
            print(f"You have {Characters.char_maxhp} health")
            sleep(.3)
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
            move = input(f"What can you do? Your ability is {status}\n>Attack\n>Defend\n>Ability\n>").capitalize()
            sleep(.3)
            if move == "Attack":
                player_turn = atk_def_player(Characters.char_atk)
                sleep(.3)
                boss_count -= 1
                break
            elif move == "Defend":
                player_turn = player_defend()
                sleep(.3)
                boss_count -= 1
                break
            elif move == "Ability":
                if Characters.char_ability == True:
                    player_turn = player_ability(Characters.char_atk, counter)
                    sleep(.3)
                    if player_turn == "Stunned":
                        counter = 3
                        boss_count -= 1
                        break
                    elif player_turn == "DOT":
                        DOT = 3
                        counter = 3
                        boss_count -= 1
                        break
                    else:
                        counter = 3
                        boss_count -= 1
                        break
                else:
                    print(f"Ability not ready. Ability will be ready in {counter} turn(s).")
                    move = input(f"What can you do? Your ability is {status}\n>Attack\n>Defend\n>Ability\n>").capitalize()
                    sleep(.3)
        else:
            boss_turn()
            boss_count = 2
        if Enemies.enm_maxhp <= 0:
            player_victory()
            while True:
                finale = input("Continue?\n >Yes\n >No\n >").capitalize
                if finale == "Yes":
                    return
                elif finale == "No":
                    quit()
                else:
                    print("Try again.")
        elif Characters.char_maxhp <= 0:
            print("You succumb to the darkness")
            quit()

def boss_turn():
    move = random.randint(1,2)
    if move == 1:
        boss_attack()
    elif move == 2:
        boss_fear()
    elif move == 3:
        boss_spec()
    return

def boss_attack():
    miss = dodge_chance_player()
    if miss == True:
        return
    var = random.randint(0, 3)
    print(f"The presence of {Enemies.enm_type} is overwhelming.")
    sleep(.5)
    print("You don't want to feel anymore")
    sleep(1)
    psycho_damage = Enemies.enm_atk + var
    pain = psycho_damage - Characters.char_def
    health = Characters.char_maxhp - pain
    Characters.char_maxhp = health
    return
    

def boss_fear():
    print(f"You try to comprehend {Enemies.enm_type}.")
    sleep(.5)
    print("Your defense and evasiveness fell.")
    sleep(1)
    Characters.char_def -= 3
    Characters.char_spd = 0
    return

def boss_spec():
    var = random.randint(1,3)
    if var != 1:
        print(f"{Enemies.enm_type} consumes your spirit.")
        sleep(.5)
        print("You feel empty")
        sleep(1)
        Characters.char_maxhp /= 2
        return
    else:
        print("You were spared.")
        return
        

    
def player_victory():
    print("You break the loop")
    sleep(5)
    print("Despite everything, you feel happy")
    sleep(5)
    print("YOU WIN!!!")
    choice = input("Enter your name for the records!\n >")
    try:
        with open("Game-Victors.txt", 'a') as file:
            file.write(f"\n{choice} has completed the game!")
    except FileNotFoundError:
        with open("Game-Victors.txt", 'w') as file:
            file.write(f"{choice} has completed the game!")
    return
    

def main():
    save = game_start()
    if save != "New":
        Characters.char_type = save[0]
        player_score = save[1]
        player_fill(Characters.char_type)
    elif save == "New":
        player_score = 0
        player_char = character_validator()
        Characters.char_type = player_char
        player_fill(player_char)
    while player_score != 10:
        while True:
            home = base_camp()
            if home == "Relax":
                print("You relax and tend to your wounds")
                sleep(.3)
                hp_restore()
            elif home == "Explore":
                sleep(.3)
                break
            elif home == "Sleep":
                save_and_quit(player_score)
            else:
                print("I don't know try again.")
        enemy = enemy_roll()
        enemy_fill(enemy)
        element = environmental()
        print(f"You encounter {enemy} in the {element}")
        sleep(.3)
        player_attack = environmental_advantage_player(element)
        enemy_attack = environmental_advantage_enemy(element)
        counter = 2
        enemy_counter = 2
        DOT = 0
        while Enemies.enm_maxhp > 0 or Characters.char_maxhp > 0:
            if Characters.char_type == "Knight":
                Characters.char_def = 7
            elif Characters.char_type == "Wizard":
                Characters.char_def = 5
            elif Characters.char_type == "Archer":
                Characters.char_def = 4
            while DOT != 0:
                dot_effect()
                DOT -= 1
                break
            if Enemies.enm_maxhp <= 0:
                print("YOU WIN!")
                player_score += 1
                print(f"Your score is now {player_score}")
                break
            print(f"{Enemies.enm_type} has {Enemies.enm_maxhp} health")
            sleep(.3)
            print(f"You have {Characters.char_maxhp} health")
            sleep(.3)
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
            sleep(.3)
            while True:
                if move == "Attack":
                    player_turn = atk_def_player(player_attack)
                    sleep(.3)
                    enemy_turn = enemy_move(enemy_attack, enemy_counter)
                    if enemy_turn == 3:
                        enemy_counter = 3
                    sleep(.3)
                    break
                elif move == "Defend":
                    player_turn = player_defend()
                    sleep(.3)
                    enemy_turn = enemy_move(enemy_attack, enemy_counter)
                    if enemy_turn == 3:
                        enemy_counter = 3
                    sleep(.3)
                    break
                elif move == "Ability":
                    if Characters.char_ability == True:
                        player_turn = player_ability(player_attack, counter)
                        sleep(.3)
                        if player_turn == "Stunned":
                            break
                        elif player_turn == "DOT":
                            DOT = 3
                            enemy_turn = enemy_move(enemy_attack, enemy_counter)
                            if enemy_turn == 3:
                                enemy_counter = 3
                            sleep(.3)
                            counter = 3
                            break
                        else:
                            enemy_turn = enemy_move(enemy_attack, enemy_counter)
                            if enemy_turn == 3:
                                enemy_counter = 3
                            sleep(.3)
                            counter = 3
                            break
                    else:
                        print(f"Ability not ready. Ability will be ready in {counter} turn(s).")
                        move = input(f"What will you do? Your ability is {status}\n>Attack\n>Defend\n>Ability\n>").capitalize()
                        sleep(.3)
                # ONLY IF WANTED NOT NECESSARY
                # elif move == "Item":
                #     item = item_choice()
                #     if item != "Back":
                #         break
                #     else:
                #         move = input(f"What will you do? Your ability is {status}\n>Attack\n>Defend\n>Ability\n>").capitalize()
                else:
                    print("Not an option")
                    move = input(f"What will you do? Your ability is {status}\n>Attack\n>Defend\n>Ability\n>").capitalize()
            if Enemies.enm_maxhp <= 0:
                print("YOU WIN!")
                player_score += 1
                print(f"Your score is now {player_score}")
                break
            elif Characters.char_maxhp <= 0:
                print("you lose...")
                cheater = input("Save your score?\n >yes\n >no\n >")
                if cheater == "yes":
                    save_and_quit(player_score)
                quit()
    else:
        hp_restore()
        print("You arrive at the castle...")
        helpless = True
        while helpless == True:
            hopeless = input("You want to leave.\n >Proceed\n >Leave\n >").capitalize()
            if hopeless == "Leave":
                print("You can't")
            else:
                print("You proceed")
                boss_battle()
                player_score += 1
                


if __name__ == "__main__":
    main()