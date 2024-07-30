from dataclasses import dataclass
import random   

@dataclass
class Characters:
    char_type: str
    char_maxhp: int
    char_atk: int
    char_def: int
    char_ability: bool
    
class Enemies:
    enm_type: str
    enm_maxhp: int
    enm_atk: int
    enm_def: int
    # enm_ablilty: bool

def character_validator():
    name = input("Please choose a character. You're options are:\nKnight, Wizard, and Archer.\n>").capitalize()
    while True:
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
    elif name == "Wizard":
        Characters.char_maxhp = 50
        Characters.char_atk = 9
        Characters.char_def = 1
    elif name == "Archer":
        Characters.char_maxhp = 50
        Characters.char_atk = 7
        Characters.char_def = 3
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
    elif name == "undead":
        Enemies.enm_maxhp = 50
        Enemies.enm_atk = 5
        Enemies.enm_def = 5
    elif name == "bandit":
        Enemies.enm_maxhp = 50
        Enemies.enm_atk = 7
        Enemies.enm_def = 3
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
            player_advantage = Characters.char_atk + 5
            return player_advantage
        elif Characters.char_type == "Knight":
            player_advantage = Characters.char_atk - 5
            return player_advantage
        else:
            return Characters.char_atk
    elif element == "forest":
        if Characters.char_type == "Knight":
            player_advantage = Characters.char_atk + 5
            return player_advantage
        elif Characters.char_type == "Archer":
            player_advantage = Characters.char_atk - 5
            return player_advantage
        else:
            return Characters.char_atk
    elif element == "desert":
        if Characters.char_type == "Archer":
            player_advantage = Characters.char_atk + 5
            return player_advantage
        elif Characters.char_type == "Wizard":
            player_advantage = Characters.char_atk - 5
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
            enemy_advantage = Enemies.enm_atk + 5
            return enemy_advantage
        elif Enemies.enm_type == "undead":
            enemy_advantage = Enemies.enm_atk - 5
            return enemy_advantage
        else:
            return Enemies.enm_atk
    elif element == "forest":
        if Enemies.enm_type == "bandit":
            enemy_advantage = Enemies.enm_atk + 5
            return enemy_advantage
        elif Enemies.enm_type == "goblin":
            enemy_advantage = Enemies.enm_atk - 5
            return enemy_advantage
        else:
            return Enemies.enm_atk
    elif element == "desert":
        if Enemies.enm_type == "undead":
            enemy_advantage = Enemies.enm_atk + 5
            return enemy_advantage
        elif Enemies.enm_type == "bandit":
            enemy_advantage = Enemies.enm_atk - 5
            return enemy_advantage
        else:
            return Enemies.enm_atk
    elif element == "arctic":
        return Enemies.enm_atk
        
def enemy_move(attack, counter):
    while True:
        move = random.randint(0,2)
        if move == 0:
            print("The enemy attacks")
            atk_def_enemy(attack)
            return
        if move == 1:
            print("The enemy defends")
            enemy_defend()
            return
        if move == 2 and counter <= 0:
            print("The enemy uses their ability")
            enemy_ability(attack, counter)
            return
        else:
            print("Enemy can't use ability")
            move = random.randint(0,1)
    
def atk_def_player(attack):
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
def atk_def_enemy(attack):
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
        print("You use Dual Strike")
        atk_def_player(attack)
        atk_def_player(attack)
        return
    # elif Characters.char_type == "Wizard":
    #     pass
    
def enemy_ability(attack, counter):
    atk_def_enemy(attack)
    atk_def_enemy(attack)
    return



def main():
    player_char = character_validator()
    Characters.char_type = player_char
    player_fill(player_char)
    enemy = enemy_roll()
    enemy_fill(enemy)
    element = environmental()
    print(f"You encounter {enemy} in the {element}")
    player_attack = environmental_advantage_player(element)
    enemy_attack = environmental_advantage_enemy(element)
    counter = 2
    enemy_counter = 2
    while Enemies.enm_maxhp > 0 or Characters.char_maxhp > 0:
        print(f"The enemy has {Enemies.enm_maxhp} health.")
        print(f"You have {Characters.char_maxhp} health.")
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
        if move == "Attack":
            player_turn = atk_def_player(player_attack)
            enemy_turn = enemy_move(enemy_attack, enemy_counter)
        elif move == "Defend":
            player_turn = player_defend()
            enemy_turn = enemy_move(enemy_attack, enemy_counter)
        elif move == "Ability":
            if Characters.char_ability == True:
                player_turn = player_ability(player_attack, counter)
                enemy_turn = enemy_move(enemy_attack, enemy_counter)
                counter = 3
            else:
                print(f"Ability not ready. Ability will be ready in {counter} turns.")
        else:
            print("Not an option")
        if Enemies.enm_maxhp <= 0:
            print("YOU WIN!")
            break
        elif Characters.char_maxhp <= 0:
            print("you lose...")
            break


if __name__ == "__main__":
    main()