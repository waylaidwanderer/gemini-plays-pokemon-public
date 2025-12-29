# Tile Mechanics (Global)
- FLOOR: Traversable. Standard collision.
- WALL: Impassable. Silver blocks or solid boundaries.
- PIT: Warp tile. Falling through takes you to the floor below.
- LADDER: Warp tile. Transfers between floors.
- ICE: Slippery movement. Causes sliding until an obstacle is hit.
- BOULDER BRIDGES: Boulders in pits act as passable FLOOR on the floor below.
- Strength: Must be re-activated after falling through a pit or changing maps.

# Physically Tested Tiles (2F)
- (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (5,0), (6,0), (6,4), (7,0), (8,0): WALL confirmed.
- (3,11) -> (4,11): Blocked by Fran (NPC).
- (5,1) -> (6,1): Passable (pushed boulder).
- (7,1) -> (8,1): Passable (pushed boulder).
- (8,1) -> (9,1): Passable (pushed boulder).

# Blackthorn Gym Layout & Boulders
- 2F Boulders (Current): Boulder 6 (3,3), Boulder 7 (9,1), Boulder 8 (8,14).
- 2F Pits: Pit (2,5), Pit (8,3), Pit (8,7).

# Boulder Puzzle Analysis
- Visual Walls (Unverified):
  - Row 0: (0,0), (1,0), (2,0), (3,0), (4,0), (9,0)
  - Col 6: (6,2), (6,3)
  - Misc: (8,8), (8,9), (7,10), (7,11), (9,16), (2,13)
- Task: Identify "fake" walls blocking boulder solutions.
- Current Turn: 29845.
- Puzzle Start: Turn 29800 (Dec 28 4:00 PM).

# Strategy: Gym Leader Clair
- Lead GNEISS (Lv45) vs Dragonairs (Earthquake).
- Vs Kingdra: Calcifer (Smokescreen) -> GNEISS (Defense Curl + Rollout).