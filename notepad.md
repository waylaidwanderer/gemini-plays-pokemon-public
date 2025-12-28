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
- STRENGTH MECHANICS: Strength must be re-activated after every floor transition or battle. Verified. (Turn 28568).

# B1F Boulder Puzzle (All Pits Pending)
- Start Turn: 28207.
- Current Attempt Start: 28546.
- Pit 1: (11, 2)
- Pit 2: (4, 7)
- Pit 3: (5, 12)
- Pit 4: (12, 13)

## Boulder 1 (ID 1) -> Pit 1 (11, 2)
1. Detour to (11, 8) via B2F transit. [CURRENT]
   - Map Discovery: B1F is partitioned. The NE section (ladder 17,3) is isolated from the rest.
   - Transit Route: B1F (17,3) -> B2F (17,1) -> B2F (9,11) -> B1F (3,15) -> B1F (11,8).
   - WARNING: Do NOT push Boulder 1 DOWN to (11, 8) from Row 6; it must be pushed UP from Row 8.
3. Push Boulder 1 UP to (11, 5).
4. Move to (12, 5) and push Boulder 1 LEFT to (10, 5).
5. Move to (10, 6) and push Boulder 1 UP to (10, 1).
6. Move to (9, 1) and push Boulder 1 RIGHT to (11, 1).
7. Move to (11, 0) and push Boulder 1 DOWN into Pit 1.

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
- Wild battles: Prioritize escaping unless it's a Swinub or Jynx.
- Menu Mechanics: In the POKéMON menu, the 'A' button sub-menu "SWITCH" option initiates the reordering process. Verified.
- Verification: Game State warps at (11, 2), (4, 7), (5, 12), and (12, 13) indicate all 4 pits are currently UNFILLED. Verified.
- Boulders: Leaving the floor via ladder or pit RESETS all boulders. Verified.
- Catch List: Swinub (Common), Jynx (Rare). Use Sleep Powder/Hypnosis.