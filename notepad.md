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
  - Boarder Ronald (2_2, 2, 17): Seel Lv24, Dewgong Lv25. [DEFEATED]
  - Boarder Douglas (2_2, 2, 4): Shellder Lv24, Cloyster Lv25. [DEFEATED]

# Leader Pryce Battle (Turn 8557)
- Pryce's Roster:
  1. Seel Lv27 (Defeated, Turn 8565)
  2. Dewgong Lv29 (Defeated, Turn 8577)
  3. Piloswine (In Battle, Turn 8577)

# Mahogany Gym Navigation Status
- Current Position: (5, 4) [In Battle].
- Path to Pryce: Completed.

# Lessons Learned
- Whirlpool requires Glacier Badge to use out of battle.
- `switch_pokemon_v1` and `battle_move_selector` are designed for specific battle menu states. Do not use in overworld menus.
- Sliding on ice: Row 2 sliding is NOT blocked by Row 3 objects. (Pryce at (5, 3) does not block sliding on Row 2).
- Markers for trainers should only be set to 'defeated' after the battle concludes.
- Always verify the trajectory of a slide. It must physically enter the tile of an object to be stopped by it.
- Stat drops (like Growl) reset upon switching or end of battle.

# Reflection (Turn 8568)
- Immediate Execution: Handled "Will GEM change POKEMON?" prompt.
- Notepad Hygiene: Removed obsolete Rocket Base notes. Restructured battle data.
- Goal Clarity: Objectives are clear: defeat Pryce for the badge.
- Error Analysis: Corrected turn reporting issues from earlier turns. Calcifer sweep is proving the lead choice correct.