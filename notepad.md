# Tile Mechanics (Global)
- FLOOR: Traversable. Standard ground.
- WALL: Impassable. Includes counters and trees.
- SHUTTER: Dynamic collision. (Solved in 3_54). Impassable when closed.
- LADDER: Warp tile. Used between floors or underground.
- WARP_CARPET_DOWN: Warp tile. Found at exits and in elevators.
- STAIRCASE: Warp tile.
- WATER: Requires Surf to traverse.
- GRASS: May trigger wild encounters.
- unseen: Traversable (optimistic assumption for pathfinding).

# Current Strategy: Stop Team Rocket
- Method: Return to Goldenrod Radio Tower and use the Card Key on 3F.
- Path: Goldenrod Dept Store -> Goldenrod City -> Radio Tower.
- Tactical: Use Card Key on the shutters on 3F to access the upper floors.
- Search Pattern (Radio Tower): Systematically clear each floor from 3F upwards.

# Observations
- Map 3_56: Real Director rescued at (12, 8). Card Key obtained.
- Map 3_56: Internal Walls at Col 5 (Gaps R1-3), Col 8 (Gaps R12-15), Col 15 (Gaps R1-3, 12-13).
- Map 3_55: Dept Store B1F. Connected to Warehouse via (17, 2).

# Trainer Rosters (Recent)
- Rival Malice: Sneasel Lv30, Golbat Lv30, Magnemite Lv28, Haunter Lv30, Typhlosion Lv32.
- Burglar Eddie: Growlithe Lv26, Koffing Lv24.
- Rocket Grunt (M): Raticate Lv24, Raticate Lv24.
- Rocket Grunt (M): Grimer Lv23, Muk Lv25.
- Rocket Grunt (M): Koffing Lv23, Koffing Lv23, Magmar Lv25.
- Rocket Girl: Gloom Lv25, Gloom Lv25.
- Burglar Duncan: Koffing Lv23, Koffing Lv23, Magmar Lv25.
- Rocket Grunt (M): Koffing Lv24.
- Rocket Grunt (M): Rattata Lv24, Rattata Lv24.

# PC Storage (Box 1)
1. ROCKY (ONIX): Lv6 (M)
2. EGG (CLEFFA): Lv5 (F)
3. XFDW (MEOWTH): Lv16 (M)
4. FRITTATA (TOGEPI): Lv5 (M)
5. SHUCKIE (SHUCKLE): Lv15 (F)

# Findings
- Card Key obtained from the real Director at (12, 8) in Map 3_56. (Turn 11056)
- Found TM35 Sleep Talk at (13, 9) in Map 3_56. (Turn 11058)
- Found Max Ether at (18, 15) in Map 3_56. (Turn 11060)
- Found Amulet Coin at (14, 2) in Map 3_55. (Turn 11039)
- Found Ultra Ball at (2, 1) in Map 3_56. (Turn 11006)
- Found Full Heal at (14, 9) in Map 3_54. (Turn 10981)

# Radio Tower Mission Plan
1. Defeat Executive: Reach the top floor and stop the broadcast.
- Status: Card Key used on 3F. Currently clearing 3F.

# Shutter Puzzle (Radio Tower 3F)
- Observation: Interacting with Card Key Slot at (14, 2) from (13, 2) facing Right produced no result.
- Hypothesis: Many switches/slots in this game require interaction from BELOW, facing UP.
- Test: Stand at (14, 3), face UP, and press A. (Attempt 1: Success! Shutter opened)

# Radio Tower Upper Floors
- Access: Card Key used at (14, 2) on 3F.
- Goal: Reach 5F and stop the broadcast.
- Note: Stairs at (17, 0) on 3F lead to the restricted area.