# Gem's Log: Pokémon Yellow Legacy - Hard Mode

## I. Current Status & Active Plans

### A. Pokémon Party (Turn 2313)
1. SPARKY (PIKACHU): Lv12 (38/38 HP, EXP: 1728) | Moves: THUNDERSHOCK (30 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP) - AT LEVEL CAP (0 Badges)
2. SPROUT (ODDISH): Lv9 (21/29 HP, EXP: 436) | Moves: TACKLE (24 PP), POISONPOWDER (35 PP), LEECH SEED (8 PP)
3. PIP (PIDGEY): Lv9 (17/27 HP, EXP: 446) | Moves: GUST (27 PP), SAND-ATTACK (15 PP)

### B. Financial Status
- Money: ¥296

### C. Current Location & Immediate Objective (Turn 2418)
- Location: Route 22 (ID: 33), at (34,10) (Turn 2418).
- Immediate Objective: Train SPROUT and PIP in the eastern grass patch of Route 22.

### D. Training Priorities
- SPROUT (ODDISH): Lv8 -> Needs significant training for Brock (Rock/Ground). Grass moves super effective. **PRIORITY**
- PIP (PIDGEY): Lv9 -> Needs training.
- SPARKY (PIKACHU): At cap, less effective vs Brock.

### E. Active Goals (for planning reference)
- **Primary Goal:** Defeat Brock and earn the Boulder Badge.
- **Secondary Goal:** Train SPROUT and PIP on Route 22 to prepare for Brock, and earn money.
- **Tertiary Goal:** Incrementally train PIP (PIDGEY) on Route 22 when opportunities arise without compromising SPROUT's training. (Route 22 exploration complete).

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
- **`pathfinding_agent` & `exploration_helper_agent`:** Critically failing on Route 22 (ledges). Do NOT use for this map until prompts are fixed. Prompts need significant update to handle ledges. Documented failures: Turn 2303 (exploration_helper), Turns 2305, 2306, 2307 (pathfinding).
- **`wkg_transition_recorder_agent`:** Prompt needs refinement to query WKG for existing nodes and use actual IDs, rather than just outputting placeholders. (High Priority)
- **`capability_checker_agent`:** Untested. Seek opportunity to test.
- **`item_finder_agent`:** Review prompt and utility.
- **`battle_strategist_agent`:** Consider using more actively in challenging battles.
- **General:** Ensure prompts for code-enabled agents clarify use of `run_code` for auto-provided variables (`map_xml_string`, `world_knowledge_graph_json_string`) and how to parse/utilize them effectively.

### C. Agent Development Ideas
- **Training Spot Suggester Agent:** Input: target Pokémon, current location, desired level. Output: suggested map/grass/trainers, considering types & enemy levels. (Low priority - fix existing agents first).
- **Shop Inventory Agent:** Input: city/mart name. Output: items sold & prices. (Requires discovery, low priority - fix existing agents first).
- **Team Composition Advisor Agent:** Input: opponent's known/likely team, my current party. Output: suggested team members, move priorities, potential weaknesses. (Medium priority).
- **EXP Farming Route Agent:** Input: target Pokémon, desired level. Output: optimal routes/areas with suitable wild Pokémon/trainers, factoring type matchups and EXP yield. (Medium priority).

## V. Lessons Learned & Strategic Refinements

### A. Key Learnings from Mistakes
- **NPC Interaction Threshold:** If an NPC interaction fails after 2-3 distinct, well-reasoned attempts, assume they are non-battling, already defeated, or require a different game state, then MOVE ON. Do not get stuck in dialogue/interaction loops (e.g., Youngster1 Viridian, ~20 attempts).
- **Pathing Precision:** Meticulously review Map Memory before committing to movement. Verify current map_id/position from Game State frequently. Cross-reference agent paths with map data, especially for ledges.
- **Agent Reliability:** If an agent is unreliable (e.g., pathfinding over ledges), default to manual planning or `run_code` scripts. Review/fix failing agent prompts ASAP.
- **Flexibility:** Be willing to change secondary/tertiary goals if current approach is stalled. Don't fixate.
- **Map Segmentation by Ledges:** Understand that ledges create one-way paths and can isolate map sections. Different entry points to a route might be necessary to access all areas (e.g., Route 22 eastern vs. western sections).

### B. Failed Hypotheses Log (Selected)
- VIRIDIANCITY_YOUNGSTER1 (ID 1) at various Viridian locations: Attempted battle ~20+ times (Turns ~1920-1943) using A, B, Stun, Unstun, Menu, Movement. Result: Stuck dialogue loop. Conclusion: Interaction bugged or requires unknown condition. Marked 🚫.
- `exploration_helper_agent` for Route 22 unseen tiles from (32,12) (Turn 2303): Path led to seen areas/ledges, not target unseen tiles. Attempts: 1.
- `pathfinding_agent` for Route 22 to (12,8) from (32,12) (Turn 2305): Invalid ledge jump from (32,8) to (31,8). Attempts: 1.
- `pathfinding_agent` for Route 22 to (12,8) from (32,8) (Turn 2306): Invalid ledge jump from (32,8) to (31,8). Attempts: 1.
- `pathfinding_agent` for Route 22 to (12,8) from (32,8) (Turn 2307): Invalid ledge jump from (32,8) to (31,8). Attempts: 1.

### C. Key Learnings from Mistakes (Extended - Turn 2416)
- **Route 22 Ledge Navigation:** Initial reliance on agents for Route 22 was a mistake. Manual exploration, careful map study, and immediate documentation of ledge behavior are crucial for complex terrain. Avoided by: Switching to manual nav sooner.
- **Notepad `old_text`:** Double-check `old_text` for `replace` actions to avoid failed edits. Use game suggestions carefully or copy directly from notepad if unsure.

### D. Manual Navigation Plans (When Agents Fail)
- **Route 22 (Current):** All navigation on Route 22 will be manual, focusing on systematically exploring reachable unseen tiles (e.g., western cluster starting with (13,7)). This is due to repeated `pathfinding_agent` and `exploration_helper_agent` failures with ledges.

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

## VII. Critique Review & Action Plan (Turn 2313)
- **Route 22 Navigation:** Ceased use of `pathfinding_agent` & `exploration_helper_agent` for Route 22. Using manual navigation. Plan documented in V.D.
- **Notepad Discipline:** Overhauled notepad (Turn 2313) to remove duplications, consolidate objectives, and update agent notes per critique.
- **Agent Strategy:** Prioritizing `wkg_transition_recorder_agent` prompt fix. Will test `capability_checker_agent` and review `item_finder_agent`. Agent dev ideas remain low priority.
- **`capability_checker_agent`**: Untested. Seek opportunity to test or reconsider its necessity.
- **`item_finder_agent`**: Review prompt for player_x/y input redundancy, given `agent_can_run_code` and access to `map_xml_string`.

- **ledge**: Jump down only. One-way traversal. Confirmed (6,10) on Route 22 is a ledge when approached from (6,11) (below).

- **Turn 2359:** SPROUT defeated wild NIDORAN♂ Lv3 (EXP +12 to 386). SPARKY (lead, capped) gained no actual EXP.

## VIII. Reflection Notes (Turn 2365)
- **Agent Development Ideas Update:** Added 'Ledge-Aware Explorer Agent' (Medium Priority).
- **Agent Prompt Review Task:** Noted to review prompts for `item_finder_agent`, `wkg_transition_recorder_agent`, `pathfinding_agent`, `exploration_helper_agent` to ensure clarity on auto-provided variables (`map_xml_string`, `world_knowledge_graph_json_string`) for their `run_code` tool.

## VIII. Reflection Notes (Turn 2371)
- Discovered (34,8) on Route 22 is a ledge when approached from (34,9) (below).

- **Turn 2393:** SPROUT defeated wild MANKEY Lv4 (EXP +21 to 407). SPROUT HP now 20/27. SPARKY (lead, capped Lv12) gained no actual EXP (EXP message: +21 EXP, but actual EXP 1728 unchanged).

- **Turn 2408:** SPROUT defeated wild NIDORAN♂ Lv4 (grew to Lv9, EXP +17 to 424). SPROUT HP now 19/29. SPARKY (lead, capped Lv12) gained no actual EXP (EXP message: +17 EXP, but actual EXP 1728 unchanged).

## VIII. Reflection Notes (Turn 2416)
- **Agent Development Ideas Update:** Added 'Team Composition Advisor Agent' (medium priority) and 'EXP Farming Route Agent' (medium priority) to IV.C.
- **Agent Usage Note:** Consider using `battle_strategist_agent` more actively for challenging fights (added to IV.B).
- **Agent Prompt Reinforcement:** Reinforced notes in IV.B regarding prompt updates for `pathfinding_agent`, `exploration_helper_agent`, `wkg_transition_recorder_agent`, and the general review for code-enabled agents' auto-provided variables.
- **New Map Markers:** Ledge at Route 22 (34,8) and Sign at Route 22 (8,12) will be marked.
- **Lessons Learned Update:** Added notes to V.A about Route 22 ledge navigation strategy and being careful with notepad `old_text` for `replace` actions.

- Turn 2452: SPROUT (Lv9) defeated wild NIDORAN♂ Lv3 on Route 22. SPROUT EXP +12 (to 436). SPROUT HP now 21/29. SPARKY (lead, capped Lv12) gained +12 EXP (visual only, actual EXP 1728 unchanged).

## IX. Critique Review & Action Plan (Turn 2460)
- **PIP's HP:** Tertiary goal updated to healing PIP before further training. Will use a Potion after this battle.
- **Agent Development Ideas (IV.C):** Added note: 'Add to Post-Brock Task List: Review and prioritize agent development ideas (Ledge-Aware Explorer, Training Spot Suggester, Team Comp Advisor, EXP Farming Route Agent). Focus on current objectives until then.'
- **Historical Log Length (VI):** Added note: 'Add to Post-Brock Task List: Review and summarize/archive older historical log entries. Focus on current objectives until then.'
- **Agent Prompts & Auto-Provided Variables (IV.B):** Added note to review prompts for code-enabled agents for clarity on `map_xml_string` and `world_knowledge_graph_json_string` usage.

## IX. Post-Brock Tasks (Consolidated from Reflection Turn 2470)
- Review and prioritize agent development ideas (Ledge-Aware Explorer, Training Spot Suggester, Team Comp Advisor, EXP Farming Route Agent).
- Review and summarize/archive older historical log entries.
- Prioritize agent prompt fixes:
    - `pathfinding_agent` & `exploration_helper_agent` for ledges.
    - `wkg_transition_recorder_agent` to query WKG for existing nodes.
    - General review for code-enabled agents on auto-provided variable usage (`map_xml_string`, `world_knowledge_graph_json_string`).
- Place pending map markers:
    - Ledge at Route 22 (34,8)
    - Sign at Route 22 (8,12)
    - Ledge at Route 22 (6,10)

- Turn 2473: SPROUT (Lv9) defeated wild NIDORAN♂ Lv4 on Route 22. SPROUT EXP +17 (to 453). SPROUT HP now 20/29. TACKLE PP now 22/35. LEECH SEED PP 7/10. SPARKY (lead, capped Lv12) gained +17 EXP (visual only, actual EXP 1728 unchanged).

## X. Post-Brock Task List (To be reviewed/actioned after defeating Brock)
- Review and prioritize agent development ideas (e.g., Ledge-Aware Explorer, Training Spot Suggester, Team Comp Advisor, EXP Farming Route Agent).
- Review and summarize/archive older historical log entries from Section VI.
- Finalize agent prompt fixes:
    - `wkg_transition_recorder_agent` to query WKG for existing nodes.
    - General review for code-enabled agents on auto-provided variable usage (`map_xml_string`, `world_knowledge_graph_json_string`).
- Place pending map markers: Ledge at Route 22 (34,8), Sign at Route 22 (8,12), Ledge at Route 22 (6,10).

## XI. Pre-Brock Agent Review & Fixes (High Priority)
- **Pathfinding & Exploration Agents for Ledges:** `pathfinding_agent` & `exploration_helper_agent` are critically failing on Route 22 due to ledges.
    - **Decision Point:** Either prioritize fixing their prompts (or creating a 'Ledge-Aware Explorer Agent') *before* attempting Brock, or formally decide to rely on manual navigation/`run_code` for ledge-heavy areas until post-Brock.
    - Current Plan: Continue manual navigation on Route 22. Re-evaluate agent fix priority if Brock proves too difficult or if significant ledge navigation is required for other pre-Brock objectives.

### E. Data Management & Logging
- **Battle Logs:** Summarize training progress (e.g., levels gained, key moves learned) rather than logging every individual EXP gain, especially for capped Pokémon, to keep notepad concise.
- **PP/HP/EXP Tracking:** Rely on Game State Information as the absolute source of truth for Pokémon stats (HP, EXP, PP). Notepad entries are for reference/planning but can have discrepancies.

## X. Post-Brock Task List (To be reviewed/actioned after defeating Brock)
- Review and prioritize agent development ideas (e.g., Ledge-Aware Explorer, Training Spot Suggester, Team Comp Advisor, EXP Farming Route Agent).
- Review and summarize/archive older historical log entries from Section VI.
- Finalize agent prompt fixes:
    - `wkg_transition_recorder_agent` to query WKG for existing nodes.
    - General review for code-enabled agents on auto-provided variable usage (`map_xml_string`, `world_knowledge_graph_json_string`).
- Place pending map markers: Ledge at Route 22 (34,8), Sign at Route 22 (8,12), Ledge at Route 22 (6,10).

## XI. Pre-Brock Agent Review & Fixes (High Priority)
- **Pathfinding & Exploration Agents for Ledges:** `pathfinding_agent` & `exploration_helper_agent` are critically failing on Route 22 due to ledges.
    - **Decision Point:** Either prioritize fixing their prompts (or creating a 'Ledge-Aware Explorer Agent') *before* attempting Brock, or formally decide to rely on manual navigation/`run_code` for ledge-heavy areas until post-Brock.
    - Current Plan: Continue manual navigation on Route 22. Re-evaluate agent fix priority if Brock proves too difficult or if significant ledge navigation is required for other pre-Brock objectives.

### E. Data Management & Logging
- **Battle Logs:** Summarize training progress (e.g., levels gained, key moves learned) rather than logging every individual EXP gain, especially for capped Pokémon, to keep notepad concise.
- **PP/HP/EXP Tracking:** Rely on Game State Information as the absolute source of truth for Pokémon stats (HP, EXP, PP). Notepad entries are for reference/planning but can have discrepancies.

## X. Post-Brock Task List (To be reviewed/actioned after defeating Brock)
- Review and prioritize agent development ideas (e.g., Ledge-Aware Explorer, Training Spot Suggester, Team Comp Advisor, EXP Farming Route Agent).
- Review and summarize/archive older historical log entries from Section VI.
- Finalize agent prompt fixes:
    - `wkg_transition_recorder_agent` to query WKG for existing nodes.
    - General review for code-enabled agents on auto-provided variable usage (`map_xml_string`, `world_knowledge_graph_json_string`).
- Place pending map markers: Ledge at Route 22 (34,8), Sign at Route 22 (8,12), Ledge at Route 22 (6,10).

## XI. Pre-Brock Agent Review & Fixes (High Priority)
- **Pathfinding & Exploration Agents for Ledges:** `pathfinding_agent` & `exploration_helper_agent` are critically failing on Route 22 due to ledges.
    - **Decision Point:** Either prioritize fixing their prompts (or creating a 'Ledge-Aware Explorer Agent') *before* attempting Brock, or formally decide to rely on manual navigation/`run_code` for ledge-heavy areas until post-Brock.
    - Current Plan: Continue manual navigation on Route 22. Re-evaluate agent fix priority if Brock proves too difficult or if significant ledge navigation is required for other pre-Brock objectives.

(Appended under Section II. Game Mechanics & Rules)
### E. Data Management & Logging
- **Battle Logs:** Summarize training progress (e.g., levels gained, key moves learned) rather than logging every individual EXP gain, especially for capped Pokémon, to keep notepad concise.
- **PP/HP/EXP Tracking:** Rely on Game State Information as the absolute source of truth for Pokémon stats (HP, EXP, PP). Notepad entries are for reference/planning but can have discrepancies.

(Appended under Section IV.B. Agent Performance Notes & Improvement Plans)
- **`capability_checker_agent`**: Untested. Seek opportunity to test or reconsider its necessity.
- **`item_finder_agent`**: Review prompt for player_x/y input redundancy, given `agent_can_run_code` and access to `map_xml_string`. Also review utility.

(Appended under Section I.E. Active Goals (for planning reference) - Turn 2521)
- **Tertiary Goal (Updated):** Now that PIP is healed (27/27 HP), train PIP when SPROUT needs a break or if a suitable opportunity arises. (Original tertiary goal regarding Route 22 exploration to be reviewed/deleted later).