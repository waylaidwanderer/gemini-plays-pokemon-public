# Strategy: Investigate Mahogany Radio Broadcast
- Starting Turn: 7780
- Objective: Locate and shut down the radio transmitter in Team Rocket Base.
- HOW:
    1. Obtain passwords from Grunt (7, 14) and Rocket Girl (21, 7). [DONE]
    2. Find a path to the western section of B3F. [CURRENT]
    3. Unlock the boss's room at (10, 9) using the passwords 'RATICATE TAIL' and 'SLOWPOKETAIL'.
    4. Defeat the boss to get the transmitter room password.
    5. Shut down the transmitter on B2F.

# Global Tile Mechanics
- FLOOR: Verified traversable.
- WALL: Verified impassable.
- WATER: Verified traversable (Surf + HM Badge).
- TALL_GRASS: Verified traversable.
- MART_SHELF: Impassable.
- COUNTER: Impassable (interact from adjacent).
- WARP: Map transition.
- BOOKSHELF: Impassable.
- TABLE: Impassable.

# Party Training Status
- GNEISS (GRAVELER): Lv38 (106/106 HP).
- ICARUS (PIDGEY): Lv16 (43/43 HP).
- Calcifer (TYPHLOSION): Lv36 (113/114 HP).
- KIMCHI (GLOOM): Lv21 (57/57 HP).
- Ravioli (KRABBY): Lv10 (27/27 HP).
- Blarney (SUDOWOODO): Lv20 (60/60 HP).

# Password Log
- Password 1: RATICATE TAIL (from Grunt at 7, 14)
- Password 2: SLOWPOKETAIL (from Rocket Girl at 21, 7)

# Trainer Roster (B3F)
- Scientist Mitch (11,15): Ditto (Lv24). Defeated.
- Rocket Grunt (7,14): Raticate (Lv19). Defeated. Password 1.
- Scientist Ross (23,11): Koffing (Lv22), Koffing (Lv22). Defeated.
- Rocket Girl (21,7): Ekans (Lv18), Gloom (Lv18). Defeated. Password 2.

# Lessons Learned
- Item sprites (POKE_BALL) and COUNTER tiles are impassable. Path to adjacent FLOOR tile to interact.
- Markers are metadata and do NOT have collision.
- Always verify foundation assumptions before pursuing complex strategies.
- The map is divided by a wall at column 15; cross at Row 12 or 13.
- To reach the boss door, go around the Row 11-13 barrier via column 3.
- Failed pathfinding for item at (14, 10) was due to trying to path onto the item tile.