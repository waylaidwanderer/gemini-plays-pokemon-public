# Tile Mechanics
- **FLOOR**: Standard traversable. Stops sliding movement.
- **WALL**: Impassable. Stops sliding movement.
- **ICE**: Sliding movement. Entering an ICE tile causes the player to slide in that direction until they hit a WALL, an Object, or a non-ICE tile.
- **LADDER**: Warp point.
- **NPC/Item Sprites**: All sprites act as walls and stop sliding movement.

# Movesets
- **Dewgong**: Growl.
- **Swinub**: Endure.
- **Jynx**: Doubleslap.

# Mahogany Gym (2_2) - Glacier Badge
- **Leader:** Pryce (Ice-type) at (5, 3).
- **Started:** Turn 8460.
- **Strategy:** Lead with Calcifer (Typhlosion) for Fire-type advantage.
- **Trainer Data:**
  - Skier Clarissa (2_2, 9, 17): Dewgong Lv28. [DEFEATED]
  - Boarder Brad (2_2, 5, 9): Swinub Lv26. [DEFEATED]
  - Skier Roxanne (2_2, 4, 6): Jynx Lv28. [DEFEATED]
  - Boarder Ronald (2_2, 2, 17): Seel Lv24, Dewgong Lv25. [IN BATTLE]
  - Rocker (2_2, 2, 4): Unseen.

# Navigation Plan
- **Path to Rocker (2, 4):**
  1. Reach (6, 16) [FLOOR].
  2. Move Up -> Slide to (6, 13) [FLOOR].
  3. Move Left -> Slide to (3, 13) [FLOOR].
  4. Move Up -> Slide to (3, 4) [FLOOR].
  5. Move Left to Rocker at (2, 4).
- **Path to Pryce (5, 3):**
  1. Reach (9, 16) [FLOOR].
  2. Move Up -> Slide to (9, 10) [FLOOR].
  3. Move Left -> Slide to (5, 10) [FLOOR].
  4. Move Up -> Slide to (5, 4) [FLOOR].
  5. Face Up and talk to Pryce at (5, 3).

# Lessons Learned
- Whirlpool requires Glacier Badge to use out of battle.
- `switch_pokemon_v1` and `battle_move_selector` are designed for specific battle menu states. Do not use in overworld menus.
- Sliding on ice: Objects only block sliding if the player's trajectory physically enters the object's tile. Row 2 sliding is NOT blocked by Row 3 objects.