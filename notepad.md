# 1. Strategic Imperatives & Rules (MANDATORY)
- **(RULE #1) Retreat > Faint:** Retreating to heal is more efficient than fainting. Prioritize team health.
- **(RULE #2) Proactive Agent Use:** Use agents *before* critical actions (battle switches, training spot selection, new area entry).
- **(RULE #3) Trust Game State:** The Game State data (`Reachable Unseen Tiles`, map connections) is absolute truth.
- **(RULE #4) Mandatory Location Check:** Always verify current map_id and coordinates before any action.
- **(RULE #5) Verify WKG Before Writing:** Check for existing nodes/edges before adding new ones to avoid errors.

# 2. Party & Level Caps
- **Current Cap (2 badges):** 24
- SPARKY (Pikachu): Lv24 (Capped)
- SPROUT (Gloom): Lv24
- PIP (Pidgeotto): Lv24
- THISTLE (Nidorina): Lv17
- PARCH (Sandslash): Lv24

# 3. Game Mechanics & World Insights
- **Level Cap:** Fake EXP gain message at cap; EXP value doesn't change.
- **PC System:** 'SOMEONE's PC' (Pokémon) vs 'Gem's PC' (Items).
- **Navigation:**
  - Defeated trainers remain as impassable obstacles.
  - Diglett's Cave connects Route 11 (Vermilion) to Route 2 (Pewter).
  - Cuttable trees respawn after changing maps.
- **HMs:**
  - **Flash:** Aide on Route 2 gives it for 10 caught Pokémon.
  - **Cut:** Received from S.S. Anne Captain.
- **Status Effects:**
  - Non-volatile status cured after trainer battles.
  - Poison deals 1 HP/4 steps outside battle.

# 4. Core Battle Mechanics (Learned Lessons)
- **EXP Sharing:** Shared among all participants for each faint.
- **Type Matchups (Verified):
  - Magnemite resists Flying (likely part Steel).
  - Ground is immune to paralysis (e.g., Stun Spore).
  - Poison is not very effective vs. Ground.
  - Ground is not very effective vs. Bug.
  - Fighting is not very effective vs. Poison.
- **Move Mechanics (Verified):
  - **Two-Turn Moves (Dig, Fly):** Invulnerable during the first turn.
  - **Sleep Status:** Prevents all actions. Counter only decreases if 'FIGHT' is selected. Hypnosis fails on sleeping targets.
  - **Leech Seed:** High accuracy (90%), but not guaranteed.
- **General Tactics (Verified):
  - Sacrificial switches are a valid hard-mode tactic.
  - **Adaptive Tactics:** Against accuracy-lowering moves (Sand-Attack), switch to high-accuracy/can't-miss moves or switch Pokémon.

# 5. Critical Failure Log (To Be Avoided)
- **(Tactical Failure):** Persisted with failing strategy (Double Kick vs. Sand-Attack on Route 11). **MUST ADAPT QUICKER.**
- **(Tactical Failure):** Ignored 4x Psychic weakness (THISTLE vs. Drowzee), leading to a faint and inefficient 'grind-faint-heal' loop on Route 11.
- **(Navigation Failure):** Misjudged dead ends by ignoring `Reachable Unseen Tiles` and map exits (Route 11, Route 2).
- **(Navigation Failure):** Forgotten that defeated trainers are impassable (Mt. Moon B2F, Route 11).
- **(Data Failure):** Hallucinated location (believed I was in Route 11 Gatehouse when still on Route 11). **MUST VERIFY WITH GAME STATE.**
- **(Procedural Failure):** Violated own rule by not using `battle_switch_advisor_agent` (vs. Dugtrio in Diglett's Cave).
- **(Knowledge Failure):** Incorrectly assumed SPROUT had a Grass-type damaging move. **MUST VERIFY MOVESETS.**

# 6. Procedural Reminders & Self-Correction
- **(CHECKLIST):** Before major actions, check party status.
- **(NAVIGATION):** Navigate small, explored rooms manually. Don't overuse pathfinder.
- **(WKG):** Always check for existing nodes/edges before adding new ones.

# 7. Agent Ideas (Implemented)
- HM Requirement Forecaster
- Battle Switch Advisor
- Training Hotspot Advisor
- Grind Session Manager
- Progression Blocker Agent