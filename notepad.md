# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable. Silver blocks.
- PIT: Warp tile. Falling through takes you to the floor below.
- LADDER: Warp tile.
- ICE: Slippery movement.
- BOULDER BRIDGES: Boulders in pits act as passable FLOOR.
- Strength must be re-activated after falling through a pit.

# Physically Tested Tiles (2F)
- (6,0): WALL confirmed.
- (5,0): WALL confirmed.
- (3,11) -> (4,11): Blocked by Fran (NPC).
- (5,1) -> (6,1): Passable (pushed boulder).

# Blackthorn Gym Layout & Boulders
- 2F Boulders (Current): Boulder 6 (3,3), Boulder 7 (7,1), Boulder 8 (8,14).
- 2F Pits: Pit (2,5), Pit (8,3), Pit (8,7).

# Boulder Puzzle Analysis
- Visual Walls (Unverified):
  - Row 0: (0,0), (1,0), (2,0), (3,0), (4,0), (7,0), (8,0), (9,0)
  - Col 4: (4,2)-(4,7)
  - Col 6: (6,2), (6,3), (6,4)
  - Misc: (8,9), (7,10), (7,11), (9,16), (2,13)
- Task: Identify "fake" walls blocking boulder solutions.
- Current Turn: 29826.

# Strategy: Gym Leader Clair
- Lead GNEISS (Lv45) vs Dragonairs (Earthquake).
- Vs Kingdra: Calcifer (Smokescreen) -> GNEISS (Defense Curl + Rollout).

# Navigation Insights
- 1F Access: Must use 2F detour (Ladder at 7,9 to Ladder at 1,7) to move between halves.
- 2F Crossing: Gap in the central wall exists at Row 13 (4, 13 is FLOOR). Column 4 is otherwise mostly WALLs and NPCs (Cody at 4,1, Fran at 4,11).