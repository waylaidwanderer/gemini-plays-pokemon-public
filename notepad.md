# Tile Mechanics (Global)
- FLOOR: Traversable. Standard collision.
- WALL: Impassable. Silver blocks or solid boundaries.
- PIT: Warp tile for player (falls to 1F). Destination for boulders to form bridges on 1F.
- LADDER: Warp tile. Transfers between floors.
- ICE: Slippery movement.
- BOULDER BRIDGES: Boulders in pits act as passable FLOOR on the floor below.
- Strength: Must be re-activated after falling through a pit or changing maps.

# Blackthorn Gym Layout & Boulders
- 2F Boulders (Initial): Boulder 6 (3,3), Boulder 7 (6,1), Boulder 8 (8,14).
- 2F Pits: Pit (2,5), Pit (8,3), Pit (8,7).

# Strategy: Gym Leader Clair
- Lead GNEISS (Lv45) vs Dragonairs (Earthquake).
- Vs Kingdra: Calcifer (Smokescreen) -> GNEISS (Defense Curl + Rollout).

# Boulder Puzzle Strategy
- Mechanics: Push all three boulders into pits on 2F to create a path to Gym Leader Clair on 1F.
- Current Status: Boulders 6 and 7 are reset. Boulder 8 is at (8, 14). Strength needs activation.
- Plan: Use the `solve_blackthorn_boulders` tool to calculate the exact push sequence and execute it.
- Observations: Column 4 is a wall barrier for boulders except at Row 13. Row 0 is entirely impassable.
- Start Turn: 29800. Decisive Phase Start: Turn 29911.