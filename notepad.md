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
- Current Status: At (2, 7) on 2F. Activating Strength. Then testing 'WALL' tiles at (4, 10).
- Plan: 
  1. Activate Strength.
  2. Navigate to (3, 3) and push Boulder 6 -> (2, 3) -> (2, 5).
  3. Push Boulder 7 (6, 1) -> (8, 1) -> (8, 3).
  4. Push Boulder 8 (8, 14) -> (8, 7).
- Start Turn: 29800. Decisive Phase Start: Turn 29911. Puzzle Start: Turn 29931 (Sunday 6:00 PM).
- Lessons: Resetting by ladder works. Strength must be reactivated after map change. Manual pushing is more reliable for the first boulder.