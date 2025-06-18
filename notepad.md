# 1. Party & Level Caps
- **Current Cap (2 badges):** 24
- SPARKY (Pikachu): Lv24 (Capped)
- SPROUT (Gloom): Lv23
- PIP (Pidgeotto): Lv22
- THISTLE (Nidoran♀): Lv16
- PARCH (Sandshrew): Lv15

# 2. Battle Strategy & Type Matchups
- **Lt. Surge's Raichu (Lv 29):** Knows Body Slam (Normal) and Surf (Water). PARCH (Sandshrew) is the best counter but is under-leveled and weak to Surf.
- **Type Discoveries:**
  - Magnemite resists Flying (likely part Steel).
  - Ground-types are immune to paralysis from moves like Stun Spore.
  - Poison moves are not very effective against Ground-types.
- **General Tactics:**
  - Sacrificing a Pokémon for a free switch is a valid hard-mode tactic.

# 3. Game Mechanics & World Insights
- **Level Cap:** Fake EXP gain message at cap; EXP value doesn't change.
- **EXP Sharing:** EXP is shared among all battle participants for each faint.
- **Status Effects:** Non-volatile status cured after trainer battles. Poison deals 1 HP/4 steps.
- **PC System:** 'SOMEONE's PC' (Pokémon) vs 'Gem's PC' (Items).
- **Navigation & Key Items:**
  - Defeated trainers remain as impassable obstacles.
  - Diglett's Cave connects Route 11 (Vermilion) to Route 2 (Pewter).
  - **HM Flash:** Needed for Rock Tunnel. An Aide of Prof. Oak gives it to you if you have caught 10 different Pokémon. The Aide is in the southern gatehouse on Route 2.
  - **HM Cut:** Received from the Captain of the S.S. Anne.

# 4. Critical Lessons & Risk Management
- **(FAILURE LOG): Misjudging Dead Ends:** I have repeatedly ignored the `Reachable Unseen Tiles` list, leading to getting stuck. I must trust the game state information. (Failed on Route 11 twice, Route 2 once).
- **(FAILURE LOG): Ignoring Obstacles:** I have forgotten that defeated trainers are impassable, leading to failed pathing. (Failed on Mt. Moon B2F, Route 11).
- **(FAILURE LOG): Hallucination:** I have misidentified my location multiple times. I must verify my position with game state data before acting.
- **(RISK ASSESSMENT):** Use `heal_priority_agent` *before* entering new, dangerous areas. I failed to do this before entering Route 11, resulting in a near party wipe.
- **(TOOL USAGE):** Trust agents (pathfinder, exploration) to find paths when I am stuck.