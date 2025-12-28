## Battle Strategy (Blackthorn Gym)
- Leader Clair: Dragonair Lv37 x3, Kingdra Lv40.
- Typhlosion (Lv45) with Thunderpunch is key for Kingdra.
- Graveler (Lv44) with Earthquake for Dragonairs.
- Fodder: Gloom, Pidgey, Krabby, Gastly (Lv10-21) to heal/switch.
- Prep: Catch Swinub/Jynx in Ice Path for Ice-type moves.

# Tile Mechanics
- FLOOR: Walkable. Verified.
- WALL: Impassable. Verified.
- WATER: Needs Surf (HM03). Verified.
- ICE: Sliding mechanic. Verified. You slide until you hit a wall, an object, or a non-ice tile.
- PIT: Warp to B2F. Verified.
- BOULDER: Pushable with Strength (HM04). Verified.

# B1F Boulder Puzzle
- Start Turn: 28207.
- Reset Turn: 28476 (Fell through Pit 1).
- Pit 1 (11, 2): Pending Boulder 1 (ID 1).
- Pit 2 (4, 7): Pending Boulder 2 (ID 2).
- Pit 3 (5, 12): COMPLETED.
- Pit 4 (12, 13): COMPLETED.

## Boulder 1 Sequence (ID 1)
- Starting at (11, 7).
1. Move to (11, 8). [DONE]
2. Activate Strength. [DONE]
3. Push Up to (11, 5). [DONE]
4. Move to (12, 5). [DONE]
5. Push Left to (10, 5). [DONE]
6. Move to (10, 6). [DONE]
7. Push Up to (10, 1). [DONE - T28496]
8. Move to (9, 1). [NEXT]
8. Move to (9, 1).
9. Push Right to (11, 1).
10. Move to (11, 0).
11. Push Down to (11, 2). [PIT]

## Boulder 2 Sequence (ID 2)
- Starting at (7, 8).
1. Move to (8, 8).
2. Push Left to (5, 8).
3. Move to (5, 9).
4. Push Up to (5, 6).
5. Move to (6, 6).
6. Push Left to (4, 6).
7. Move to (4, 5).
8. Push Down to (4, 7). [PIT]

# Party Management
- Lead: KIMCHI (Lv21)
- Note: Party swap to Calcifer abandoned at Turn 28473 to prioritize puzzle.

# Lessons Learned
- Falling through a PIT on B1F resets the entire floor's boulder puzzle.
- Be extremely cautious when moving near (11, 2), (4, 7), (5, 12), and (12, 13) on B1F.
- Optimization Trap: Do not spend more turns on a "safety" optimization (like party swapping) than the optimization actually saves.
- Verification: Always verify boulder coordinates in Game State before updating notepad "Current Status".