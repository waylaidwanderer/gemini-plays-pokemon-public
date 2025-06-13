# Gem's Log: Pokémon Yellow Legacy - Hard Mode

## I. Current Status & Active Plans

### A. Pokémon Party (Turn 2574)
1. SPROUT (ODDISH): Lv10 (24/32 HP, EXP: 624) | Moves: TACKLE (7 PP), POISONPOWDER (35 PP), LEECH SEED (5 PP)
2. PIP (PIDGEY): Lv9 (21/27 HP, EXP: 523) | Moves: GUST (15 PP), SAND-ATTACK (15 PP)
3. SPARKY (PIKACHU): Lv12 (38/38 HP, EXP: 1728) | Moves: THUNDERSHOCK (28 PP), TAIL WHIP (30 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP) - AT LEVEL CAP (0 Badges). Visual EXP from NIDORAN♀ Lv3 (Turn 2578): +25.

### B. Financial Status
- Money: ¥296

### C. Current Location & Immediate Objective
- Location: Route 22 (ID: 33), at (34,11) (Turn 2574).
- Immediate Objective: Train SPROUT and PIP in the eastern grass patch of Route 22.

### D. Training Priorities
- SPROUT (ODDISH): Lv9 -> Needs significant training for Brock (Rock/Ground). Grass moves super effective. **PRIORITY**
- PIP (PIDGEY): Lv9 -> Needs training.
- SPARKY (PIKACHU): At cap, less effective vs Brock.

<!-- Goals section removed as per system guidance. Goals are tracked in the response structure. -->

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
- Party Order: Game may auto-switch lead Pokémon in certain battle initiation scenarios (Observed Turn 2572).

### E. Data Management & Logging
- **Battle Logs:** Summarize training progress (e.g., levels gained, key moves learned) rather than logging every individual EXP gain, especially for capped Pokémon, to keep notepad concise. Note visual EXP gains for capped Pokémon if significant.
- **PP/HP/EXP Tracking:** Rely on Game State Information as the absolute source of truth for Pokémon stats (HP, EXP, PP). Notepad entries are for reference/planning but can have discrepancies.

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
- 🚫: Bugged/Blocked/Problematic Interaction (Note reason)
- 🚧: Obstacle/Ledge (Note nature, e.g. "Ledge - Jump Down Only")
- ℹ️: Important Info/Sign
- 💬: Key NPC Dialogue Snippet
- ✅: Event Complete/Path Unblocked
- 🏛️: Gym Entrance (Note status)
- 🏠: Key Building Entrance
- 🏥: Pokécenter Entrance

## IV. Agent Management

### A. Defined Agents
1.  `level_cap_compliance_checker`
2.  `item_finder_agent`
3.  `wkg_transition_recorder_agent`

5.  `battle_strategist_agent`
6.  `pathfinding_agent`
7.  `exploration_helper_agent`

### B. Active Agent Improvement Tasks (High Priority)
- **`wkg_transition_recorder_agent`:** Update prompt to *mandate* querying WKG for existing nodes using `run_code` with `world_knowledge_graph_json_string` before suggesting new node creation. (Top Priority)
- **`item_finder_agent`:** Remove redundant `player_x`, `player_y` from `agent_input_schema` as agent can derive location from `map_xml_string`. (High Priority)
- **`pathfinding_agent` & `exploration_helper_agent`:** Prompts need significant update to handle ledges correctly. *Current Plan: Defer major fix, continue manual navigation in ledge-heavy areas like Route 22. Re-evaluate agent fix priority if Brock proves too difficult or if significant ledge navigation is required for other pre-Brock objectives.*
- **General for code-enabled agents**: Prompts must clarify use of `run_code` for auto-provided variables (`map_xml_string`, `world_knowledge_graph_json_string`) and how to parse/utilize them effectively.

### C. Future Agent Considerations (To be defined when strategically beneficial)
- **Ledge-Aware Explorer Agent:** Specialized for navigating ledge-heavy areas.
- **Training Spot Suggester Agent:** Input: target Pokémon, current location, desired level. Output: suggested map/grass/trainers.
- **Shop Inventory Agent:** Input: city/mart name. Output: items sold & prices.
- **EXP Farming Route Agent:** Input: target Pokémon, desired level. Output: optimal routes/areas.

## V. Lessons Learned & Strategic Refinements

### A. Key Learnings from Mistakes
- **NPC Interaction Threshold:** If an NPC interaction fails after 2-3 distinct, well-reasoned attempts, assume they are non-battling, already defeated, or require a different game state, then MOVE ON.
- **Pathing Precision:** Meticulously review Map Memory before committing to movement. Verify current map_id/position from Game State frequently. Cross-reference agent paths with map data, especially for ledges.
- **Agent Reliability:** If an agent is unreliable (e.g., pathfinding over ledges), default to manual planning or `run_code` scripts. Review/fix failing agent prompts ASAP.
- **Flexibility:** Be willing to change secondary/tertiary goals if current approach is stalled.
- **Map Segmentation by Ledges:** Understand that ledges create one-way paths and can isolate map sections.
- **Route 22 Ledge Navigation:** Manual exploration and careful map study are crucial for complex terrain like Route 22 due to agent failures.
- **Notepad `old_text`:** Double-check `old_text` for `replace` actions to avoid failed edits.

### B. Failed Hypotheses Log (Selected)
- VIRIDIANCITY_YOUNGSTER1 (ID 1) at various Viridian locations: Attempted battle ~20+ times (Turns ~1920-1943). Result: Stuck dialogue loop. Conclusion: Interaction bugged or requires unknown condition. Marked 🚫.
- `exploration_helper_agent` for Route 22 unseen tiles from (32,12) (Turn 2303): Path led to seen areas/ledges. Attempts: 1.
- `pathfinding_agent` for Route 22 to (12,8) from (32,12), (32,8) (Turns 2305-2307): Invalid ledge jumps. Attempts: 3.

### C. Manual Navigation Plans (When Agents Fail)
- **Route 22 (Current):** All navigation on Route 22 will be manual, focusing on systematically exploring reachable unseen tiles. This is due to repeated `pathfinding_agent` and `exploration_helper_agent` failures with ledges.

## VI. Historical Log & Major Milestones (CONCISE - To be reviewed/archived post-Brock)
- **Startup:** Pallet Town, got SPARKY. Delivered Oak's Parcel, got Pokédex.
- **Early Routes & Forest:** Traversed Route 1. Viridian Forest (caught SPROUT, PIP), defeated Bug Catchers.
- **Pewter City Exploration:** Visited Museum (couldn't afford ticket), Nidoran House, Mart. Gathered intel on Brock.
- **Blackout:** Lost to Jr. Trainer in Pewter Gym (Turn 1901). Returned to Viridian Pokecenter.
- **Viridian City NPC Issues:** Encountered bugged/non-battling NPCs (Youngster1, Gambler1).
- **Route 22 Initial Exploration:** Defeated Rival BLAZe (Turn ~2159). Navigational difficulties with ledges.
- **Route 22 Training (Turns 2250+):** Ongoing training for SPROUT and PIP.

## VII. Task List (Active & Pending)

### A. Pre-Brock Tasks (High Priority)
- **Agent Definition Updates (Immediate):**
    - `wkg_transition_recorder_agent`: Update prompt (see IV.B).
    - `item_finder_agent`: Update input schema (see IV.B).
- **Agent Prompt Fixes (Ongoing/Deferred):**
    - `pathfinding_agent` & `exploration_helper_agent` for ledges (see IV.B).
    - General review for code-enabled agents on auto-provided variable usage.
- **Map Markers (This Turn):**
    - Place Route 22 (9,6) Warp marker: 🚪 "Used - To Route 22 Gate (5,8) EP:1"
    - Place Route 22 (8,12) Sign marker: ℹ️ "Sign: ROUTE22_POKEMON_LEAGUE_SIGN"

### B. Post-Brock Task List (To be reviewed/actioned after defeating Brock)
- Review and prioritize agent development ideas (from IV.C).
- Review and summarize/archive older historical log entries from Section VI.
- Finalize any remaining agent prompt fixes from VII.A.
- Place any other pending map markers (e.g., Sign at Route 22 (8,12) - already marked, Ledge at Route 22 (34,8) - already marked).
- Review and potentially delete old/redundant tertiary goal definitions from Section I.E.

## VIII. Reflection Notes (Consolidated)
- **Notepad Maintenance (Critique Turn 2551):** This `overwrite` action addresses the need for consolidation. Will continue to aim for accurate `replace` actions or use `overwrite` for major refactors.
- **Agent `item_finder_agent` (Turn 2551):** Definition needs review for redundant player_x/y input.
- **Agent `capability_checker_agent`:** Deleted (Turn 2641) due to lack of use and to streamline agent list.