# Game Mechanics & Rules
- Dialogue: A single 'A' press advances dialogue. 'B' can dismiss it.
- Defeated Trainers: Some defeated trainers become impassable obstacles.
- Elevation Rule: Movement between `ground` and `elevated_ground` is impossible unless a `steps` tile connects them. An exception exists for adjacent warp tiles, allowing movement onto them from an elevated tile.
- Confusion: This status effect wears off after a battle ends.

# Battle Notes & Movesets
- Electric is ineffective vs. Ground (Geodude, Sandshrew).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Electric is NOT very effective vs. Bug/Grass (Paras), or Grass/Poison (Oddish, Bellsprout).

# Area Notes & Navigation
- **Mt. Moon 1F:**
  - The ladder at (26, 16) is a one-way trap to a dead-end area on B1F.
  - The ladder at (6, 6) is a dead end.
  - The ladder at (18, 12) is a dead-end trap.

# Defeated Trainers Log
- **Mt. Moon 1F:**
  - Hiker (6, 7)
  - Youngster (8, 23) (Bug Catcher sprite)
  - Lass (17, 25)
  - Super Nerd (25, 30)
  - Lass (31, 7)
  - Youngster (13, 17)
  - Youngster (31, 28)
- **Mt. Moon B2F:**
  - Rocket Grunt (16, 23)
  - Rocket Grunt (30, 8)

# Lessons & Future Plans
- **Navigation Strategy (Revised):** My initial attempts at automated pathfinding failed, but abandoning the approach is the wrong lesson. The failure was in my agent design and prompting. I will commit to iteratively refining my navigation and pathfinding agents until they are reliable tools. Manual navigation will be a fallback, not the primary strategy.

- **Battle-Warps:** Some specific tiles can trigger a wild battle that also teleports the player to a different location/map. Discovered on Mt. Moon B2F (29, 9) warping to B1F (21, 12).