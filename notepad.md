## Battle Strategy (Blackthorn Gym)
- Leader Clair: Dragonair Lv37 x3, Kingdra Lv40.
- Kingdra Strategy: Only weak to Dragon. Use Typhlosion (Lv45) with Thunderpunch and Graveler (Lv44) with Earthquake for consistent neutral damage. Use Max Potion as needed.
- Dragonair Strategy: Weak to Ice. Catch Swinub or Jynx in Ice Path to handle them easily.

## Tile Mechanics
- FLOOR: Walkable. Verified. NOTE: B1F FLOOR tiles do NOT have sliding ice properties.
- WALL: Impassable. Verified.
- WATER: Needs Surf (HM03). Verified.
- ICE: Sliding mechanic. Moving onto an ICE tile causes the player to slide in that direction until hitting a non-ICE tile, a wall, or an object. Verified.
- PIT: Warp to B2F. Verified.
- BOULDER: Pushable with Strength (HM04). Verified.
- RESET MECHANICS: Leaving the floor via ladder or pit resets all boulders to their starting positions. Verified. (Turn 28531).

# B1F Boulder Puzzle (All Pits Pending)
- Start Turn: 28207.
- Current Attempt Start: 28546.
- Pit 1: (11, 2)
- Pit 2: (4, 7)
- Pit 3: (5, 12)
- Pit 4: (12, 13)

## Boulder 1 (ID 1) -> Pit 1 (11, 2)
1. Reset floor via pit at (11, 2). [DONE]
2. Move to (11, 8) via western corridor detour. [CURRENT]
3. Push Up to (11, 5).
4. Move to (12, 5).
5. Push Left to (10, 5).
6. Move to (10, 6).
7. Push Up to (10, 1). (CRITICAL: Do not push to 10,0)
8. Move to (9, 1) via (12, 1) detour.
9. Push Right to (11, 1).
10. Move to (11, 0).
11. Push Down to (11, 2). [PIT]

## Boulder 2 (ID 2) -> Pit 2 (4, 7)
1. Move to (8, 8).
2. Push Left to (5, 8).
3. Move to (5, 9).
4. Push Up to (5, 6).
5. Move to (6, 6).
6. Push Left to (4, 6).
7. Move to (4, 5).
8. Push Down to (4, 7). [PIT]

# Lessons Learned
- Wild battles: Prioritize escaping.
- Menu Mechanics: In the POKéMON menu, the 'A' button sub-menu "SWITCH" option initiates the reordering process (same as the 'Select' button shortcut). To swap two Pokémon, select the first, choose "SWITCH", move to the second, and press 'A'. Verified.
- Verification: Game State warps at (11, 2), (4, 7), (5, 12), and (12, 13) indicate all 4 pits are currently UNFILLED. Verified. (Turn 28531).
- Boulders: Leaving the floor via ladder or pit RESETS all boulders to their starting positions. Verified. (Turn 28535).
- Hypothesis: Strength must be re-activated after every floor transition or battle. To be verified.