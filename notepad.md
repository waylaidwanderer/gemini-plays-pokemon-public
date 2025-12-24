# Current Strategy
- **Primary Goal:** Reach Blackthorn City via Ice Path.

# Ice Path Strategy
- **Primary Goal:** Reach Blackthorn City.
- **Status:** Testing Ledge Hypothesis.
- **Analysis:**
  - The map is divided vertically. The West Corridor (x=0) is the goal.
  - The **ONLY** connection found is at **Row 22** (x=0 to x=14 are Floor).
  - To reach Row 22, I must pass the barrier at Row 18.
  - The barrier consists of `FLOOR_UP_WALL` tiles. These MUST be jumpable ledges, or I am missing a hidden mechanic.
- **Plan:**
  1. Go to (8, 17).
  2. Attempt to jump ledge at (8, 18).
  3. If successful, walk South to Row 22, then West to x=0.
  4. If fail, this implies `FLOOR_UP_WALL` are solid walls. I will need to reassess the entire map for missed Warps or Ladders.
- **Items:** Item Balls at (32, 23) and (35, 9).

# Tile Mechanics
- **FLOOR:** Walkable.
- **WALL:** Impassable.
- **WATER:** Surfable.
- **HEADBUTT_TREE:** Interactable/Obstacle.

# Key Log
- **Turn 16261:** Surfing on Route 44 (35,9).
- **Turn 16240:** Defeated Psychic Phil.
- **Turn 16222:** Confirmed Suicune not in Pokedex.
- **Route 44 Update:** North/East bank of 2nd lake (Zach's island) is a DEAD END (Ledges block Eastward travel).
- **Correction:** Path to Blackthorn must be via the South Path, accessible from the 1st lake (likely landing South at x=27).
- **Next Step:** Backtrack to 1st lake and explore South bank.
- **Turn 16312:** Defeated Cooltrainer Cybil. Proceeding East on South Path to Blackthorn City.
- **Turn 16322:** Defeated Cooltrainer Allen at (37,15).
- **Turn 16327:** At (44,4). Path blocked by ledges. Looping South to (44,14) then East to (49,14) to use the gap.
- **Turn 16328:** Entered Ice Path 1F at (4,19).
- **Observation:** Spotted an Item Ball at (32, 23) in the eastern ice area, currently separated by a wall.
- **Observation:** Spotted another Item Ball at (35, 9) in the far North-East, currently unreachable from the low ground.
- **Correction:** The "South-East Path" was a dead end.
- **Hypothesis:** The way forward is likely jumping the ledge at (18, 24) to access the southern rows (25+).
- **Turn 16368:** Sliding Down from (19, 21) to (19, 23). Next: Move Right to (20, 23) to exit ice.
- **Turn 16369:** Dismissing Repel text. Retrying Slide Down from (19, 21).
- **Turn 16370:** Retrying Slide Down from (19, 21). Previous attempt interrupted by Repel text.
- **Turn 16374:** Spotted Item Ball at (31, 7). Continuing West along Row 11.
- **Turn 16375:** Reached dead end at (25, 11). Confirmed West path blocked by wall.
- **Correction:** The "North-East Loop" is a dead end on this level.
- **Action:** Backtracking to (20, 23) to retry the ledge jump at (20, 24). This is the only remaining lead to reach the lower-south area and the West Corridor (x=0).