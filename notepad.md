# Goldenrod Radio Tower Crisis (Started Turn 8588)
- **Strategy (HOW)**:
    1. Perform a floor-by-floor sweep (1F to 5F).
    2. Identify and defeat all Rocket Grunts and Executives.
    3. Locate the Director (rumored to be on 5F or in the basement).
    4. Obtain the Radio Card by passing the quiz on 1F.
    5. Use `battle_strategist_v2` for high-stakes Executive battles.

# Tile Mechanics
- **FLOOR**: Standard traversable.
- **WALL**: Impassable.
- **COUNTER**: Impassable. Interaction must be done from an adjacent tile facing the counter.
- **WARP_CARPET_DOWN**: Triggers map transition when walked onto from above.
- **ICE**: Sliding movement. Entering an ICE tile causes sliding in that direction until hitting a WALL, Object, or FLOOR tile.
- **LADDER**: Warp point.
- **NPC/Item Sprites**: Act as walls and stop sliding movement.

# Lessons Learned
- **Counter Interaction**: You cannot walk through counters. You must face them from an adjacent tile to interact with NPCs behind them.
- **Whirlpool**: Requires Glacier Badge to use out of battle.
- **Battle Menus**: `switch_pokemon_v1` and `battle_move_selector` are ONLY for specific battle menu states.
- **Ice Trajectory**: Always verify the trajectory of a slide. It must physically enter the tile of an object to be stopped by it.
- **Fly Map (Goldenrod)**: From New Bark Town, sequence is: Left (to Cherrygrove), Left (to Violet), Up (to Route 31), Left (to Goldenrod). Note: Menu may be sticky; use discrete presses. (Turn 8596-8604 failure analysis)

# Mahogany Gym (2_2) - COMPLETED
- **Leader:** Pryce defeated (Turn 8583).
- **Reward:** Glacier Badge, TM16 (Icy Wind).

# Future Strategy
- After resolving the Radio Tower crisis, travel to Blackthorn City via Route 44 (East of Mahogany) and the Ice Path.
- Prepare for the 8th Gym Badge.