# Game Mechanics & Rules
- **Battle-Warps:** Specific tiles can trigger a wild battle that also teleports the player.
  - Location: Mt. Moon B2F (29, 9) -> B1F (21, 12). Trigger condition is unknown, seems unreliable. (Attempted 3 times without success).
- **Confusion:** This status effect wears off after a battle ends.
- **Defeated Trainers:** Some defeated trainers become impassable obstacles.
- **Dialogue:** A single 'A' press advances dialogue. 'B' can dismiss it.
- **Elevation Rule:** Movement between `ground` and `elevated_ground` is impossible unless a `steps` tile connects them. An exception allows movement *from* an elevated tile *onto* an adjacent warp tile.

# Battle Notes & Movesets
- Electric is ineffective vs. Ground (Geodude, Sandshrew).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Electric is NOT very effective vs. Bug/Grass (Paras), or Grass/Poison (Oddish, Bellsprout).

# Area Notes & Navigation
- **Mt. Moon B1F:**
  - Ladder at (26, 16) leads to a dead-end on 1F.
  - Ladder at (6, 6) leads to a dead-end on 1F.
  - Ladder at (18, 12) is on an isolated platform, accessible from B2F (26, 10). Seems to be a trap/dead end.
- **Mt. Moon B2F:**
  - The floor has multiple elevations and is split into unconnected sections. Accessing new sections requires finding different ladders on B1F.
  - Rocket Grunt at (30, 12) blocks the path west, demands a fossil.

# Defeated Trainers Log
- **Mt. Moon 1F:** Hiker (6, 7), Youngster (8, 23), Lass (17, 25), Super Nerd (25, 30), Lass (31, 7), Youngster (13, 17), Youngster (31, 28)
- **Mt. Moon B2F:** Rocket Grunt (16, 23), Rocket Grunt (30, 8)

# Lessons & Future Plans
- **Navigation Strategy:** My agents are powerful tools, but their output must be cross-referenced with my own direct experience. I will not blindly follow an agent's path if it relies on a mechanic I've observed to be unreliable (e.g., the battle-warp).
- **Current Objective:** My party is critically injured. I must find a way out of Mt. Moon to heal. My current hypothesis is that I'm on a dead-end platform on B1F and must return to B2F to find the correct exit ladder.