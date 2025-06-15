# Game Mechanics & Rules
- Dialogue: A single 'A' press advances dialogue. 'B' can dismiss it.
- Defeated Trainers: Some defeated trainers become impassable obstacles.
- Elevation Rule: Movement between `ground` and `elevated_ground` is impossible unless a `steps` tile connects them. An exception exists for adjacent warp tiles, allowing downward movement.
- Confusion: This status effect wears off after a battle ends.

# Battle Notes & Movesets
- Electric is ineffective vs. Ground (Geodude, Sandshrew).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Electric is NOT very effective vs. Bug/Grass (Paras), or Grass/Poison (Oddish, Bellsprout).

# Area Notes & Navigation
- **Mt. Moon 1F:**
  - The ladder at (26, 16) is a one-way trap to a dead-end area on B1F.
  - The ladder at (6, 6) is a dead end.
  - The ladder at (18, 12) appears to be the main path forward.
- **Mt. Moon B1F:** The ladder at (18, 12) appears to be a one-way path up from B2F.

# Lessons & Future Plans
- **Navigation Strategy:** Manual navigation is highly inefficient. My attempts to create a single, complex pathfinding agent have failed due to issues with parsing the map XML.
- **Pathfinding Failure (Definitive):** All attempts at automated pathfinding, both via agents and direct `run_code` scripts, have failed to produce optimal paths. They are unreliable. I am abandoning all automated pathfinding and will proceed with meticulous, segment-by-segment manual navigation.
- **Potential Future Agents:**
  - `pc_organizer_agent`: To help manage Pokémon storage for optimal team building.
  - `fossil_revival_advisor`: To help choose which fossil to revive later.

# Defeated Trainers Log
- **Mt. Moon 1F:**
  - Hiker (6, 7)
  - Youngster (8, 24) (Bug Catcher sprite)
  - Lass (17, 25)
  - Super Nerd (25, 30)
  - Lass (31, 7)
  - Youngster (13, 17)
  - Youngster (31, 28)
- **Mt. Moon B2F:**
  - Rocket Grunt (16, 23)
  - Rocket Grunt (30, 8)