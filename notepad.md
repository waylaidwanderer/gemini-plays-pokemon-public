# Radio Tower Crisis (Started Turn 8588)
- **Primary Objective**: Clear Team Rocket from the tower and restore normal broadcasts.
- **Progress**: 1F, 2F, and 3F cleared. 4F sweep in progress.
- **Strategy (HOW)**:
    1. Floor-by-floor sweep (1F -> 5F).
    2. Defeat all Rocket Grunts and Executives.
    3. Find the Director (5F/Basement).
    4. Pass the quiz on 1F for the Radio Card.
    5. POST-SWEEP: Re-verify 1F for any missed trainers.
- **Executive Battles**: Use `battle_strategist_v2`.

# Battle Logs
- Red Gyarados (Lake of Rage): Defeated.
- Radio Tower 1F: Rocket Grunt (Raticate Lv24) - Defeated.
- Radio Tower 2F:
    - Rocket Girl (10, 3): Arbok Lv26 - Defeated.
    - Rocket Grunt (8, 4): 4 Rattatas (Lv21-23) - Defeated.
    - Rocket Grunt (4, 1): 2 Zubats (Lv26) - Defeated.
    - Rocket Grunt (1, 4): Grimer Lv23 x2, Muk Lv25 - Defeated.
- Radio Tower 3F:
    - Rocket Grunt (6, 4): Weezing Lv26 - Defeated.
    - Rocket Grunt (5, 1): Koffing, Grimer, Zubat, Rattata (Lv23) - Defeated.
    - Scientist Marc (9, 3): Magnemite Lv27 x2 - Defeated.
- Radio Tower 4F:
    - Scientist Rich (4, 2): Porygon Lv30 (In progress).

# Tile Mechanics
- **FLOOR**: Standard traversable.
- **WALL**: Impassable.
- **COUNTER**: Impassable. Interact from adjacent tile facing the counter.
- **WARP_CARPET_DOWN**: Map transition.
- **ICE**: Sliding movement until hitting an obstacle.
- **LADDER/STAIRS**: Warp points.
- **NPC/Item Sprites**: Walls; stop sliding.

# Completed Badges
- Zephyr, Hive, Plain, Fog, Storm, Mineral, Glacier.

# Navigation Notes
- **Counter Interaction**: Face the counter, not the NPC.
- **Fly Map (Goldenrod)**: From New Bark Town, 4 Ups and 6 Lefts. Menu is "sticky"; use discrete presses or `fly_to_v1`.
- **PC Storage**: SHUCKIE (Lv15), ROCKY (Lv6), EGG (Lv5), XFDW (Lv16), FRITTATA (Lv5).

# Strategic Insights
- **Turn 8775**: Fixed `battle_move_selector_v2` logic. Pruned transient turn logs. 4F sweep in progress. Defeating Scientist Rich. Foundational assumption: Progress is achieved by defeating Rockets floor-by-floor to reach the Director.
- **Director Info**: The Director is being held on the 5th floor. He has the ability to open the locked boss's door.
- **Card Key Slot**: Located at (14, 2) on 3F. Likely requires the Card Key.