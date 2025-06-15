# Game Mechanics & Rules
- **Battle-Warps:** Specific tiles can trigger a wild battle that also teleports the player.
  - Location: Mt. Moon B2F (29, 9) -> B1F (21, 12). Trigger condition is unknown, seems unreliable. (Attempted 3 times without success). Should not be relied upon.
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
- **Mt. Moon B2F:**
  - The floor has multiple elevations and is split into unconnected sections. Accessing new sections requires finding different ladders on B1F.
  - **CRITICAL CORRECTION:** Rocket Grunt at (30, 12) is a mandatory trainer battle, not an item gate. His dialogue is a pre-battle taunt. Must be defeated to proceed west.

# Defeated Trainers Log
- **Mt. Moon 1F:** Hiker (6, 7), Youngster (8, 23), Lass (17, 25), Super Nerd (25, 30), Lass (31, 7), Youngster (13, 17), Youngster (31, 28)
- **Mt. Moon B2F:** Rocket Grunt (16, 23), Rocket Grunt (30, 8)

# Lessons & Future Plans
- **Navigation Strategy:**
  - Trust my refined agents, especially when they use pathfinding. My own assumptions can be flawed.
  - **The ladder at (26, 10) on B2F leads to a confirmed dead-end platform on B1F at (18, 12). This path should be ignored.**
- **Current Objective:** My party is critically injured, but the only way to heal is to progress. I must defeat the Rocket Grunt at (30, 12) to open the path forward.