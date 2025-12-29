# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Warp tile. Falling through takes you to the floor below.
- LADDER: Warp tile.
- ICE: Slippery movement.
- BOULDER BRIDGES: Boulders in pits act as passable FLOOR on the floor below.
- Strength: Must be re-activated after falling through a pit or changing maps.

# Physically Tested Tiles (2F)
- WALL confirmed: (2,0), (3,0), (5,0), (6,0), (7,0), (8,0), (4,1), (4,2)-(4,7), (6,4), (8,8), (8,9), (4,11).
- Passable (Boulder Pushes): (5,1)->(6,1), (7,1)->(8,1), (8,1)->(9,1).

# Blackthorn Gym Layout & Boulders
- 2F Boulders (Initial): Boulder 6 (3,3), Boulder 7 (6,1), Boulder 8 (8,14).
- Boulders reset at Turn 29858.
- 2F Pits: Pit (2,5), Pit (8,3), Pit (8,7).

# Strategy: Gym Leader Clair
- Lead GNEISS (Lv45) vs Dragonairs (Earthquake).
- Vs Kingdra: Calcifer (Smokescreen) -> GNEISS (Defense Curl + Rollout).

# Boulder Puzzle Solve Plan
- Start Turn: 29800. Decisive Phase Start: 29851.
- Reset Turn: 29858 (Boulders at initial positions).
- Current Hypothesis: (1,0) or (0,0) is a fake wall.
- Step 1: Activate Strength (COMPLETED).
- Step 2: Test (1,0) and (0,0) for passability.
- Step 3: Detour to (5,2) and test (6,2), (6,3).
- Step 4: Execute push sequence.