# 1. Party Composition & Strategy
- **SPARKY (Pikachu):** Lv24 Electric. Fast sweeper, paralysis support. Capped.
- **SPROUT (Gloom):** Lv23 Grass/Poison. Status effects (Leech Seed, Stun Spore), good bulk.
- **THISTLE (Nidoran♀):** Lv16 Poison/Ground. Under-leveled physical attacker.
- **PIP (Pidgeotto):** Lv22 Normal/Flying. Standard attacker.
- **PARCH (Sandshrew):** Lv14 Ground. Key counter for Electric types, but critically weak to Water (Surf). Very under-leveled.

# 2. Battle Strategy & Type Matchups
- **Lt. Surge's Team (Known):**
  - Raichu (Lv 29): Knows Body Slam (Normal) and Surf (Water).
- **Type Discoveries:**
  - Magnemite resists Flying, suggesting it's part Steel-type.
  - Ground-types seem immune to paralysis from moves like Stun Spore.
  - Poison-type moves are not very effective against Ground-types.
- **General Strategy:**
  - Sacrificing a Pokémon for a free switch is a valid tactic.
  - Avoid relying on confused or sleeping Pokémon against strong attackers.

# 3. Game Mechanics & World Insights
- **Level Cap:** Fake EXP gain message at cap; EXP value doesn't change. Current cap (2 badges) is 24.
- **EXP Sharing:** EXP is shared among all battle participants for each faint.
- **Status Effects:** Non-volatile status cured after trainer battles. Poison deals 1 HP/4 steps outside battle.
- **PC System:** 'SOMEONE's PC' (Pokémon) vs 'Gem's PC' (Items).
- **Navigation:**
  - Defeated trainers remain as impassable obstacles.
  - Diglett's Cave connects Route 11 (Vermilion) to Route 2 (Pewter).
  - An NPC mentioned FLASH is needed for the dark Rock Tunnel.

# 4. Critical Lessons & Risk Management
- **(FAILURE LOG): Misjudging Dead Ends:** I have repeatedly ignored the `Reachable Unseen Tiles` list, leading to getting stuck. I must trust the game state information. (Failed on Route 11 twice, Route 2 once).
- **(FAILURE LOG): Ignoring Obstacles:** I have forgotten that defeated trainers are impassable, leading to failed pathing. (Failed on Mt. Moon B2F, Route 11).
- **(FAILURE LOG): Hallucination:** I completely misidentified my location (thought I was in Vermilion City while on Route 11, thought I was in the Route 2 Gatehouse while still outside). I must verify my position with game state data before acting.
- **(RISK ASSESSMENT):** I must use my `heal_priority_agent` *before* entering new, dangerous areas. I failed to do this before entering Route 11, resulting in a near party wipe.
- **(TOOL USAGE):** Trust agents (pathfinder) to find paths when I am stuck. Use `select_battle_option` for main battle menu choices.

# 5. Current Strategy & Blockers
- **Route 2 Gatehouse Block:** The gatehouse at (4,12) on Route 2 is currently impassable. Multiple attempts to enter have failed. The reason is unknown.
- **New Plan:** The AI critique revealed a major flaw in my strategy. The path forward is not through the stubborn gatehouse. Instead, I must explore the reachable unseen tiles on the eastern part of Route 2 to find Professor Oak's Aide and obtain HM Flash.