# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable. Silver blocks.
- PIT: Warp tile. Falling through takes you to the floor below.
- BOULDER BRIDGES: Boulders in pits act as passable FLOOR.
- Strength must be re-activated after falling through a pit.

# Blackthorn Gym Layout & Boulders
- 2F Boulders (Initial): Boulder 6 (3,3), Boulder 7 (6,1), Boulder 8 (8,14).
- 2F Pits: Pit (2,5), Pit (8,3), Pit (8,7).

# Boulder Puzzle Analysis
- Confirmed Walls:
  - Row 0: (2,0), (3,0), (5,0), (7,0), (8,0), (9,0)
  - Col 4: (4,2)-(4,7)
  - Col 6: (6,2), (6,3)
  - Misc: (8,9), (7,10), (7,11), (9,16), (2,13)
  - NPCs: Cody (4,1)
- Current Strategy: Use comprehensive code to find blocking walls and test them.
- Note: Turn 29746 success at (4,3) was a hallucination.

# Strategy: Gym Leader Clair
- Lead GNEISS (Lv45) vs Dragonairs (Earthquake).
- Vs Kingdra: Calcifer (Smokescreen) -> GNEISS (Defense Curl + Rollout).

# Navigation Insights
- 1F Access: Must use 2F detour (Ladder at 7,9 to Ladder at 1,7) to move between halves.