# Tile Mechanics (Global)
- FLOOR: Traversable. Standard collision.
- WALL: Impassable. Silver blocks or solid boundaries.
- PIT: Warp tile for player (falls to 1F). Destination for boulders to form bridges on 1F.
- LADDER: Warp tile. Transfers between floors.
- ICE: Slippery movement.
- BOULDER BRIDGES: Boulders in pits on 2F act as passable FLOOR on 1F.
- Strength: Must be re-activated after falling through a pit or changing maps.

# Blackthorn Gym Layout & Boulders
- 1F Mechanics: Boulders must be dropped into specific pits on 2F to bridge gaps on 1F.
- 2F Pits -> 1F Landing Spots:
  - Pit (2, 5) -> Landing (2, 6)
  - Pit (8, 3) -> Landing (7, 6)
  - Pit (8, 7) -> Landing (7, 7)
- 2F Boulders (Initial): Boulder 6 (3, 3), Boulder 7 (6, 1), Boulder 8 (8, 14).

# Strategy: Gym Leader Clair
- Lead GNEISS (Lv45) vs Dragonairs (Earthquake).
- Vs Kingdra: Calcifer (Smokescreen) -> GNEISS (Defense Curl + Rollout).

# Boulder Puzzle Strategy
- Goal: Push all three boulders into pits on 2F to create a path to Gym Leader Clair on 1F.
- Current Status: At (3, 6) on 2F. Strength activation in progress.
- Plan: 
  1. Activate Strength: Start -> Up x5 (to POKEDEX) -> Down (to POKEMON) -> A -> Down x4 (to GNEISS) -> A -> Down x2 (to STRENGTH) -> A -> 3 Bs (exit).
  2. Push Boulder 6 (3, 3) down to (3, 13).
  3. Push Boulder 6 (3, 13) left to (1, 13).
  4. Push Boulder 6 (1, 13) up to (1, 5).
  5. Push Boulder 6 (1, 5) right to (2, 5) PIT.
- Start Turn: 29800. Decisive Phase Start: Turn 29911. Puzzle Start: Turn 29931.
- Lessons: Resetting by ladder works. Strength must be reactivated after map change. Column 4 is a wall from row 2-12. Detour through row 13 and column 1 is the only way for B6.
- Failed Strength Activation Attempts: 7 (Succeeded on Turn 30000).
- Discovery: Interacting with a boulder (pressing A while facing it) triggers a prompt to use Strength.
- Turn 30000 Strategy:
  1. Strength is ACTIVE.
  2. Push Boulder 6 (3, 4) down to (3, 13).
- Boulder 6 Detour Plan:
  1. Push B6 to (3, 13).
  2. Navigate around the central wall via Row 1 to reach (2, 13) or (4, 13).
  3. Push B6 into PIT (2, 5).
- Boulder 7 Plan: Push into PIT (8, 3).
- Boulder 8 Plan: Push into PIT (8, 7).
- Verification: Column 4 (WALL) blocks direct access from the right. Column 2 (WALL) from row 8-12 blocks access from the left. Only Row 13 and Row 1 are open for cross-gym navigation.