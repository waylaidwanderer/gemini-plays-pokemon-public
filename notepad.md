# 1. Strategic Imperatives & Rules (MANDATORY)
- **(RULE #1) Break the 'Grind-Faint-Heal' Loop:** Retreating to a Pokémon Center to heal an injured team is MORE EFFICIENT than risking a faint and being forced to retreat. Prioritize team health for sustainable training.
- **(RULE #2) Proactive Agent Use:** Use strategic agents *before* taking critical actions, not after a mistake.
  - `battle_switch_advisor_agent` MUST be used before every non-forced switch in battle.
  - `training_hotspot_advisor` MUST be used to find efficient grinding spots, not just defaulting to the nearest grass patch.
- **(RULE #3) Trust Game State Data:** The Game State Information (especially `Reachable Unseen Tiles` and map connection data) is the absolute source of truth. Do not hallucinate or misread it.
- **(RULE #4) Mandatory Location Check:** Before ANY action (tool call, movement), I MUST verify my current map_id and coordinates against the Game State. No exceptions.

# 2. Party & Level Caps
- **Current Cap (2 badges):** 24
- SPARKY (Pikachu): Lv24 (Capped)
- SPROUT (Gloom): Lv24
- PIP (Pidgeotto): Lv24
- THISTLE (Nidoran♀): Lv16
- PARCH (Sandslash): Lv22

# 3. Game Mechanics & World Insights
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

# 4. Core Battle Mechanics (Learned Lessons)
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

# 5. Critical Failure Log
- **(FAILURE LOG - Tactical):** Persisted with a failing strategy (DIG vs. Sand-Attack). Must adapt quickly.
- **(FAILURE LOG - Tactical):** Careless switch (THISTLE vs. Drowzee) led to a faint due to ignoring a 4x Psychic weakness. This initiated the 'grind-faint-heal' loop. (Route 11).
- **(FAILURE LOG - Navigation):** Misjudged dead ends by ignoring `Reachable Unseen Tiles` and map exits. (Route 11 x2, Route 2 x1).
- **(FAILURE LOG - Navigation):** Forgotten that defeated trainers are impassable obstacles. (Mt. Moon B2F, Route 11).
- **(FAILURE LOG - Data):** Hallucinated unseen tiles and location multiple times. Must verify with game state data.

# 6. Procedural Reminders & Self-Correction
- **(CHECKLIST):** Before starting a new major action (like training or entering a dungeon), check the status of all party members first.
- **(NAVIGATION):** For simple, small, fully-explored rooms (like a Pokémon Center), navigate manually. Do not overuse the pathfinder agent.