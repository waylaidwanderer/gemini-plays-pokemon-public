# Game Mechanics & Rules
- **Battle-Warps:** Specific tiles can trigger a wild battle that also teleports the player. Location: Mt. Moon B2F (29, 9) -> B1F (21, 12). Unreliable.
- **Confusion:** Wears off after battle.
- **Defeated Trainers:** Some become impassable obstacles.
- **Elevation Rule:** Movement between `ground` and `elevated_ground` requires a `steps` tile.

# Battle Notes & Movesets
- Electric is ineffective vs. Ground (Geodude, Sandshrew).
- Grass is 4x effective vs. Rock/Ground (Geodude).
- Electric is NOT very effective vs. Bug/Grass (Paras) or Grass/Poison (Oddish, Bellsprout).

# Area Notes & Navigation
- **Mt. Moon B2F:** The northern section is a large side-loop accessed via a ladder on B1F at (26, 10). The main path forward is in the southern part of the floor.

# Defeated Trainers Log
- **Mt. Moon 1F:** Hiker (6, 7), Youngster (8, 23), Lass (17, 25), Super Nerd (25, 30), Lass (31, 7), Youngster (13, 17), Youngster (31, 28)
- **Mt. Moon B2F:** Rocket Grunt (16, 23), Rocket Grunt (30, 8)

# Lessons & Future Plans
- **CRITICAL LESSON:** Do not fixate on NPCs as impassable walls. Always check for open paths around them. My assumption that the Rocket at (30, 12) blocked the entire corridor cost me over 50 turns. The path was open to the east the entire time.
- **CRITICAL LESSON:** The ladder at (26, 10) on B2F leads to a confirmed dead-end platform on B1F at (18, 12). This path is a loop and should be ignored.
- **Agent Reliability:** My `map_analyzer_agent` was fundamentally broken. Do not trust it until it has been successfully overhauled and tested. Rely on direct observation first.

- **Item-Gated NPCs:** Some NPCs block paths and require a specific item to let you pass, instead of a battle. Example: Rocket Grunt at Mt. Moon B2F (30, 12) requires a fossil.