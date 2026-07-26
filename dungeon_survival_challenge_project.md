# Dungeon Survival Challenge

## Project Overview

You enter a dungeon containing **five rooms**. Each room has a randomly selected enemy, reward, or special event.

Your objective is to:

- Survive all five rooms
- Defeat enemies
- Collect treasure
- Earn as much gold as possible

---

## Player Classes

The player must select one class before entering the dungeon.

| Class | Health | Minimum Damage | Maximum Damage | Special Ability |
|---|---:|---:|---:|---|
| Warrior | 140 | 18 | 30 | Reduces enemy damage by 5 |
| Mage | 90 | 25 | 42 | Has a 25% chance to deal double damage |
| Rogue | 110 | 20 | 35 | Has a 25% chance to avoid an enemy attack |

---

## Dungeon Rooms

The dungeon contains five rooms:

1. Forgotten Hall
2. Spider Nest
3. Underground Prison
4. Treasure Chamber
5. Dragon's Lair

### Room Rules

- The player must visit all five rooms.
- The room order must be random.
- A room cannot be repeated during the same game.

---

## Enemies

| Enemy | Health | Minimum Damage | Maximum Damage | Gold Reward |
|---|---:|---:|---:|---:|
| Giant Rat | 35 | 4 | 9 | 15 |
| Goblin | 55 | 7 | 14 | 30 |
| Skeleton | 75 | 10 | 18 | 50 |
| Orc | 105 | 14 | 25 | 80 |
| Dark Knight | 135 | 18 | 32 | 120 |
| Dragon | 200 | 25 | 45 | 250 |

### Enemy Rules

- Enemies should be selected randomly.
- An enemy must not appear more than once during the same game.
- The Dragon can appear only in the fifth room.

---

## Room Events

Every room should randomly contain one of the following events:

- Enemy encounter
- Treasure chest
- Healing fountain
- Trap
- Empty room

### Event Probabilities

| Event | Chance |
|---|---:|
| Enemy encounter | 50% |
| Treasure chest | 20% |
| Healing fountain | 10% |
| Trap | 15% |
| Empty room | 5% |

---

## Battle Actions

During an enemy encounter, the player must choose one action:

- Attack
- Defend
- Heal
- Run

### Attack

- Damage should be randomly generated between the player's minimum and maximum damage.
- The player's weapon bonus is added to the attack.
- Every attack has a 20% chance of becoming a critical attack.
- A critical attack deals double damage.

### Defend

- The player does not attack during that round.
- The next enemy attack is reduced by 50%.

### Heal

- The player restores a random amount between 15 and 30 health.
- The player can heal only three times during the entire dungeon.
- The player's health cannot exceed the class's original maximum health.
- The enemy still attacks after the player heals.

### Run

- There is a 60% chance of escaping successfully.
- There is a 40% chance of failing to escape.
- If the escape attempt fails, the enemy attacks immediately.
- The player receives no reward when escaping from an enemy.

---

## Character Abilities

### Warrior

- Reduces every enemy attack by 5 damage.
- Damage cannot become lower than zero.

### Mage

- Has a 25% chance of dealing double damage.
- Do not apply the normal critical attack and the Mage's special double-damage ability at the same time.

### Rogue

- Has a 25% chance of completely avoiding an enemy attack.
- Has a separate 30% chance of avoiding traps.

---

## Starting Weapons

The player receives one random starting weapon.

| Weapon | Bonus Damage |
|---|---:|
| Iron Sword | 4 |
| Steel Axe | 7 |
| Magic Staff | 9 |
| Shadow Dagger | 6 |

---

## Upgraded Weapons

After defeating the third enemy, there is a 40% chance of receiving one upgraded weapon.

| Weapon | Bonus Damage |
|---|---:|
| Fire Sword | 12 |
| Ice Staff | 14 |
| Dragon Axe | 16 |

### Upgrade Rules

- Only one upgraded weapon can be received.
- The upgraded weapon replaces the starting weapon.
- The upgrade opportunity happens only after the third enemy is defeated.

---

## Treasure Chests

When the player enters a treasure-chest room, one treasure is selected randomly.

| Treasure | Gold Value |
|---|---:|
| Bag of Coins | 30 |
| Silver Cup | 60 |
| Golden Crown | 120 |
| Ancient Gem | 200 |
| Empty Chest | 0 |

### Treasure Rules

- A treasure should be selected randomly.
- The same valuable treasure should not appear twice in one game.
- The Empty Chest gives no gold.
- Every collected treasure should be recorded for the final summary.

---

## Healing Fountain

When the player finds a healing fountain:

- Restore a random amount between 20 and 45 health.
- The player's health cannot exceed their original maximum health.
- Using a healing fountain does not reduce the player's three battle-healing uses.

---

## Traps

| Trap | Minimum Damage | Maximum Damage |
|---|---:|---:|
| Falling Rocks | 10 | 20 |
| Poison Darts | 15 | 25 |
| Fire Trap | 20 | 35 |
| Broken Floor | 25 | 40 |

### Trap Rules

- The trap should be selected randomly.
- Trap damage should be randomly generated between its minimum and maximum damage.
- The Rogue has a 30% chance of avoiding the trap completely.
- Other classes always receive the trap damage.
- The game ends if trap damage reduces the player's health to zero or below.

---

## Empty Room

When the player enters an empty room:

- No enemy appears.
- No treasure is awarded.
- No health is restored.
- The player continues to the next room.

---

## Dungeon Progression

The dungeon contains exactly five rooms.

For every room, display:

- Room number
- Room name
- Room event
- Player's current health
- Current gold
- Current weapon
- Remaining battle-healing uses

### Progression Rules

- Complete the rooms in their randomly selected order.
- Stop the game immediately if the player's health reaches zero or below.
- Do not continue an enemy battle after the enemy has been defeated.
- Do not continue the dungeon after the player has been defeated.
- The fifth room must allow the Dragon to appear.
- Record the number of completed rooms.

---

## Enemy Battle Result

After every battle:

- If the enemy's health reaches zero or below, the enemy is defeated.
- The player receives the enemy's gold reward after defeating it.
- If the player's health reaches zero or below, the player is defeated.
- If the player escapes, the room ends without a reward.
- Record whether the enemy was defeated or escaped from.

---

## Winning and Losing Conditions

### Victory

The player wins by surviving all five rooms.

### Defeat

The player loses when their health reaches zero or below.

---

## Final Ranks

The player's final rank depends on the total gold collected.

| Total Gold | Rank |
|---:|---|
| 0–99 | Survivor |
| 100–249 | Adventurer |
| 250–449 | Treasure Hunter |
| 450 or more | Dungeon Master |

---

## Final Summary

At the end of the game, display:

- Player name
- Selected class
- Rooms completed
- Enemies defeated
- Enemies escaped from
- Treasures collected
- Final weapon
- Remaining health
- Total gold
- Final rank
- Final result: Victory or Defeat

---

## Invalid Situations to Handle

The program should detect and handle:

- Invalid class selection
- Invalid battle action
- Attempting to heal after all three healing uses are consumed
- Attempting to continue a battle after the enemy is defeated
- Attempting to continue the game after the player is defeated
- Player health exceeding maximum health
- Repeating an enemy
- Repeating a room
- Giving the player a second upgraded weapon
- Allowing the Dragon to appear before the fifth room

---

## Python Concepts to Use

Build the project using:

- Variables
- User input
- `if`, `elif`, and `else`
- Nested conditions
- Multiple independent `if` statements
- `and`, `or`, `in`, and `not in`
- Lists
- Nested lists
- Random number generation
- Random selection
- `random.sample()`
- `range()`
- `for` loops

---

## Main Project Requirements

Your completed project should include:

- Three player classes
- Five dungeon rooms
- Six enemies
- Random room order without repetition
- Random enemies without repetition
- Five possible room events
- Event probabilities
- Four battle actions
- Class-specific abilities
- Critical attacks
- Limited healing
- Starting and upgraded weapons
- Treasure rewards
- Healing fountains
- Random traps
- Gold and ranking systems
- A final game summar
- Victory, defeat, and escape outcomes
- Invalid-input handling
