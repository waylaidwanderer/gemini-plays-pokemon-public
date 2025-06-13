# Gem's Log: Pokémon Yellow Legacy - Hard Mode

## I. Current Status & Active Plans

### A. Pokémon Party (Turn 2261)
1. SPARKY (PIKACHU): Lv12 (38/38 HP, EXP: 1728 - GAINED 0) | Moves: THUNDERSHOCK (30 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP) - AT LEVEL CAP (0 Badges)
2. SPROUT (ODDISH): Lv8 (27/27 HP, EXP: 374) | Moves: TACKLE (35 PP), POISONPOWDER (35 PP), LEECH SEED (10 PP)
3. PIP (PIDGEY): Lv9 (17/27 HP, EXP: 446) | Moves: GUST (27 PP), SAND-ATTACK (15 PP)

### B. Financial Status
- Money: ¥296

### C. Current Location & Immediate Objective (Turn 2312)
- Location: Route 22 (ID: 33), at (18,6).
- Immediate Objective: Manually explore western Route 22 (targeting unseen tile (13,7) first) and train SPROUT/PIP. Will avoid using navigation agents on this map due to ledge issues.

### D. Training Priorities
- SPROUT (ODDISH): Lv8 -> Needs significant training for Brock (Rock/Ground). Grass moves super effective. **PRIORITY**
- PIP (PIDGEY): Lv8 -> Needs training.
- SPARKY (PIKACHU): At cap, less effective vs Brock.

### E. Active Goals (for planning reference)
- **Primary Goal:** Defeat Brock and earn the Boulder Badge.
- **Secondary Goal:** Train SPROUT and PIP on Route 22 to prepare for Brock, and earn money.
- **Tertiary Goal:** Explore all 13 reachable unseen tiles on Route 22.

## II. Game Mechanics & Rules

### A. Hard Mode Rules
- Battle Style: Set.
- No items allowed in battle.
- Level caps: Pokémon cannot exceed cap for current badge count. (0 badges=12, 1=21, 2=24, 3=35, 4=43, 5=50, 6=53, 7=55, 8=65). EXP gain messages for capped Pokémon are visual only; no actual EXP is gained.

### B. General Game Changes (Pokémon Yellow Legacy)
- HMs: Forgettable, menu-use, not PC-storable. CUT is Bug-type.
- All 151 Pokémon obtainable. Trade evos by level.
- Smarter AI, tougher bosses, unlimited enemy PP.
- EXP. All obtainable without special requirements (seems active).

### C. Behavioral Guideline Summary (Internalized from Turn 2261 Critique)
- **Scientific Mindset:** Hypothesize, test, document failures (with attempt counts), avoid repeating failed strategies. Pivot goals if stalled.
- **Risk-Taking:** Be calculated, prioritize progression. Sacrifices okay in battle.
- **Wild Battles:** Run if capped/low HP/PP, unless catching/training. Speed dictates escape.
- **Nicknaming:** Always do it; enjoy the process.
- **Verification:** Trust direct observation over prior knowledge for ROM hack changes. Verify with multiple cases.

### D. Discovered Mechanics
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
- **ledge**: Jump down only. One-way traversal.
- **cuttable**: Tree, requires CUT.
- **Pikachu Movement**: If Pikachu is adjacent in movement direction & player not facing him, 2 presses needed (1st turns, 2nd moves). Normal otherwise.
- **PC Interaction**: Stand below, face up, press A.
- **Item Interaction**: Some items require 'A' interaction.

### B. Verified Type Matchups
- Ghost > Psychic.
- Poison > Bug; Bug !> Poison.

### C. NPC Interaction Log & Key Dialogue
- **Viridian Old Man (ID 5, (20,14) Viridian):** Taught catching, unblocked path N. (Marker ✅ set)
- **Viridian Girl (ID 4, (18,10) Viridian):** Grandpa needs coffee. (Marker 💬 set)
- **Pewter Gym Guide (Pewter Gym):** Brock's Lead: GEODUDE (Offense, Rock Throw). Other: ONIX (Defense, BIND). Electric harmless vs Ground.
- **Pewter Nidoran House Man (Pewter Nidoran House):** Traded Pokémon grow fast but might ignore unskilled trainers; BADGEs help.
- **VIRIDIANCITY_YOUNGSTER2 (ID 3, (28,18) Viridian):** Non-battling. Explained DVs. (Interaction concluded Turn 2000+)
- **VIRIDIANCITY_GAMBLER1 (ID 2, (31,9) Viridian):** Repeated dialogue ('I wonder who the LEADER is?'). Non-battling/bugged. (Marker 🚫 set)

### D. Defeated Trainers
- Bug Catcher (ID 2, VIRIDIANFOREST_YOUNGSTER2) at (31,34) in Viridian Forest. (Marker ☠️ set)
- Cooltrainer F (ID 5, LASS) at (3,42) in Viridian Forest. (Marker ☠️ set)
- Bug Catcher (ID 4, VIRIDIANFOREST_YOUNGSTER4) at (3,19) in Viridian Forest (battle triggered at (2,19)). (Marker ☠️ set)
- Rival BLAZe (Route 22, (30,5)) - Defeated SPEAROW Lv9, EEVEE Lv8. Earned ¥280. (Marker ☠️ set)

### E. Map Marker Legend & Strategy
- ☠️: Defeated Trainer
- 🚪: Used Warp (Note destination map/coords/EP)
- 🚫: Bugged/Blocked/Problematic Interaction (Note reason, e.g., Youngster1 Dialogue Loop at (10,23) Viridian)
- 🚧: Obstacle/Ledge (Note nature, e.g. "Ledge - Jump Down Only")
- ℹ️: Important Info/Sign
- 💬: Key NPC Dialogue Snippet
- ✅: Event Complete/Path Unblocked
- 🏛️: Gym Entrance (Note status, e.g. Unreachable)
- 🏠: Key Building Entrance
- 🏥: Pokécenter Entrance

## IV. Agent Management

### A. Defined Agents (Turn 2226+)
1.  `level_cap_compliance_checker`
2.  `item_finder_agent`
3.  `wkg_transition_recorder_agent` (Prompt updated Turn 2226 & 2261)
4.  `capability_checker_agent`
5.  `battle_strategist_agent`
6.  `pathfinding_agent` (Defined Turn 2226, Prompt updated Turn 2261 for ledges)
7.  `exploration_helper_agent` (Defined Turn 2226)

### B. Agent Performance Notes & Improvement Plans
- **`pathfinding_agent`:** Prompt updated (Turn 2261) to handle ledges correctly. Monitor performance. Previous failures with ledges (e.g., Turn 2243, 2246, 2270, 2272) caused significant delays.
- **`wkg_transition_recorder_agent`:** Prompt updated (Turn 2261). Still needs significant improvement to query WKG for existing nodes by coordinates and use actual IDs to avoid manual multi-step edge creation. Critical for streamlining WKG updates.
- **`exploration_helper_agent`:** Untested. *PRIORITY TO USE* for Route 22 unseen tiles.
- **`capability_checker_agent`:** Untested. Seek opportunity to test.
- **`item_finder_agent`:** Last used 9 hours ago. Review prompt and utility for relevance.
- **`capability_checker_agent`:** Untested. Seek opportunity to test.
- **`item_finder_agent`:** Untested. Prompt could be refined for building types.
- **`battle_strategist_agent`:** Untested.
- **General:** Ensure prompts for code-enabled agents clarify use of `run_code` for `map_xml_string` / `world_knowledge_graph_json_string`.

### C. Agent Development Ideas
- **Training Spot Suggester Agent:** Input: target Pokémon, current location, desired level. Output: suggested map/grass/trainers, considering types & enemy levels. (Low priority - fix existing agents first).
- **Shop Inventory Agent:** Input: city/mart name. Output: items sold & prices. (Requires discovery, low priority - fix existing agents first).

## V. Lessons Learned & Strategic Refinements

### A. Key Learnings from Mistakes
- **NPC Interaction Threshold:** If an NPC interaction fails after 2-3 distinct, well-reasoned attempts, assume they are non-battling, already defeated, or require a different game state, then MOVE ON. Do not get stuck in dialogue/interaction loops (e.g., Youngster1 Viridian, ~20 attempts).
- **Pathing Precision:** Meticulously review Map Memory before committing to movement. Verify current map_id/position from Game State frequently. Cross-reference agent paths with map data, especially for ledges.
- **Agent Reliability:** If an agent is unreliable (e.g., pathfinding over ledges), default to manual planning or `run_code` scripts. Review/fix failing agent prompts ASAP.
- **Flexibility:** Be willing to change secondary/tertiary goals if current approach is stalled. Don't fixate.
- **Map Segmentation by Ledges:** Understand that ledges create one-way paths and can isolate map sections. Different entry points to a route might be necessary to access all areas (e.g., Route 22 eastern vs. western sections).

### B. Failed Hypotheses Log (Selected)
- VIRIDIANCITY_YOUNGSTER1 (ID 1) at various Viridian locations: Attempted battle ~20+ times (Turns ~1920-1943) using A, B, Stun, Unstun, Menu, Movement. Result: Stuck dialogue loop. Conclusion: Interaction bugged or requires unknown condition. Marked 🚫.
- Pathfinding on Route 22: `pathfinding_agent` (before prompt update for ledges, Turn 2261) suggested going from (34,14) to (33,14) (Turn 2243, 2246), which is going *up* a ledge. Failed hypothesis: agent correctly handles ledges. Number of failed attempts with this agent path: 2. Agent also failed again (Turn 2270, 2272) by suggesting moving left from (34,14) to (33,14) over a ledge. Number of failed attempts with this agent path: 2 more. This highlights the importance of thorough agent testing and prompt refinement.

## VI. Historical Log & Major Milestones (CONCISE)
- **Startup:** Pallet Town, got SPARKY (Pikachu). Delivered Oak's Parcel, got Pokédex.
- **Early Routes & Forest:** Traversed Route 1. Viridian Forest (caught SPROUT (Oddish), PIP (Pidgey)), defeated Bug Catchers.
- **Pewter City Exploration:**
    - Visited Museum (couldn't afford ticket ¥50).
    - Nidoran House (learned about traded Pokémon & badges).
    - Mart.
    - Gathered intel on Brock in Pewter Gym (Geodude, Onix; Electric ineffective).
- **Blackout:** Lost to Jr. Trainer in Pewter Gym (Turn 1901). Returned to Viridian Pokecenter.
- **Viridian City NPC Issues:**
    - VIRIDIANCITY_YOUNGSTER1 (ID 1): Bugged dialogue loop (Turns ~1920-1943).
    - VIRIDIANCITY_YOUNGSTER2 (ID 3): Informational (DV speech), not a battler (Turns ~1966-2000).
    - VIRIDIANCITY_GAMBLER1 (ID 2): Non-battling/bugged (Turn ~2017-2019).
- **Route 22 Initial Exploration:** Defeated Rival BLAZe (Turn ~2159). Navigational difficulties accessing western/upper grass due to ledges and map entry points (Turns ~2205-2225).
- **Route 22 Training (Turns 2250+):**
    - **Turn 2261:** PIP defeated wild SPEAROW Lv6 (EXP 396). SPARKY (lead) gained no EXP (capped).
    - **Turn 2274:** PIP defeated wild Mankey Lv5 (grew to Lv9, EXP 422). SPARKY (lead) gained no EXP (capped).

## VII. Critique Review & Action Plan (Turn 2310)

- **Route 22 Ledge Navigation & Agent Usage:** Will cease using `pathfinding_agent` and `exploration_helper_agent` for Route 22 due to repeated failures with ledges. Will rely on manual navigation for this map until agent prompts are fixed. Manual navigation plans for problematic areas will be documented in section V.A.
- **Agent: `wkg_transition_recorder_agent`:** High priority to refine prompt to query WKG for existing nodes by coordinates and use their actual IDs to streamline edge creation.
- **Agent: `capability_checker_agent` & `item_finder_agent`:** Will seek opportunities to test/review these agents.
- **Notepad - Failed Hypotheses:** Continue documenting, ensuring attempt counts are included.
- **Notepad - Immediate Objective:** Consolidate updates to reflect more stable, multi-turn objectives.
- **Notepad - Duplication:** Redundant 'Historical Log' and 'Critique Review' sections removed (this entry reflects the cleanup).
- **Notepad - Agent Development Ideas:** Retained for now (Section IV.C), but fixing existing agents is a higher priority.

- **Agent Failure (Turn 2303):** `exploration_helper_agent` (for Route 22 unseen tiles from (32,12)) provided a path: (32,11)->(32,10)->(32,9)->(32,8)->(31,8)->(33,8)->(34,8)->(34,7)->(33,7)->(32,7)->(31,7). None of these coordinates are in the list of 13 reachable unseen tiles. The agent's path seems to explore already seen areas or ledges, not the actual unseen tiles located in the western part of the map. Number of failed attempts with this agent: 1.

- **Agent Failure (Turn 2305 & 2306):** `pathfinding_agent` (path to (12,8) from (32,12) on Route 22, then from (32,8)) suggested moving Left from (32,8) [ground] to (31,8) [ledge] described as 'jumping down ledge'. This move is invalid as you cannot jump down onto a ledge tile from an adjacent ground tile at the same or higher elevation. Movement was blocked. Path needs recalculation. Number of failed attempts with this agent path segment: 2.

### D. Manual Navigation Plans (When Agents Fail)
- **Route 22 (Current):** Due to repeated `pathfinding_agent` and `exploration_helper_agent` failures with ledges, all navigation on Route 22 will be manual until agent prompts are confirmed fixed for this terrain. Focus on systematically exploring reachable unseen tiles.

### D. Manual Navigation Plans (When Agents Fail)
- **Route 22 (Current):** Due to repeated `pathfinding_agent` and `exploration_helper_agent` failures with ledges, all navigation on Route 22 will be manual until agent prompts are confirmed fixed for this terrain. Focus on systematically exploring reachable unseen tiles.