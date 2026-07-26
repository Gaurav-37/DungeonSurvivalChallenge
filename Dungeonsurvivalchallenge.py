import random
import enemy
import hero
import location
import trap
import treasure
import weapon
import event

username = ""
class_chosen_name = ""
weapon_name = ""
game_state = True
threat_level = 0
weapon_damage = 0
base_health = 0
base_min_damage  = 0
base_max_damage = 0
gold = 0
heal_counter = 0
rooms_completed = 0
enemies_defeated = 0
enemies_escaped = 0
treasures_collected = []
upgrade_opportunity_used = False
upgraded_weapon_received = False
escaped_final_battle = False
final_rank = ""
final_result = ""
line = "=" * 60
small_line = "-" * 60

print(f"\n{line}")
print("DUNGEON SURVIVAL CHALLENGE")
print(f"{line}\n")

username = input("Enter your hero name: ").strip()

while username.strip() == "":
    print("\nName cannot be empty. Please try again.\n")
    username = input("Enter your hero name: ").strip()
else:
    print(f"\nWelcome, {username}.\n")

if game_state == True: 
    class_input = input(f"{small_line}\nCHOOSE YOUR CLASS\n{small_line}\n1. Warrior\n   Health: {hero.hero_list[0][1]}\n   Damage: {hero.hero_list[0][2]}-{hero.hero_list[0][3]}\n   Passive: Reduces enemy damage by 5\n\n2. Mage\n   Health: {hero.hero_list[1][1]}\n   Damage: {hero.hero_list[1][2]}-{hero.hero_list[1][3]}\n   Passive: 25% chance to deal double damage\n\n3. Rogue\n   Health: {hero.hero_list[2][1]}\n   Damage: {hero.hero_list[2][2]}-{hero.hero_list[2][3]}\n   Passive: 25% chance to evade enemy attacks and 30% chance to avoid trap damage\n\nEnter 1, 2, or 3: ").strip()
    if class_input == "1":
        class_option = 0
    elif class_input == "2":
        class_option = 1
    elif class_input == "3":
        class_option = 2
    else:
        print("\nInvalid class selection.\n")
        game_state = False

if game_state == True:
    class_chosen_name = hero.hero_list[class_option][0]                     
    base_health += hero.hero_list[class_option][1]
    base_min_damage += hero.hero_list[class_option][2]
    base_max_damage += hero.hero_list[class_option][3]
    print(f"\n{small_line}")
    print("CLASS SELECTED")
    print(f"{small_line}")
    print(f"Class: {class_chosen_name}")
    print(f"Health: {base_health}")
    print(f"Damage: {base_min_damage}-{base_max_damage}\n")


if game_state == True:

    if class_option == 0:
        weapon_pool = [
            weapon.iron_sword,
            weapon.street_axe
        ]

    elif class_option == 1:
        weapon_pool = [
            weapon.iron_sword,
            weapon.magic_staff
        ]

    elif class_option == 2:
        weapon_pool = [
            weapon.iron_sword,
            weapon.shadow_dagger
        ]
    selected_weapon = random.choice(weapon_pool)

    weapon_name = selected_weapon[0]
    weapon_damage = selected_weapon[1]

    print(f"{small_line}")
    print("STARTING WEAPON")
    print(f"{small_line}")
    print(f"Weapon: {weapon_name}")
    print(f"Bonus Damage: +{weapon_damage}\n")

else:
    pass

normal_locations = random.sample(location.location_list[:4],4)
location_order = normal_locations + [location.dragons_lair]
enemy_order = random.sample(enemy.enemy_list[:5],5)
treasure_order = random.sample(treasure.treasure_list,5)
trap_order = random.sample(trap.trap_list,4)


event_order = []

for turn in range(0,4):
    event_randomizer = random.random()
    if event_randomizer <= 0.5:
        event_order.append(event.event_list[0])
    elif event_randomizer <= 0.7:
        event_order.append(event.event_list[1])
    elif event_randomizer <= 0.85:
        event_order.append(event.event_list[3])
    elif event_randomizer <= 0.95:
        event_order.append(event.event_list[2])
    else:
        event_order.append(event.event_list[4])

for i in range(0,4):
    if game_state == True:
        location_selected = location_order[i]
        print(f"\n{line}")
        print(f"ROOM {i + 1}: {location_selected}")
        print(f"{line}")
        
        event_selected = event_order[i]
        print(f"Event: {event_selected}")
        print(f"Health: {base_health} | Gold: {gold} | Weapon: {weapon_name} (+{weapon_damage})")

        if event_selected == "Enemy":
            
            current_enemy = enemy_order[i]
            current_enemy_name = enemy_order[i][0]
            current_enemy_health = int(enemy_order[i][1])
            current_enemy_min_damage = int(enemy_order[i][2])
            current_enemy_max_damage = int(enemy_order[i][3])
            current_enemy_reward = int(enemy_order[i][4])
            
            print(f"\n{small_line}")
            print("ENEMY ENCOUNTER")
            print(f"{small_line}")
            print(f"Enemy: {current_enemy_name}")
            print(f"Health: {current_enemy_health}")
            print(f"Reward: {current_enemy_reward} gold\n")
            
            while current_enemy_health > 0 and base_health > 0:
                action_input = input("Choose an action [attack / defend / heal / run]: ").strip().lower()
                if action_input == "attack":
                    base_random_damage = int(random.randint(base_min_damage,base_max_damage)+weapon_damage)

                    if class_chosen_name == "Mage":
                        mage_passive_chance = random.random()
                        if mage_passive_chance <= 0.25:
                            mage_damage = base_random_damage * 2
                            current_enemy_health -= mage_damage
                            print(f"\nMage passive activated: {mage_damage} damage dealt.")
                            print(f"{current_enemy_name} Health: {current_enemy_health}")
                        else:
                            current_enemy_health -= base_random_damage
                            print(f"\nYou attack for {base_random_damage} damage.")
                            print(f"{current_enemy_name} Health: {current_enemy_health}")
                    else:
                        critical_chance = random.random()
                        if critical_chance < 0.2:
                            critical_damage = base_random_damage * 2
                            current_enemy_health -= critical_damage
                            print(f"\nCritical hit: {critical_damage} damage dealt.")
                            print(f"{current_enemy_name} Health: {current_enemy_health}")
                        else:
                            current_enemy_health -= base_random_damage
                            print(f"\nYou attack for {base_random_damage} damage.")
                            print(f"{current_enemy_name} Health: {current_enemy_health}")

                    if current_enemy_health <= 0:
                        print(f"\n{current_enemy_name} defeated.")
                        gold += current_enemy_reward
                        enemies_defeated += 1
                        print(f"Gold gained: {current_enemy_reward}")
                        print(f"Total gold: {gold}\n")
                        if enemies_defeated == 3 and upgrade_opportunity_used == False:
                            upgrade_opportunity_used = True
                            weapon_upgrade_chance = random.random()
                            print(f"{small_line}")
                            print("WEAPON UPGRADE")
                            print(f"{small_line}")
                            if weapon_upgrade_chance <= 0.4:
                                selected_weapon = random.choice(weapon.upgraded_weapon_list)
                                weapon_name = selected_weapon[0]
                                weapon_damage = selected_weapon[1]
                                upgraded_weapon_received = True
                                print(f"You received an upgraded weapon: {weapon_name}")
                                print(f"New Bonus Damage: +{weapon_damage}\n")
                            else:
                                print("No upgraded weapon was found.\n")
                        break

                    current_enemy_random_damage = random.randint(current_enemy_min_damage,current_enemy_max_damage)

                    if class_chosen_name == "Rogue":
                        rogue_evade_chance = random.random()
                        if rogue_evade_chance <= 0.25:
                            print(f"\nRogue passive activated: you evaded the {current_enemy_name}'s attack.")
                        else:
                            base_health -= current_enemy_random_damage
                            print(f"\n{current_enemy_name} attacks for {current_enemy_random_damage} damage.")
                            print(f"Your Health: {base_health}")
                            if base_health <= 0:
                                print("\nYou have been defeated.")
                                game_state = False
                                break
                    else:
                        if class_chosen_name == "Warrior":
                            current_enemy_random_damage -= 5
                            if current_enemy_random_damage < 0:
                                current_enemy_random_damage = 0
                        base_health -= current_enemy_random_damage
                        print(f"\n{current_enemy_name} attacks for {current_enemy_random_damage} damage.")
                        print(f"Your Health: {base_health}")
                        if base_health <= 0:
                            print("\nYou have been defeated.")
                            game_state = False
                            break
                elif action_input == "defend":
                    current_enemy_random_damage = random.randint(current_enemy_min_damage,current_enemy_max_damage)
                    reduced_damage = current_enemy_random_damage // 2

                    if class_chosen_name == "Rogue":
                        rogue_evade_chance = random.random()
                        if rogue_evade_chance <= 0.25:
                            print(f"\nRogue passive activated: you evaded the {current_enemy_name}'s attack.")
                        else:
                            base_health -= reduced_damage
                            print(f"\nYou defend. Incoming damage reduced to {reduced_damage}.")
                            print(f"Your Health: {base_health}")
                            if base_health <= 0:
                                print("\nYou have been defeated.")
                                game_state = False
                                break
                    else:
                        if class_chosen_name == "Warrior":
                            reduced_damage -= 5
                            if reduced_damage < 0:
                                reduced_damage = 0
                        base_health -= reduced_damage
                        print(f"\nYou defend. Incoming damage reduced to {reduced_damage}.")
                        print(f"Your Health: {base_health}")
                        if base_health <= 0:
                            print("\nYou have been defeated.")
                            game_state = False
                            break
                elif action_input == "heal":
                    if heal_counter <= 2 and base_health < hero.hero_list[class_option][1]:
                        heal_counter += 1
                        health_amount_random = random.randint(15,30)
                        base_health += health_amount_random
                        if hero.hero_list[class_option][1] < base_health:
                           reduced_health = base_health - hero.hero_list[class_option][1]
                           base_health -= reduced_health
                           actaul_healed_amount = health_amount_random - reduced_health
                           print(f"\nHealing used: +{actaul_healed_amount}")
                           print(f"Your Health: {base_health}")
                        else:
                             print(f"\nHealing used: +{health_amount_random}")

                        current_enemy_random_damage = random.randint(current_enemy_min_damage,current_enemy_max_damage)

                        if class_chosen_name == "Rogue":
                            rogue_evade_chance = random.random()
                            if rogue_evade_chance <= 0.25:
                                print(f"\nRogue passive activated: you evaded the {current_enemy_name}'s attack.")
                            else:
                                base_health -= current_enemy_random_damage
                                print(f"\n{current_enemy_name} attacks for {current_enemy_random_damage} damage.")
                                print(f"Your Health: {base_health}")
                                if base_health <= 0:
                                    print("\nYou have been defeated.")
                                    game_state = False
                                    break
                        else:
                            if class_chosen_name == "Warrior":
                                current_enemy_random_damage -= 5
                                if current_enemy_random_damage < 0:
                                    current_enemy_random_damage = 0
                            base_health -= current_enemy_random_damage
                            print(f"\n{current_enemy_name} attacks for {current_enemy_random_damage} damage.")
                            print(f"Your Health: {base_health}")
                            if base_health <= 0:
                                print("\nYou have been defeated.")
                                game_state = False
                                break
                    else:
                        print("\nHeal unavailable: limit reached or health is already full.")
                elif action_input == "run":
                    run_chance = random.random()
                    if  run_chance <= 0.6:
                        print("\nYou escaped the enemy.")
                        enemies_escaped += 1
                        break
                    else:
                        print("\nEscape failed.")
                        current_enemy_random_damage = random.randint(current_enemy_min_damage,current_enemy_max_damage)

                        if class_chosen_name == "Rogue":
                            rogue_evade_chance = random.random()
                            if rogue_evade_chance <= 0.25:
                                print(f"\nRogue passive activated: you evaded the {current_enemy_name}'s attack.")
                            else:
                                base_health -= current_enemy_random_damage
                                print(f"\n{current_enemy_name} attacks for {current_enemy_random_damage} damage.")
                                print(f"Your Health: {base_health}")
                                if base_health <= 0:
                                    print("\nYou have been defeated.")
                                    game_state = False
                                    break
                        else:
                            if class_chosen_name == "Warrior":
                                current_enemy_random_damage -= 5
                                if current_enemy_random_damage < 0:
                                    current_enemy_random_damage = 0
                            base_health -= current_enemy_random_damage
                            print(f"\n{current_enemy_name} attacks for {current_enemy_random_damage} damage.")
                            print(f"Your Health: {base_health}")
                            if base_health <= 0:
                                print("\nYou have been defeated.")
                                game_state = False
                                break
                else:
                    print("\nInvalid action. Choose attack, defend, heal, or run.")
        elif event_selected == "Treasure":
            treasure_name = treasure_order[i][0]
            treasure_gold = treasure_order[i][1]
            gold += treasure_gold
            treasures_collected.append(treasure_name)
            print(f"\n{small_line}")
            print("TREASURE CHEST")
            print(f"{small_line}")
            print(f"Treasure: {treasure_name}")
            print(f"Gold found: {treasure_gold}")
            print(f"Total gold: {gold}")
        elif event_selected == "Trap":
            trap_name = trap_order[i][0]
            trap_hit_chance = random.random()
            trap_damage = random.randint(trap_order[i][1],trap_order[i][2])
            if class_chosen_name == "Rogue" and trap_hit_chance <= 0.3:
                print(f"\n{small_line}")
                print("TRAP")
                print(f"{small_line}")
                print("Rogue passive activated: you evaded the trap.")
            else:
                base_health -= trap_damage
                print(f"\n{small_line}")
                print("TRAP")
                print(f"{small_line}")
                print(f"Trap: {trap_name}")
                print(f"Damage taken: {trap_damage}")
                print(f"Your Health: {base_health}")
                if base_health <= 0:
                    print("\nYou died to a trap.")
                    game_state = False
                    break
                else:
                    print("You survived the trap.")
        elif event_selected == "Healing Fountain":
            health_amount_random = random.randint(20,45)
            base_health += health_amount_random
            print(f"\n{small_line}")
            print("HEALING FOUNTAIN")
            print(f"{small_line}")
            if hero.hero_list[class_option][1] < base_health:
               reduced_health = base_health - hero.hero_list[class_option][1]
               base_health -= reduced_health
               actaul_healed_amount = health_amount_random - reduced_health
               print(f"Health restored: +{actaul_healed_amount}")
               print(f"Your Health: {base_health}")
            else:
                print(f"Health restored: +{health_amount_random}")
                print(f"Your Health: {base_health}")
        else:
            print("\nThe room is empty. You move on.")

        if game_state == True:
            rooms_completed += 1

if game_state == True:
    last_dungeon_name = location_order[4]
    current_enemy = enemy.enemy_list[5]
    current_enemy_name = current_enemy[0]
    current_enemy_health = int(current_enemy[1])
    current_enemy_min_damage = int(current_enemy[2])
    current_enemy_max_damage = int(current_enemy[3])
    current_enemy_reward = int(current_enemy[4])
    
    print(f"\n{line}")
    print(f"FINAL BATTLE: {last_dungeon_name}")
    print(f"{line}")
    print(f"\n{small_line}")
    print("BOSS ENCOUNTER")
    print(f"{small_line}")
    print(f"Enemy: {current_enemy_name}")
    print(f"Health: {current_enemy_health}")
    print(f"Reward: {current_enemy_reward} gold\n")
    
    while current_enemy_health > 0 and base_health > 0:
        action_input = input("Choose an action [attack / defend / heal / run]: ").strip().lower()
        if action_input == "attack":
            base_random_damage = int(random.randint(base_min_damage,base_max_damage)+weapon_damage)

            if class_chosen_name == "Mage":
                mage_passive_chance = random.random()
                if mage_passive_chance <= 0.25:
                    mage_damage = base_random_damage * 2
                    current_enemy_health -= mage_damage
                    print(f"\nMage passive activated: {mage_damage} damage dealt.")
                    print(f"{current_enemy_name} Health: {current_enemy_health}")
                else:
                    current_enemy_health -= base_random_damage
                    print(f"\nYou attack for {base_random_damage} damage.")
                    print(f"{current_enemy_name} Health: {current_enemy_health}")
            else:
                critical_chance = random.random()
                if critical_chance < 0.2:
                    critical_damage = base_random_damage * 2
                    current_enemy_health -= critical_damage
                    print(f"\nCritical hit: {critical_damage} damage dealt.")
                    print(f"{current_enemy_name} Health: {current_enemy_health}")
                else:
                    current_enemy_health -= base_random_damage
                    print(f"\nYou attack for {base_random_damage} damage.")
                    print(f"{current_enemy_name} Health: {current_enemy_health}")

            if current_enemy_health <= 0:
                print(f"\n{current_enemy_name} defeated.")
                gold += current_enemy_reward
                enemies_defeated += 1
                print(f"Gold gained: {current_enemy_reward}")
                print(f"Total gold: {gold}\n")
                break

            current_enemy_random_damage = random.randint(current_enemy_min_damage,current_enemy_max_damage)

            if class_chosen_name == "Rogue":
                rogue_evade_chance = random.random()
                if rogue_evade_chance <= 0.25:
                    print(f"\nRogue passive activated: you evaded the {current_enemy_name}'s attack.")
                else:
                    base_health -= current_enemy_random_damage
                    print(f"\n{current_enemy_name} attacks for {current_enemy_random_damage} damage.")
                    print(f"Your Health: {base_health}")
                    if base_health <= 0:
                        print("\nYou have been defeated.")
                        game_state = False
                        break
            else:
                if class_chosen_name == "Warrior":
                    current_enemy_random_damage -= 5
                    if current_enemy_random_damage < 0:
                        current_enemy_random_damage = 0
                base_health -= current_enemy_random_damage
                print(f"\n{current_enemy_name} attacks for {current_enemy_random_damage} damage.")
                print(f"Your Health: {base_health}")
                if base_health <= 0:
                    print("\nYou have been defeated.")
                    game_state = False
                    break
        elif action_input == "defend":
            current_enemy_random_damage = random.randint(current_enemy_min_damage,current_enemy_max_damage)
            reduced_damage = current_enemy_random_damage // 2

            if class_chosen_name == "Rogue":
                rogue_evade_chance = random.random()
                if rogue_evade_chance <= 0.25:
                    print(f"\nRogue passive activated: you evaded the {current_enemy_name}'s attack.")
                else:
                    base_health -= reduced_damage
                    print(f"\nYou defend. Incoming damage reduced to {reduced_damage}.")
                    print(f"Your Health: {base_health}")
                    if base_health <= 0:
                        print("\nYou have been defeated.")
                        game_state = False
                        break
            else:
                if class_chosen_name == "Warrior":
                    reduced_damage -= 5
                    if reduced_damage < 0:
                        reduced_damage = 0
                base_health -= reduced_damage
                print(f"\nYou defend. Incoming damage reduced to {reduced_damage}.")
                print(f"Your Health: {base_health}")
                if base_health <= 0:
                    print("\nYou have been defeated.")
                    game_state = False
                    break
        elif action_input == "heal":
            if heal_counter <= 2 and base_health < hero.hero_list[class_option][1]:
                heal_counter += 1
                health_amount_random = random.randint(15,30)
                base_health += health_amount_random
                if hero.hero_list[class_option][1] < base_health:
                   reduced_health = base_health - hero.hero_list[class_option][1]
                   base_health -= reduced_health
                   actaul_healed_amount = health_amount_random - reduced_health
                   print(f"\nHealing used: +{actaul_healed_amount}")
                   print(f"Your Health: {base_health}")
                else:
                     print(f"\nHealing used: +{health_amount_random}")

                current_enemy_random_damage = random.randint(current_enemy_min_damage,current_enemy_max_damage)

                if class_chosen_name == "Rogue":
                    rogue_evade_chance = random.random()
                    if rogue_evade_chance <= 0.25:
                        print(f"\nRogue passive activated: you evaded the {current_enemy_name}'s attack.")
                    else:
                        base_health -= current_enemy_random_damage
                        print(f"\n{current_enemy_name} attacks for {current_enemy_random_damage} damage.")
                        print(f"Your Health: {base_health}")
                        if base_health <= 0:
                            print("\nYou have been defeated.")
                            game_state = False
                            break
                else:
                    if class_chosen_name == "Warrior":
                        current_enemy_random_damage -= 5
                        if current_enemy_random_damage < 0:
                            current_enemy_random_damage = 0
                    base_health -= current_enemy_random_damage
                    print(f"\n{current_enemy_name} attacks for {current_enemy_random_damage} damage.")
                    print(f"Your Health: {base_health}")
                    if base_health <= 0:
                        print("\nYou have been defeated.")
                        game_state = False
                        break
            else:
                print("\nHeal unavailable: limit reached or health is already full.")
        elif action_input == "run":
            run_chance = random.random()
            if  run_chance <= 0.6:
                print("\nYou escaped the enemy.")
                enemies_escaped += 1
                escaped_final_battle = True
                break
            else:
                print("\nEscape failed.")
                current_enemy_random_damage = random.randint(current_enemy_min_damage,current_enemy_max_damage)

                if class_chosen_name == "Rogue":
                    rogue_evade_chance = random.random()
                    if rogue_evade_chance <= 0.25:
                        print(f"\nRogue passive activated: you evaded the {current_enemy_name}'s attack.")
                    else:
                        base_health -= current_enemy_random_damage
                        print(f"\n{current_enemy_name} attacks for {current_enemy_random_damage} damage.")
                        print(f"Your Health: {base_health}")
                        if base_health <= 0:
                            print("\nYou have been defeated.")
                            game_state = False
                            break
                else:
                    if class_chosen_name == "Warrior":
                        current_enemy_random_damage -= 5
                        if current_enemy_random_damage < 0:
                            current_enemy_random_damage = 0
                    base_health -= current_enemy_random_damage
                    print(f"\n{current_enemy_name} attacks for {current_enemy_random_damage} damage.")
                    print(f"Your Health: {base_health}")
                    if base_health <= 0:
                        print("\nYou have been defeated.")
                        game_state = False
                        break
        else:
            print("\nInvalid action. Choose attack, defend, heal, or run.")

    if game_state == True:
        rooms_completed += 1

if gold <= 99:
    final_rank = "Survivor"
elif gold <= 249:
    final_rank = "Adventurer"
elif gold <= 449:
    final_rank = "Treasure Hunter"
else:
    final_rank = "Dungeon Master"

if game_state == True and base_health > 0 and rooms_completed >= 5 and escaped_final_battle == False:
    final_result = "Victory"
elif escaped_final_battle == True:
    final_result = "Escaped"
else:
    final_result = "Defeat"

remaining_health = base_health
if remaining_health < 0:
    remaining_health = 0

print(f"\n{line}")
print("FINAL SUMMARY")
print(f"{line}")
print(f"Player Name: {username}")
print(f"Selected Class: {class_chosen_name}")
print(f"Rooms Completed: {rooms_completed}/5")
print(f"Enemies Defeated: {enemies_defeated}")
print(f"Enemies Escaped From: {enemies_escaped}")

if len(treasures_collected) > 0:
    print("Treasures Collected:")
    for treasure_item in treasures_collected:
        print(f"- {treasure_item}")
else:
    print("Treasures Collected: None")

print(f"Final Weapon: {weapon_name}")
print(f"Remaining Health: {remaining_health}")
print(f"Total Gold: {gold}")
print(f"Final Rank: {final_rank}")
print(f"Final Result: {final_result}")
print(f"{line}\n")

