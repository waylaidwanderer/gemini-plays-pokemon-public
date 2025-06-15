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
- **Mt. Moon B2F:** The floor has multiple elevations. The main path forward was to simply walk east around the Rocket Grunt at (30, 12).

# Defeated Trainers Log
- **Mt. Moon 1F:** Hiker (6, 7), Youngster (8, 23), Lass (17, 25), Super Nerd (25, 30), Lass (31, 7), Youngster (13, 17), Youngster (31, 28)
- **Mt. Moon B2F:** Rocket Grunt (16, 23), Rocket Grunt (30, 8)

# Lessons & Future Plans
- **CRITICAL LESSON:** Do not fixate on NPCs as impassable walls. Always check for open paths around them. My assumption that the Rocket at (30, 12) blocked the entire corridor cost me over 50 turns.
- **CRITICAL LESSON:** The ladder at (26, 10) on B2F leads to a confirmed dead-end platform on B1F at (18, 12). This path is a loop and should be ignored.
- **CRITICAL LESSON:** The Rocket Grunt at (30, 12) is NOT an item gate. His dialogue is a pre-battle taunt. He must be defeated to proceed past his line of sight, but the path around him is open.
- **Agent Reliability:** My `map_analyzer_agent` is fundamentally broken. Do not trust it until it has been successfully overhauled and tested. Rely on direct observation first.