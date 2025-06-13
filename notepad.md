## Game Info
*   **Player Name:** Gem
*   **Rival Name:** Pixel
*   **Current Badges:** 0 (Game State is Source of Truth)
*   **Current Level Cap:** 12 (0 badges - Game State is Source of Truth)
*   **Pokédex:** 9/151 (Need 1 more unique for HM Flash)
*   **Money:** ¥506

## Hard Mode Rules (Player-Only Restrictions):
*   **Battle Style:** Set mode.
*   **No items in battle.**
*   **Level caps apply.**

## Level Cap Table:
*   0 badges: **12**
*   1 badge: **21**
*   (etc.)

## Gameplay & Balance Changes (Noted from Prompt):
*   HMs: forgettable, menu use, no PC storage.
*   All 151 Pokémon obtainable.
*   Trade evos by level.
*   Smarter AI, anti-sweep.
*   Tougher Bosses.
*   Dynamic scaling Gyms 4–6.
*   EXP. All obtainable.

## Current Objectives & Plans (HOW to achieve goals):
*   **HM05 FLASH Acquisition:** Catch 1 more unique Pokémon species (total 10 in Pokédex). Then, find Professor Oak's Aide on Route 2 (likely southern part or via Viridian Forest if accessible) to get HM05 FLASH.
*   **Pokédex Completion Strategy:** Actively seek out and attempt to catch new Pokémon species in all encounter areas, prioritizing routes leading to current objectives.
*   **Current Focus:** Explore grass on Route 2 (South) for a new Pokémon. If unsuccessful, re-evaluate access to Viridian Forest.

## Pokémon Party & Log (Current as of Turn 1944):
*   **GOTTSAMER (METAPOD):** Lv7 (17/25 HP, EXP: 433). TACKLE (35 PP), STRING SHOT (40 PP), HARDEN (30 PP)
*   **NADEL (WEEDLE):** Lv4 (18/18 HP, EXP: 118). POISON STING (35 PP), STRING SHOT (40 PP)
*   **NIGHTSHADE (ODDISH):** Lv8 (25/28 HP, EXP: 397). TACKLE (35 PP), POISONPOWDER (35 PP), LEECH SEED (9 PP)
*   **AEGIS (KAKUNA):** Lv7 (24/24 HP, EXP: 462). POISON STING (35 PP), STRING SHOT (40 PP), HARDEN (29 PP)
*   **SPARKY (PIKACHU):** Lv8 (23/27 HP, EXP: 615). THUNDERSHOCK (27 PP), GROWL (40 PP), QUICK ATTACK (30 PP), THUNDER WAVE (17 PP)
*   **FURYFIST (MANKEY):** Lv4 (0/17 HP, FNT, EXP: 64). SCRATCH (34 PP), LEER (30 PP)

## Items Obtained:
*   **POKé BALL x3**
*   **OAK'S PARCEL:** Delivered to Prof. Oak.
*   **POKéDEX:** Received from Prof. Oak.

## Discovered Tile Types & Properties:
*   `ground`: Walkable.
*   `impassable`: Walls, counters, etc. Not enterable.
*   `grass`: Wild encounters.
*   `ledge`: Jump down (Y+2 from above the ledge tile), not up. Impassable from below (when player is at Y+1 relative to ledge tile at Y).

## Lessons Learned / Game Mechanics:
*   **Battle Menu Navigation (2x2 Layout):** FIGHT (top-left), PKMN (top-right), ITEM (bottom-left), RUN (bottom-right).
*   **Party List Selection:** 'A' on Pokémon opens sub-menu (SWITCH, STATS, CANCEL).
*   Menu Navigation (Naming Screen): Precise inputs. 'B' is backspace. 'START' or 'END' confirms.
*   Poison: Outside battle, -1 HP every 4 steps.
*   Pikachu Movement: Can walk through. Adjacent & not facing: 1st press turns, 2nd moves.
*   Warp Types: 1x1 instant. Larger warps (2x1, 1x2) may need 2 steps.
*   Critical Game Mechanic: ALWAYS press 'A' to clear dialogue/text BEFORE other inputs.
*   Ghost vs. Psychic: Ghost-type moves SUPER EFFECTIVE against Psychic.
*   **Trust Game Data:** Game State Information is ABSOLUTE TRUTH (e.g., badges, level caps). Corrected notepad error regarding Brock/badges.
*   Failed Interaction Loops: If NPC/object interaction yields no progress after 2-3 attempts, different trigger needed.
*   Coordinate Misreads: Double-check current coordinates.
*   DV Checking Tip: Hold START while pressing A on STATS screen.
*   Notepad `replace` Action: `old_text` must be *exact*. `overwrite` used for major corrections.
*   Pokémon Switching Menu: Select Pokémon -> 'SWITCH' -> select swap target.
*   Battle Efficiency: Avoid low EXP battles. Balance agent recommendations with resources.
*   Cautious Pathing: Prioritize avoiding optional fights when injured/poisoned.
*   Escape Mechanics: Speed-dependent. Lead with fastest if critical.
*   WKG Tool Usage: No multi-step tool chains in one turn.
*   Battle Menu Tool: Use `select_battle_option` if manual nav fails.
*   Stat Drops: Account for stat changes in move choice.
*   Goal Prioritization: Re-evaluate tertiary goals if primary/secondary advanceable.
*   Ledge Navigation: Impassable from below (Y+1 of ledge). The 'reachable:yes' flag for warps on the same map might not fully account for this if player is on the 'wrong' side of a series of ledges.

## Defeated Trainers:
*   OAK'S LAB (ID 40) - (6,6) - Rival Pixel (initial battle)
*   Viridian Forest (ID 51) - (3,42) - Lass (Cool Trainer F sprite)
*   Viridian Forest (ID 51) - (28,20) - Youngster (Bug Catcher sprite, VIRIDIANFOREST_YOUNGSTER3)
*   Viridian Forest (ID 51) - (28,34) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER2)
*   Viridian Forest (ID 51) - (14,18) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER5)

## Agent Management (9 Active Agents):
*   **`battle_strategist_agent`**: Defined.
*   **`route_planner_agent`**: Defined.
*   **`level_cap_compliance_agent`**: Defined. Use frequently. Input `num_badges` from Game State.
*   **`wild_encounter_evaluator_agent`**: Defined. Use judgment.
*   **`npc_dialogue_analyzer_agent`**: Defined. Low usage. Will review system prompt or delete after next town/milestone.
*   **`optimal_training_spot_agent`**: Defined.
*   **`item_reminder_agent`**: Defined.
*   **`map_analyzer_agent`**: Defined.
*   **`team_composition_advisor_agent`**: Defined. Test before next major battle.
*   **Agent Development Plan (Revised T1944):**
    *   `pokedex_progress_agent`: Idea discarded to keep agent slot free.
    *   **Action Item:** Review system prompts for all code-enabled agents (`route_planner_agent`, `optimal_training_spot_agent`, `map_analyzer_agent`, `team_composition_advisor_agent`) after the current exploration of Route 2 (South) or reaching Viridian Forest, to ensure optimal configuration (leveraging auto-provided variables, not defining them in input schemas).

## World Knowledge Graph Notes:
*   **Critical:** Record inter-map transitions IMMEDIATELY.

## Area Notes:
### Route 2 (ID 13) - Current Area
*   **Objective:** Catch 1 more unique Pokémon for HM Flash. Proceed to Viridian Forest if possible, then find Oak's Aide for HM05 FLASH.
*   **Current Location:** (5,51) - Grass (South Part)
*   **Items:** Two Poké Balls visible on map (14,55) and (14,46) but listed as `reachable: no` (likely on inaccessible eastern ledge path).
*   **Encounters:** None yet on this map part.
*   **Pokédex Evaluation:** Professor Oak or his aides evaluate the Pokédex in person. (Corrected from PC evaluation note).
*   **Navigation:** Western path seems blocked by ledges at Y=48 if trying to go north to warp (4,44) from south of these ledges. Warp (4,44) to Viridian Forest South Gate is `reachable:yes` in game state, but this might be misleading due to one-way ledges.

### Route 22 (ID 33)
*   **Encounters:** FURYFIST (MANKEY) (Lv4, caught). SPIKE (NIDORAN♂) (Lv3, caught, sent to PC). BELLADONNA (NIDORAN♀) (Lv4, caught, sent to PC).

## AI Feedback & Action Plan (Turn 1923 & 1937 addressed):
*   **Battle Tactics:** Acknowledged stat change impact. THUNDERSHOCK better vs NIDORAN♀ after Growl.
*   **Goal Refinement:** Tertiary goal is exploration for encounters on current route segment.
*   **Agent Development:** Addressed `pokedex_progress_agent` (discarded). Scheduled review of other agent prompts.
*   **Poké Ball Management:** 3 Poké Balls remaining. Be cautious.
*   **Notepad Management:** Using `overwrite` for major refactors. Careful with Nicknaming screen.
*   **Nicknaming Screen:** Acknowledged inefficiency. Will plan inputs more carefully.
*   **Multi-step Movement:** Will continue to plan reasonably long paths but be ready for interruptions.
*   **Deferred Tasks:** Addressed agent development plan deferrals.
*   **Agent Usage:** Will try to use `npc_dialogue_analyzer_agent` and `team_composition_advisor_agent` more appropriately or decide on their future.
*   **Pokédex Evaluation Correction:** Corrected notepad based on AI feedback (not via PC).
*   **WKG:** Will continue to manage diligently.

## Reflection Insights (Turn 1974):
*   **Battle Risk Assessment:** Letting SPARKY drop to 1HP vs RATTATA was very risky. Consider switching or using items (if allowed) more proactively in similar situations. Prioritize Pokémon health when possible, even if it means a slightly longer battle.
*   **Pathing Precision:** Multiple pathing attempts on Route 2 (South) were blocked by impassable tiles visible on screen. Analyze the screen more carefully before committing to multi-step paths, or use `run_code` to parse `map_xml_string` for pathfinding if unsure, especially in unfamiliar or complex areas.
*   **Agent Usage Reminder:** Use `map_analyzer_agent` more consistently when entering new routes or areas to get strategic insights early on.