## Game Info
*   **Player Name:** Gem
*   **Rival Name:** Pixel
*   **Current Badges:** 0 (Game State is Source of Truth)
*   **Current Level Cap:** 12 (0 badges - Game State is Source of Truth)
*   **Pokédex:** 10/151 (HM05 FLASH requirement met!)
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
*   **HM05 FLASH Acquisition:** Requirement of 10 unique Pokémon met. Current hypothesis: Aide is accessible via the warp to Viridian Forest South Gate at (4,44) on Route 2 (South), which game state lists as 'reachable'. Pathing north along X=8, then west to (4,44).
*   **Failed Hypotheses Log (Route 2 Aide Search):**
    *   Sign at (6,66) is/leads to Aide: Failed Attempt 1 (Sign text unchanged).
    *   Aide appears on Route 2 (South) after map reload: Failed Attempt 1 (No new NPC sprites after re-entering Route 2 from Viridian City).
*   **Pokédex Completion Strategy:** Continue catching new species when opportunities arise, especially if Flash acquisition is blocked.
*   **Healing:** Heal SPARKY (1HP) and revive FURYFIST (fainted) at the next Pokémon Center (likely Viridian City if Aide search fails here and forces backtrack).

## Pokémon Party & Log (Current as of Turn 1993):
*   **GOTTSAMER (METAPOD):** Lv7 (17/25 HP, EXP: 433). TACKLE (35 PP), STRING SHOT (40 PP), HARDEN (30 PP)
*   **NADEL (WEEDLE):** Lv4 (18/18 HP, EXP: 118). POISON STING (35 PP), STRING SHOT (40 PP)
*   **NIGHTSHADE (ODDISH):** Lv8 (25/28 HP, EXP: 397). TACKLE (35 PP), POISONPOWDER (35 PP), LEECH SEED (9 PP)
*   **AEGIS (KAKUNA):** Lv7 (24/24 HP, EXP: 462). POISON STING (35 PP), STRING SHOT (40 PP), HARDEN (29 PP)
*   **SPARKY (PIKACHU):** Lv8 (1/27 HP, EXP: 615). THUNDERSHOCK (26 PP), GROWL (40 PP), QUICK ATTACK (30 PP), THUNDER WAVE (16 PP)
*   **FURYFIST (MANKEY):** Lv4 (0/17 HP, FNT, EXP: 64). SCRATCH (34 PP), LEER (30 PP)

## Items Obtained:
*   **POKé BALL x2**
*   **OAK'S PARCEL:** Delivered to Prof. Oak.
*   **POKéDEX:** Received from Prof. Oak.

## Discovered Tile Types & Properties:
*   `ground`: Walkable.
*   `impassable`: Walls, counters, etc. Not enterable.
*   `grass`: Wild encounters.
*   `ledge`: Jump down (Y+2 from above the ledge tile), not up. Impassable from below (when player is at Y+1 relative to ledge tile at Y).

## Lessons Learned / Game Mechanics:
*   **Battle Menu Navigation (2x2 Layout):** FIGHT (top-left), PKMN (top-right), ITEM (bottom-left), RUN (bottom-right). Navigate with appropriate directional inputs. Pay close attention to screen text for current cursor position.
*   **Party List Selection:** Pressing 'A' on a Pokémon in the 'Choose a POKéMON' list *selects* it and brings up its sub-menu (SWITCH, STATS, CANCEL). Pay close attention to screen text to confirm sub-menu vs. main list.
*   **Menu Navigation (Naming Screen):** Precise inputs needed. Verify letter before 'A'. 'B' is backspace. 'START' confirms name (manually navigating to END is not required).
*   **Nicknaming Efficiency:** Plan directional inputs for nicknames to reduce turns. A single sequence of directional inputs followed by 'A' is more efficient than multiple single-direction + 'A' turns. Using 'Start' to confirm is key.
*   Poison: Outside battle, -1 HP every 4 steps.
*   Pikachu Movement: Can walk through. Adjacent & not facing: 1st press turns, 2nd moves.
*   Warp Types: 1x1 instant (move off/on to re-warp). Larger warps (2x1, 1x2, e.g. building entrances) may need 2 steps (onto warp, then into boundary/direction of warp).
*   Critical Game Mechanic: ALWAYS press 'A' to clear dialogue/text BEFORE other inputs.
*   Ghost vs. Psychic: Ghost-type moves are SUPER EFFECTIVE against Psychic.
*   **Trust Game Data (but verify visual interpretation):** Game State Information is the *absolute* source of truth (e.g., for badge count, level caps, 'reachable' flags). However, visual interpretation of how to reach something marked 'reachable' can be flawed (e.g. ledges on Route 2 South blocking path to warp at (4,44) from below Y=48, despite warp being 'reachable').
*   Failed Interaction Loops: If an NPC/object interaction yields no progress after 2-3 varied attempts, a different trigger is likely needed.
*   Coordinate Misreads: Double-check current coordinates from game state before planning movement.
*   DV Checking Tip: Hold START while pressing A on a Pokémon's STATS screen to check DVs.
*   Notepad `replace` Action: `old_text` must be an *exact* match. `overwrite` is safer for large changes.
*   Pokémon Switching Menu: Selecting a Pokémon in the party list opens its action sub-menu. To switch: select 'SWITCH', then select the Pokémon to swap with. Pay close attention to cursor position on screen.
*   Battle Efficiency: Avoid prolonged battles with low EXP yield. Balance agent recommendations with resource cost.
*   Cautious Pathing Under Duress: Prioritize avoiding optional engagements when Pokémon are injured/poisoned. (Contradicts new sticky guideline about overcautious play - need to balance this).
*   Escape Mechanics: Speed-dependent. Lead with fastest Pokémon if escape is critical.
*   WKG Tool Usage: No multi-step tool chains in one turn. Single `manage_world_knowledge` call per operation.
*   **Pathing Precision:** Analyze map memory and screen carefully before committing to multi-step paths, especially near ledges or complex terrain. (Failed attempts on Route 2 South, Turns 1940-1943, 1947). Re-check tile types if blocked.
*   **Battle Risk Assessment (RATTATA T1974):** Letting SPARKY drop to 1HP was very risky. While new guidelines suggest less caution, this was extreme. Balance risk with available healing/resources.
*   **Pokédex Evaluation Correction:** Professor Oak or his aides evaluate the Pokédex in person (Corrected from PC evaluation note from Viridian Forest sign).

## Defeated Trainers:
*   OAK'S LAB (ID 40) - (6,6) - Rival Pixel (initial battle)
*   Viridian Forest (ID 51) - (3,42) - Lass (Cool Trainer F sprite)
*   Viridian Forest (ID 51) - (28,20) - Youngster (Bug Catcher sprite, VIRIDIANFOREST_YOUNGSTER3)
*   Viridian Forest (ID 51) - (28,34) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER2)
*   Viridian Forest (ID 51) - (14,18) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER5)

## Agent Management (9 Active Agents):
*   **`battle_strategist_agent`**: Defined.
*   **`route_planner_agent`**: Defined.
*   **`level_cap_compliance_agent`**: Defined. **Note:** Use more frequently after level-ups/before bosses. Ensure `num_badges` input reflects Game State.
*   **`wild_encounter_evaluator_agent`**: Defined. Exercise judgment when its suggestions conflict with primary/secondary goals.
*   **`npc_dialogue_analyzer_agent`**: Defined. Low usage. Will review system prompt after obtaining HM Flash, or consider deletion.
*   **`optimal_training_spot_agent`**: Defined.
*   **`item_reminder_agent`**: Defined.
*   **`map_analyzer_agent`**: Defined. Use more consistently when entering new areas or if stuck.
*   **`team_composition_advisor_agent`**: Defined. **Note:** Test before next major gym battle.
*   **Agent Development Plan (Revised T1993):**
    *   `pokedex_progress_agent`: Idea discarded to keep agent slot free.
    *   Review system prompts for all code-enabled agents (`route_planner_agent`, `optimal_training_spot_agent`, `map_analyzer_agent`, `team_composition_advisor_agent`) after obtaining HM Flash, to ensure optimal configuration (leveraging auto-provided variables, not defining them in input schemas).

## World Knowledge Graph Notes:
*   **Critical:** Record inter-map transitions IMMEDIATELY.
*   Node `cab3db02-4a0b-4da0-9faa-8d6af20bfe21` is the correct Route 2 South Entrance from Viridian City.

## Area Notes:
### Route 2 (ID 13) - Current Area
*   **Objective:** Find Professor Oak's Aide for HM05 FLASH (10 Pokédex entries met!).
*   **Current Location:** (8,72) - Ground (South Part, just re-entered from Viridian City)
*   **Items:** Two Poké Balls visible on map (14,55) and (14,46) but listed as `reachable: no` (on inaccessible eastern ledge path).
*   **Encounters:** SKITTER (RATTATA) (Lv8, caught, sent to PC). Requirement for Flash met.
*   **Navigation:** Western path warp to Viridian Forest South Gate at (4,44) is listed as 'reachable: yes' in game state. Previous attempts to reach it from south of Y=48 were blocked by ledges. Current hypothesis is that there IS a path. Re-attempting path north along X=8.

## Reflection Insights (Turn 1993):
*   **Battle Risk Assessment (RATTATA T1974):** Letting SPARKY drop to 1HP was very risky. Need to balance new 'less cautious' guideline with common sense, especially with no items in battle.
*   **Pathing Precision (Route 2 South, T1940-1947, T1982-1987):** Multiple pathing attempts blocked by impassable tiles/ledges. Analyze screen and map memory more carefully. Trust map memory for tile types.
*   **Agent Usage Reminder:** Use `map_analyzer_agent` more consistently when entering new routes or areas, or if stuck.
*   **Notepad Management:** `overwrite` is good for major refactors. Careful with Nicknaming screen inputs; 'Start' to confirm.
*   **Pokédex Evaluation Correction:** Confirmed Professor Oak or aides evaluate in person, not via PC.
*   **WKG:** Manage diligently. Deleted redundant node `4c2a58ce-ef8d-4448-9c82-8051f83a4946`.