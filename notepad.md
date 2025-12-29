# Tile Mechanics (Global)
- FLOOR: Traversable. Standard collision.
- WALL: Impassable. Silver blocks or solid boundaries.
- PIT: Warp tile. Falling through takes you to the floor below.
- LADDER: Warp tile. Transfers between floors.
- ICE: Slippery movement. Causes sliding until an obstacle is hit.
- BOULDER BRIDGES: Boulders in pits act as passable FLOOR on the floor below.
- Strength: Must be re-activated after falling through a pit or changing maps.

# Physically Tested Tiles (2F)
- (4,2)-(4,7), (5,0), (6,0), (6,4), (7,0), (8,0), (8,8), (8,9): WALL confirmed.
- (3,11) -> (4,11): Blocked by Fran (NPC).
- (5,1) -> (6,1): Passable (pushed boulder).
- (7,1) -> (8,1): Passable (pushed boulder).
- (8,1) -> (9,1): Passable (pushed boulder).

# Blackthorn Gym Layout & Boulders
- 2F Boulders (Initial): Boulder 6 (3,3), Boulder 7 (6,1), Boulder 8 (8,14).
- Boulders reset to initial positions at Turn 29858.
- 2F Pits: Pit (2,5), Pit (8,3), Pit (8,7).

# Strategy: Gym Leader Clair
- Lead GNEISS (Lv45) vs Dragonairs (Earthquake).
- Vs Kingdra: Calcifer (Smokescreen) -> GNEISS (Defense Curl + Rollout).

# Boulder Puzzle Decisive Action Phase
- Plan: Reset boulders by leaving 2F, then use BFS to find the push sequence.
- Step 1: Reach Ladder at (1, 7).
- Step 2: Transition to 1F and back.
- Step 3: Run BFS simulation for all 3 boulders.
- Puzzle Start: Turn 29800.
- Decisive Phase Start: Turn 29851.