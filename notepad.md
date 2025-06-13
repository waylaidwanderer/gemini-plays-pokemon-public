# Gem's Pokémon Yellow Legacy Hard Mode Playthrough Notes

## Game Information
*   **Player Name:** Gem
*   **Rival Name:** Pixel
*   **Current Badges:** 0 (Game State is Source of Truth)
*   **Current Level Cap:** 12 (0 badges - Game State is Source of Truth)
*   **Pokédex:** 10/151 (HM05 FLASH requirement met!)
*   **Money:** ¥506

## Core Game Rules & Mechanics (Notepad Quick Reference)
### Hard Mode Rules (Player-Only Restrictions):
*   **Battle Style:** Set mode.
*   **No items in battle.**
*   **Level caps apply.** (See table below)

### Level Cap Table:
*   0 badges: **12**
*   1 badge: **21**
*   2 badges: **24**
*   3 badges: **35**
*   4 badges: **43**
*   5 badges: **50**
*   6 badges: **53**
*   7 badges: **55**
*   8 badges: **65**

### Key Gameplay & Balance Changes (ROM Hack):
*   HMs: forgettable, menu use, no PC storage.
*   All 151 Pokémon obtainable.
*   Trade evolutions by level (e.g., Haunter → Gengar at 42, Machoke → Machamp at 38).
*   Smarter AI, anti-sweep tactics.
*   Tougher Boss fights (custom teams, varied).
*   Dynamic scaling for Gyms 4–6.
*   EXP. All obtainable without special requirements.

## Current Objectives & Tactical Plans (HOW to achieve goals)
*   **Viridian City Exploration (Post-Healing, 10 Pokédex Entries):**
    *   **Objective:** Systematically explore Viridian City for new leads (NPCs, interactions, items like EXP. All), prioritizing Reachable Unseen Tiles.
    *   **Current Focus (Turn 2026+):** Exploring southeastern unseen tiles: (33,32), (34,32), (35,32), (36,32). Currently at (33,31), planning to move to (33,32).
    *   **Contingency:** If Viridian City yields no new leads after thorough exploration, re-evaluate progression (check Pallet Town/Route 1 for new dialogue/events).
    *   **NPC Interaction Strategy:** Interact with any unencountered NPCs or re-interact with previously met NPCs to check for new dialogue due to increased Pokédex count.

## Pokémon Party & Status (As of Turn 2199)
*   **GOTTSAMER (METAPOD):** Lv8 (0/27 HP, FNT, PSN, EXP: 523). TACKLE (31 PP), STRING SHOT (40 PP), HARDEN (30 PP)
*   **NADEL (WEEDLE):** Lv4 (18/18 HP, EXP: 118). POISON STING (35 PP), STRING SHOT (40 PP)
*   **NIGHTSHADE (ODDISH):** Lv9 (24/30 HP, EXP: 430). TACKLE (32 PP), POISONPOWDER (35 PP), LEECH SEED (10 PP)
*   **AEGIS (KAKUNA):** Lv7 (15/24 HP, EXP: 489). POISON STING (30 PP), STRING SHOT (40 PP), HARDEN (30 PP)
*   **SPARKY (PIKACHU):** Lv8 (27/27 HP, EXP: 645). THUNDERSHOCK (29 PP), GROWL (40 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP)
*   **FURYFIST (MANKEY):** Lv4 (0/17 HP, EXP: 64). SCRATCH (25 PP), LEER (30 PP)

## Inventory & Key Items
*   **POKé BALL x2**
*   **OAK'S PARCEL:** Delivered.
*   **POKéDEX:** Received.
*   **HM05 FLASH:** Not yet obtained. (Pokédex requirement of 10 unique Pokémon to receive it has been met - item must still be acquired from NPC/event.)

## Lessons Learned, Game Mechanics & Insights
*   **Tile Types:** `ground`, `impassable`, `grass`, `ledge` (jump Y+2, impassable from Y+1 below), `cuttable`.
*   **Battle Menu (2x2):** FIGHT (top-left), PKMN (top-right), ITEM (bottom-left), RUN (bottom-right).
*   **Party List Selection:** 'A' on Pokémon opens sub-menu (SWITCH, STATS, CANCEL).
*   **Naming Screen:** 'START' confirms name. Plan inputs for efficiency.
*   **Poison:** Outside battle, -1 HP every 4 steps.
*   **Pikachu Movement:** Can walk through. Adjacent & not facing: 1st press turns, 2nd moves.
*   **Warp Types:** 1x1 instant (move off/on to re-warp). Larger warps (2x1, 1x2) may need 2 steps (onto warp, then into boundary/direction).
*   **Dialogue Clearing:** ALWAYS press 'A' to clear dialogue/text BEFORE other inputs.
*   **Type Matchups:** Ghost super effective vs. Psychic.
*   **Game Data Trust:** Game State Information is truth (badges, level caps, 'reachable'). Visual interpretation can be flawed.
*   **Interaction Loops:** If NPC/object interaction yields no progress after 2-3 attempts, different trigger needed.
*   **Coordinate Checks:** Verify current coordinates before planning movement.
*   **DV Checking:** Hold START while pressing A on STATS screen.
*   **Notepad `replace`:** `old_text` must be *exact*. `overwrite` for major changes.
*   **Pokémon Switching Menu:** Select Pokémon -> 'SWITCH' -> select swap target.
*   **Pathing Precision:** Analyze map memory/screen carefully, especially near ledges/complex terrain. Trust map memory for tile types. Multiple failed pathing attempts on Route 2 South (Turns 1940s, 1980s, 1990s) and Viridian City (Turns 2004-2012) due to misreading impassable tiles.
*   **Pokédex Evaluation:** Professor Oak or aides evaluate in person (not via PC, corrected from Viridian Forest sign).
*   **Battle Risk Assessment:** Balance "less cautious" guideline with resource conservation (e.g., SPARKY at 1HP vs RATTATA T1974 was very risky).
*   **WKG Tool Usage:** Single `manage_world_knowledge` call per operation. Record transitions IMMEDIATELY.
*   **Agent Usage Reflection (T2026):** Could have used `map_analyzer_agent` and `route_planner_agent` more during recent Viridian City navigation.

## Defeated Trainers Log
*   OAK'S LAB (ID 40) - (6,6) - Rival Pixel (initial battle)
*   Viridian Forest (ID 51) - (3,42) - Lass (Cool Trainer F sprite)
*   Viridian Forest (ID 51) - (28,20) - Youngster (Bug Catcher sprite, VIRIDIANFOREST_YOUNGSTER3)
*   Viridian Forest (ID 51) - (28,34) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER2)
*   Viridian Forest (ID 51) - (14,18) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER5)
*   Pewter Gym (ID 3) - (3,4) - Jr. Trainer M (DIGLETT Lv9, SANDSHREW Lv9)

## Agent Management (9 Active Agents)
*   **`battle_strategist_agent`**: Analyzes battle data for optimal moves/switches.
*   **`route_planner_agent`**: Calculates paths. (Code-enabled)
*   **`level_cap_compliance_agent`**: Checks party vs. level cap.
*   **`wild_encounter_evaluator_agent`**: Advises on wild encounters (FIGHT, RUN, CATCH).
*   **`npc_dialogue_analyzer_agent`**: Interprets NPC dialogue for clues. (Low usage, review pending).
*   **`optimal_training_spot_agent`**: Suggests training areas. (Code-enabled)
*   **`item_reminder_agent`**: Reminds about nearby uncollected items.
*   **`map_analyzer_agent`**: Identifies strategic points on current map. (Code-enabled)
*   **`team_composition_advisor_agent`**: Recommends teams for major battles. (Code-enabled)
*   **Agent Development Plan:** Review system prompts for code-enabled agents after obtaining HM Flash to ensure optimal use of auto-provided variables. Consider `Pokédex Completion Strategist` or `HM Usage Advisor` if a slot is needed and `npc_dialogue_analyzer_agent` is deleted.

## Archived Plans & Hypotheses
### Route 2 (South) - HM Flash Aide Search (Turns ~1988-2002)
*   **Initial Hypothesis:** Aide for HM05 FLASH accessible via warp to Viridian Forest South Gate at (4,44) on Route 2 (South). (10 Pokédex entries met).
*   **Pathing Attempts from Route 2 South to (4,44) warp:**
    *   North along X=8: Failed (T1995, blocked at (8,58) by impassable (8,57)).
    *   North along X=9: Failed (T1996, blocked at (9,58) by impassable (9,57)).
    *   North along X=10: Failed (T1997, blocked at (10,58) by impassable (10,57)).
    *   North along X=11: Failed (T1998, blocked at (11,58) by impassable (11,57)).
*   **Conclusion (T1998):** Warp to Viridian Forest South Gate at (4,44) NOT reachable from southern segment of Route 2. Paths blocked by trees (Y=57) or ledges (Y=48). 'Reachable:yes' flag for warp likely misleading for this isolated map segment. HM Flash Aide search on Route 2 (South) stalled.
*   **Pivoted Strategy (T1998):** Heal Pokémon (completed T2022), then re-explore Viridian City.

### Viridian City Exploration - Pathing to Northern Unseen Tiles (Turn 2024)
*   **Attempt:** Pathing north from (27,17) towards (27,6) to explore unseen tiles (e.g., (26,3-6)).
*   **Outcome:** Realized path blocked by Y=10 ledge line, preventing northward travel from southern part of city to that specific cluster. 'Reachable' status likely requires different approach (e.g., different entry point to Viridian City, or a path not yet found).

*   **Entered Route 2 (South) (T2069):** Arrived at (9,72) from Viridian City (19,1). Goal: Reach warp at (4,44) to Viridian Forest South Gate.

- **Wild Battle (Viridian Forest, (19,37), T2133):** Defeated wild METAPOD. FURYFIST fainted. SPARKY EXP: 615 -> 645 (+30). GOTTSAMER EXP: 433 -> 463 (+30).

## Viridian Forest NPC Notes (Turn 2205+)
*   Youngster 6 (VIRIDIANFOREST_YOUNGSTER6) at (28,41) gave a tip: "I ran out of POKé BALLs to catch POKéMON with! You should carry extras!". Did not initiate a battle.