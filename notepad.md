# Tile Mechanics (Global)
- FLOOR: Traversable. Standard ground.
- WALL: Impassable. Includes counters, bookshelves, and decorative walls.
- SHUTTER: Dynamic collision. (Solved in 3_54). Impassable when closed.
- LADDER: Warp tile. Used between floors or underground.
- WARP_CARPET_DOWN: Warp tile. Found at exits and in elevators.
- STAIRCASE: Warp tile.
- WATER: Requires Surf to traverse. (HM03)
- GRASS: May trigger wild encounters.
- MART_SHELF: Impassable. Acts as WALL.
- COUNTER: Impassable. Acts as WALL. Interact with NPCs behind counters from an adjacent tile.
- ELEVATOR: Warp tile (2, 0).
- VENDING MACHINE: Interaction point. Stand below and press A to buy drinks.
- CUT_TREE: Obstacle. Can be cleared with HM01 CUT.

# Ecruteak Tower Lore
- Original state: Two nine-tier towers.
- Brass Tower: Purpose was to awaken Pokémon. Roost of an immense, silver-colored Pokémon.
- Tin Tower: Purpose was for Pokémon to rest.
- The Great Fire: 150 years ago, lightning struck the Brass Tower. It burned for 3 days until a sudden downpour extinguished it. The ruins are now known as the Burned Tower.

# Wise Trio Battle Summary
- Defeated Sages Gaku, Masa, and Koji. (Start #11502, End #11562)
- Proved worthiness to enter the Tin Tower.
- Learned the history of the Burned and Tin Towers.

# Observations (Radio Tower Takeover - COMPLETED)
- Director rescued, CLEAR BELL obtained.
- Radio Tower 5F: Rocket Executive defeated. Ultra Ball found at (8, 5).
- Radio Tower 4F: Rocket Executive defeated.
- Radio Tower 3F: Rocket Grunt defeated. Shutters unlocked with Card Key.
- Radio Tower 2F: Rocket Grunts and Girl defeated.
- Radio Tower 1F: Base of operations.

# Trainer Rosters (Recent)
- Rival Malice: Sneasel Lv30, Golbat Lv30, Magnemite Lv28, Haunter Lv30, Typhlosion Lv32.
- Rocket Executive (5F): Houndour Lv33, Koffing Lv33, Houndoom Lv35.
- Rocket Executive (5F - Near stairs): Arbok Lv32, Vileplume Lv32, Murkrow Lv32.
- Rocket Executive (4F): Golbat Lv36.
- Sage GAKU: Noctowl Lv32 (Hypnosis, Foresight, Peck, Reflect), Flareon Lv32 (Fainted).
- Sage MASA: Noctowl Lv32 (Fainted), Jolteon Lv32 (Fainted).
- Sage KOJI: Noctowl Lv32 (Fainted), Vaporeon Lv32 (Fainted).

# PC Storage (Box 1)
1. ROCKY (ONIX): Lv6 (M)
2. EGG (CLEFFA): Lv5 (F)
3. XFDW (MEOWTH): Lv16 (M)
4. FRITTATA (TOGEPI): Lv5 (M)
5. SHUCKIE (SHUCKLE): Lv15 (F)

# Findings
- Goldenrod Dept Store 5F: Receptionist (7, 5) gives TM27 (Return) if friendship is high.
- Clerk (8, 5) sells TM41, TM48, TM33 for 3000, TM02 for 2000, TM08 for 1000.
- Goldenrod Dept Store 4F: Clerk (13, 5) sells Vitamins for 9800.
- Goldenrod Dept Store 3F: Clerk (6, 1) sells battle items.
- Goldenrod Dept Store 2F Clerk (13, 5): Healing items.
- Goldenrod Dept Store 2F Clerk (13, 6): Basic supplies.

# General Lessons
- Lesson: Interact with switches, slots, and interactive objects from BELOW (facing UP) whenever possible.
- Lesson: Elevator buttons may require a specific trigger or are non-functional in this state. Use stairs.

# Error Log
- Turn #11355, #11370: Attempted to interact with elevator buttons on 5F and 4F. No text appeared.
- Turn #11489, #11586: Swapping lead failed due to truncated button sequence or cursor persistence. Refined custom tool with comprehensive resets.
- Turn #11578-11580: Pressed A repeatedly in menu. Lesson: Use B to clear messages and exit menus efficiently.

# Tin Tower Navigation
- Entrance building at (18, 11) leads to Wise Trios Room.
- Wise Trios Room ladder at (17, 3) leads to Wise Trios Room upper level.
- Warp at (7, 4) in Wise Trios Room leads to Tin Tower 1F (20, 2).
- Tin Tower 1F (20, 2) and (20, 3) are exits back to Ecruteak City top center.

# Error Log
- Turn #11594: swap_pokemon_v1 failed significantly, opening Pokegear and Pokedex. Manual swap required.
- Turn #11594: Hallucination warning at (31, 5). Moving to break loop.