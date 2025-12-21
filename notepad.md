# Tile Mechanics
- **FLOOR**: Standard traversable. Stops sliding movement.
- **WALL**: Impassable. Stops sliding movement.
- **ICE**: Sliding movement. Entering an ICE tile causes sliding in that direction until hitting a WALL, Object, or FLOOR tile.
- **LADDER**: Warp point.
- **NPC/Item Sprites**: Act as walls and stop sliding movement.

# Mahogany Gym (2_2) - COMPLETED
- **Leader:** Pryce defeated (Turn 8583).
- **Reward:** Glacier Badge, TM16 (Icy Wind).
- **Trainer Data:** All trainers defeated.

# Strategy (HOW)
1. Exit Mahogany Gym.
2. Check for plot updates (Radio Tower/Professor Elm).
3. Travel to Blackthorn City via Route 44 (East of Mahogany) and Ice Path.

# Lessons Learned
- Whirlpool requires Glacier Badge to use out of battle.
- `switch_pokemon_v1` and `battle_move_selector` are designed for specific battle menu states. Do not use in overworld menus.
- Sliding on ice: Row 2 sliding is NOT blocked by Row 3 objects. (Pryce at (5, 3) does not block sliding on Row 2).
- Markers for trainers should only be set to 'defeated' after the battle concludes.
- Always verify the trajectory of a slide. It must physically enter the tile of an object to be stopped by it.
- Stat drops (like Growl) reset upon switching or end of battle.

# Goldenrod Radio Tower Crisis
- Team Rocket has taken over the Radio Tower.
- Goal: Clear the tower and defeat the Rocket Executives.
- Strategy: Fly to Goldenrod, heal, and enter the tower.