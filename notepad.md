# Tile Mechanics
- **FLOOR**: Standard traversable. Stops sliding movement.
- **WALL**: Impassable. Stops sliding movement.
- **ICE**: Sliding movement. Entering an ICE tile causes sliding in that direction until hitting a WALL, Object, or FLOOR tile.
- **LADDER**: Warp point.
- **NPC/Item Sprites**: Act as walls and stop sliding movement.

# Mahogany Gym (2_2) - Glacier Badge
- **Leader:** Pryce (Ice-type) at (5, 3).
- **Started:** Turn 8460.
- **Strategy:** Lead with Calcifer (Typhlosion) for Fire-type advantage.
- **Trainer Data:**
  - Skier Clarissa (2_2, 9, 17): Dewgong Lv28. [DEFEATED]
  - Boarder Brad (2_2, 5, 9): Swinub Lv26. [DEFEATED]
  - Skier Roxanne (2_2, 4, 6): Jynx Lv28. [DEFEATED]
  - Boarder Ronald (2_2, 0, 17): Seel Lv24, Dewgong Lv25. [DEFEATED]
  - Rocker (2_2, 2, 4): Unseen.

# Navigation Plan
- **Phase 1: Clear the South-West Corner**
  1. From current position (1, 17), move Right to (2, 17) [FLOOR].
  2. Move Up to (2, 16) [FLOOR].
  3. Move Up to (2, 14) [FLOOR].
  4. Move Up to (2, 10) [FLOOR].
  5. Move Up to (2, 5) [ICE, stops at Rocker at (2, 4)].
  6. Interact with Rocker at (2, 4) and defeat him.
- **Phase 2: Reach Gym Leader Pryce**
  1. From (2, 5), move Right to (6, 5) [FLOOR].
  2. Move Down to (6, 11) [ICE, stops at WALL at (6, 12)].
  3. Move Left to (3, 11) [ICE, stops at WALL at (2, 11)].
  4. Move Up to (3, 4) [ICE, stops at FLOOR at (3, 4)].
  5. Move Right to (5, 4) [ICE, stops at FLOOR at (5, 4)].
  6. Face Up and talk to Pryce at (5, 3).

# Lessons Learned
- Whirlpool requires Glacier Badge to use out of battle.
- `switch_pokemon_v1` and `battle_move_selector` are designed for specific battle menu states. Do not use in overworld menus.
- Sliding on ice: Row 2 sliding is NOT blocked by Row 3 objects. (Pryce at (5, 3) does not block sliding on Row 2).
- Markers for trainers should only be set to 'defeated' after the battle concludes.
- Always verify the trajectory of a slide. It must physically enter the tile of an object to be stopped by it.