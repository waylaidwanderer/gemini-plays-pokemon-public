# 1. Party & Level Caps
- **Current Cap (2 badges):** 24
- SPARKY (Pikachu): Lv24 (Capped)
- SPROUT (Gloom): Lv24
- PIP (Pidgeotto): Lv24
- THISTLE (Nidoran♀): Lv16
- PARCH (Sandshrew): Lv21

# 2. Game Mechanics & World Insights
- **Level Cap:** Fake EXP gain message at cap; EXP value doesn't change.
- **PC System:** 'SOMEONE's PC' (Pokémon) vs 'Gem's PC' (Items).
- **Navigation:**
  - Defeated trainers remain as impassable obstacles.
  - Diglett's Cave connects Route 11 (Vermilion) to Route 2 (Pewter).
  - Cuttable trees respawn after changing maps.
- **HM Flash:** An Aide of Prof. Oak on Route 2 gives it if you have caught 10 different Pokémon.
- **HM Cut:** Received from the Captain of the S.S. Anne.
- **Status Effects:**
  - Non-volatile status (e.g., sleep, paralysis) is cured after trainer battles.
  - Poison deals 1 HP/4 steps outside of battle.

# 3. Core Battle Mechanics (Learned Lessons)
- **EXP Sharing:** EXP is shared among all Pokémon who participated in the battle for each faint. (Discovered on Route 11).
- **Type Matchups:**
  - Magnemite resists Flying (likely part Steel).
  - Ground-types are immune to paralysis from moves like Stun Spore.
  - Poison moves are not very effective against Ground-types.
  - Ground-type moves are not very effective against Bug-type Pokémon (e.g., PARCH's DIG vs. Caterpie).
- **Move Mechanics:**
  - **Two-Turn Moves (Dig, Fly, etc.):** Pokémon are invulnerable during the first turn. Attacking them during this phase will always result in a miss.
  - **Sleep Status:** A sleeping Pokémon CANNOT perform any actions. If put to sleep while underground, it cannot complete the second turn of a move like DIG. The sleep counter only decreases if 'FIGHT' is selected. Hypnosis fails against an already sleeping Pokémon.
- **General Tactics:**
  - Sacrificing a Pokémon for a free switch is a valid hard-mode tactic.
  - **(Sustainable Training):** Use REST proactively to heal, then switch to another Pokémon to finish the fight.

# 4. Critical Lessons & Risk Management
- **(FAILURE LOG): Misjudging Dead Ends:** Repeatedly ignored `Reachable Unseen Tiles`, getting stuck. Must trust game state information. (Failed on Route 11 x2, Route 2 x1).
- **(FAILURE LOG): Ignoring Obstacles:** Forgotten that defeated trainers are impassable. (Failed on Mt. Moon B2F, Route 11).
- **(FAILURE LOG): Hallucination:** Misidentified my location multiple times. Must verify position with game state data.
- **(FAILURE LOG): Tactical Rigidity:** Persisted with a failing strategy (DIG vs. Sand-Attack). Must adapt quickly and use agents.
- **(FAILURE LOG): Inefficient Status Recovery:** Wasted turns waiting for Sleep to wear off. Pokémon Centers are the most efficient cure.
- **(RISK ASSESSMENT):** Use `heal_priority_agent` *before* entering new, dangerous areas.
- **(RISK ASSESSMENT):** Lt. Surge's Raichu might know an Electric-type move. Don't assume its moveset is fully known.
- **(TOOL USAGE):** Trust agents (pathfinder, exploration) to find paths when stuck. Use `battle_switch_advisor_agent` in critical battles.

# 5. Procedural Reminders & Self-Correction
- **(CHECKLIST):** Before starting a new major action (like training or entering a dungeon), check the status of all party members first.
- **(NAVIGATION):** For simple, small, fully-explored rooms (like a Pokémon Center), navigate manually. Do not overuse the pathfinder agent.

# 6. World Knowledge Graph Node IDs
- Vermilion City East Entrance (from Route 11): 2c1fc924-efe9-4559-8c7a-902cf94ef665