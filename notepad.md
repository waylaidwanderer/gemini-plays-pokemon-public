# Gem's Log: Pokémon Yellow Legacy - Hard Mode

## I. Current Status & Active Plans

### A. Pokémon Party
1. SPARKY (PIKACHU): Lv12 (38/38 HP, EXP: 1728) | Moves: THUNDERSHOCK (30 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP) - AT LEVEL CAP (0 Badges)
2. SPROUT (ODDISH): Lv7 (25/25 HP, EXP: 296) | Moves: TACKLE (35 PP), POISONPOWDER (35 PP)
3. PIP (PIDGEY): Lv7 (23/23 HP, EXP: 287) | Moves: GUST (35 PP), SAND-ATTACK (15 PP)

### B. Financial Status
- Money: ¥16 (CRITICALLY LOW!)

### C. Current Location & Immediate Objective
- Location: Viridian City (ID: 1), at (28,19) facing Up.
- Immediate Objective: Battle wild Mankey on Route 22, then explore Route 22 for trainers/money/EXP.

### D. Training Priorities
- SPROUT (ODDISH): Lv7 -> Needs significant training for Brock (Rock/Ground).
- PIP (PIDGEY): Lv7 -> Needs training.
- SPARKY (PIKACHU): At cap, less effective vs Brock.

### E. Active Goals (for planning reference)
- **Primary Goal:** Defeat Brock and earn the Boulder Badge.
- **Secondary Goal:** Find a way to earn money to prepare for Brock.
- **Tertiary Goal:** Explore reachable unseen tiles in Viridian City.

## II. Game Mechanics & Rules

### A. Hard Mode Rules
- Battle Style: Set.
- No items allowed in battle.
- Level caps: Pokémon cannot exceed cap for current badge count. (0 badges=12, 1=21, 2=24, 3=35, 4=43, 5=50, 6=53, 7=55, 8=65).

### B. General Game Changes (Pokémon Yellow Legacy)
- HMs: Forgettable, menu-use, not PC-storable. CUT is Bug-type.
- All 151 Pokémon obtainable. Trade evos by level.
- Smarter AI, tougher bosses, unlimited enemy PP.
- EXP. All obtainable without special requirements.

### C. Discovered Mechanics
- Poison: 1 HP lost per 4 steps outside battle.
- STAT Experience: Significant stat boosts from battling/leveling.
- PC Log Off: Saves game.
- Evolution: By training.
- Status Conditions: SLP (AWAKENING), BRN (BURN HEAL), PSN (ANTIDOTE), FRZ (ICE HEAL), PAR (PARLYZ HEAL).
- Wild Battle Escapes: Speed-dependent. If lead Pokémon's Speed >= wild's, escape is guaranteed. Otherwise, chance increases with attempts.
- Pokémon Nicknaming: Always do it when prompted.
- DV Checking: Hold START, then press A on STATS in Pokémon menu. (Learned from VIRIDIANCITY_YOUNGSTER2, Turn 1972)

## III. World Knowledge & Exploration

### A. Discovered Tile Types & Movement Rules
- **ground**: Walkable.
- **impassable**: Walls, objects, etc. Not traversable.
- **warp**: Map transition. Activation varies (instant 1x1, or 2-step for larger like exit mats/gatehouses).
- **water**: Requires Surf.
- **grass**: Wild encounters.
- **ledge**: Jump down only.
- **cuttable**: Tree, requires CUT.
- **NPC Interaction & Blocking**: Dialogue loops cannot be broken by re-interacting. NPCs can block paths. Treat non-battling/informational NPCs as such after their dialogue.
- **Pikachu Movement**: If Pikachu is adjacent in movement direction & player not facing him, 2 presses needed (1st turns, 2nd moves). Normal otherwise.
- **PC Interaction**: Stand below, face up, press A.
- **Item Interaction**: Some items require 'A' interaction.

### B. Verified Type Matchups
- Ghost > Psychic.
- Poison > Bug; Bug !> Poison.

### C. Defeated Trainers
- Bug Catcher (ID 2, VIRIDIANFOREST_YOUNGSTER2) at (31,34) in Viridian Forest. (Marker ☠️ set)
- Cooltrainer F (ID 5, LASS) at (3,42) in Viridian Forest. (Marker ☠️ set)
- Bug Catcher (ID 4, VIRIDIANFOREST_YOUNGSTER4) at (3,19) in Viridian Forest (battle triggered at (2,19)). (Marker ☠️ set)

### D. Important NPC Information & Key Dialogue
- Viridian Old Man (ID 5, now at (20,14)): Taught catching, unblocked path N. (Marker ✅ set)
- Viridian Girl (ID 4, (18,10)): Grandpa needs coffee. (Marker 💬 set)
- Pewter Gym Guide: Brock's Lead: GEODUDE (Offense, Rock Throw). Other: ONIX (Defense, BIND). Electric harmless vs Ground.
- Pewter Nidoran House Man: Traded Pokémon grow fast but might ignore unskilled trainers; BADGEs help.
- VIRIDIANCITY_YOUNGSTER2 (ID 3, (28,18)): Non-battling. Explained DVs. (Interaction concluded Turn 2000+)

### E. Map Marker Legend & Strategy
- ☠️: Defeated Trainer
- 🚪: Used Warp (Note destination map/coords/EP)
- 🚫: Bugged/Blocked/Problematic Interaction (Note reason, e.g., Youngster1 Dialogue Loop at (10,23))
- ℹ️: Important Info/Sign
- 💬: Key NPC Dialogue Snippet
- ✅: Event Complete/Path Unblocked
- 🏛️: Gym Entrance (Note status, e.g. Unreachable)
- 🏠: Key Building Entrance
- 🏥: Pokécenter Entrance

### F. World Knowledge Graph (WKG) Strategy
- Use `wkg_transition_recorder_agent` for all inter-map transitions.
- Record nodes and edges immediately after map_id changes.
- Capture node IDs from `add_node` calls to streamline edge creation if doing manually.

## IV. Agent Management

### A. Defined Agents
1.  `level_cap_compliance_checker`
2.  `item_finder_agent`
3.  `map_exploration_strategist_agent`
4.  `path_simplifier_agent`
5.  `wkg_transition_recorder_agent`
6.  `capability_checker_agent`

### B. Agent Review TODOs & Improvement Plans
- `map_exploration_strategist_agent`: **CRITICAL FAILURE (Turn 1945, 2038).** As per critique (Turn 2040), continued use is a major error. Must establish a reliable alternative (fix agent, `run_code` script, or manual planning) ASAP. Current strategy is manual planning.
- `path_simplifier_agent`: **PRIORITY REVIEW.** Failed Turn 1946 and Turn 2006 (jumbled instructions, incorrect button presses). Logic, especially Pikachu handling, is unreliable. Consider replacement with a `run_code` script or commit to manual path breakdown.
- `item_finder_agent`: Review prompt for better building ID. Assess utility; consider deletion if not consistently valuable.
- `wkg_transition_recorder_agent`: Monitor multi-step output. Ensure logic for existing vs. new nodes is robust.
- `capability_checker_agent`: Untested. Seek opportunity to test or reassess necessity.

### C. Agent Development Ideas
- Battle Strategist Agent: Input current/enemy Pokémon details, output suggested battle action (attack, switch, move). Could be very useful for Hard Mode strategy.
- Focus on improving existing agents.

## V. Lessons Learned & Strategic Refinements

### A. Key Learnings from Mistakes
- **NPC Interaction Threshold:** If an NPC interaction fails after 2-3 distinct, well-reasoned attempts, assume they are non-battling, already defeated, or require a different game state, then MOVE ON. Do not get stuck in dialogue/interaction loops (e.g., Youngster1, Youngster2).
- **Pathing Precision:** Meticulously review Map Memory before committing to movement. Verify current map_id/position from Game State frequently.
- **Agent Reliability:** If an agent is unreliable, default to manual planning or `run_code` scripts. Review/fix failing agent prompts ASAP.
- **Flexibility:** Be willing to change secondary/tertiary goals if current approach is stalled. Don't fixate.

### B. Failed Hypotheses Log (Selected)
- VIRIDIANCITY_YOUNGSTER1 (ID 1) at (10,23) / (15,18) etc.: Attempted battle ~20+ times (Turns ~1920-1943) using A, B, Stun, Unstun, Menu, Movement. Result: Stuck dialogue loop. Conclusion: Interaction bugged or requires unknown condition. Marked 🚫.
- VIRIDIANCITY_YOUNGSTER2 (ID 3) at (28,18) etc.: Attempted battle ~10+ times (Turns ~1966-2000) after he gave DV info. Result: Repeated DV dialogue. Conclusion: Informational NPC, non-battling. Interaction concluded.

## VI. Historical Log & Major Milestones (CONCISE)
- Started in Pallet Town, got SPARKY (Pikachu).
- Delivered Oak's Parcel, got Pokédex.
- Traversed Route 1, Viridian Forest (caught SPROUT (Oddish), PIP (Pidgey)).
- Explored Pewter City, Museum (couldn't afford ticket), Nidoran House, Mart.
- Gathered intel on Brock in Pewter Gym.
- **Blackout:** Lost to Jr. Trainer in Pewter Gym (Turn 1901). Returned to Viridian Pokecenter. Money halved to ¥16.
- **Stuck Interaction:** VIRIDIANCITY_YOUNGSTER1 (ID 1) dialogue loop (Turns ~1920-1943).
- **Misunderstood NPC:** VIRIDIANCITY_YOUNGSTER2 (ID 3) - informational (DV speech), not a battler (Turns ~1966-2000).

### Agent Review Update (Turn 2007)
- `path_simplifier_agent`: Failed again (Turn 2006). Outputted jumbled instructions and incorrect total button presses. Manual path breakdown and button press calculation was necessary. **PRIORITY REVIEW NOW** to fix its logic or consider replacing with a `run_code` script for path simplification.

### NPC Interaction Updates (Turn 2019)
- **VIRIDIANCITY_YOUNGSTER2 (ID 3, (29,22) area):** Confirmed informational NPC. Explained DVs. Not a battler. Marked interaction as concluded.
- **VIRIDIANCITY_GAMBLER1 (ID 2, (31,9)):** Interaction attempt (Turn 2017-2019). Repeated dialogue ('I wonder who the LEADER is?') after two 'A' presses. Conclusion: Likely non-battling or bugged. Abandoning as a battle target. Marked 🚫.