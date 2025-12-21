# Radio Tower Crisis (Started Turn 8588)
- **Primary Objective**: Clear Team Rocket from the tower and restore normal broadcasts.
- **Progress**: 1F cleared of immediate threats. Currently clearing 2F.
- **Strategy (HOW)**:
    1. Floor-by-floor sweep (1F -> 5F).
    2. Defeat all Rocket Grunts and Executives.
    3. Find the Director (5F/Basement).
    4. Pass the quiz on 1F for the Radio Card.
- **Executive Battles**: Use `battle_strategist_v2`.

# Tile Mechanics
- **FLOOR**: Standard traversable.
- **WALL**: Impassable.
- **COUNTER**: Impassable. Interact from adjacent tile facing the counter.
- **WARP_CARPET_DOWN**: Map transition.
- **ICE**: Sliding movement until hitting an obstacle.
- **LADDER/STAIRS**: Warp points.
- **NPC/Item Sprites**: Walls; stop sliding.

# Lessons Learned
- **Counter Interaction**: Face the counter, not the NPC.
- **Whirlpool**: Requires Glacier Badge.
- **Battle Menus**: `switch_pokemon_v1` and `battle_move_selector` are ONLY for battle sub-menus.
- **Fly Map (Goldenrod)**: From New Bark Town, move Left to reach the western side, then Up to Goldenrod. Menu is "sticky"; use discrete presses or `fly_to_v1`.
- **Notepad Edits**: `replace` requires exact character matching. Use `overwrite` for major reorganization.

# Completed Badges
- Zephyr, Hive, Plain, Fog, Storm, Mineral, Glacier.

# Future Strategy
- Travel to Blackthorn City via Route 44 (East of Mahogany) and Ice Path.
- Prepare for the 8th Gym Badge.
- Battle: Rocket Grunt (2F, 8,4). Opponent: 4 Rattatas (Lv21-23). Currently on 3rd. (Turn 8660+)