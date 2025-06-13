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
*   **HM05 FLASH Acquisition:** Catch 1 more unique Pokémon species (total 10 in Pokédex). Then, travel to Route 2 (North of Viridian City, through Viridian Forest) to find Professor Oak's Aide who gives HM05 FLASH. Look for encounters en route to Route 2.
*   **Pokédex Completion Strategy:** Actively seek out and attempt to catch new Pokémon species in all encounter areas, prioritizing routes leading to current objectives.

## Pokémon Party & Log (Current as of Turn 1923):
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
*   **Battle Menu Navigation (2x2 Layout):** FIGHT (top-left), PKMN (top-right), ITEM (bottom-left), RUN (bottom-right). Navigate with appropriate directional inputs. Pay close attention to screen text for current cursor position.
*   **Party List Selection:** Pressing 'A' on a Pokémon in the 'Choose a POKéMON' list *selects* it and brings up its sub-menu (SWITCH, STATS, CANCEL). Pay close attention to screen text to confirm sub-menu vs. main list.
*   Menu Navigation (Naming Screen): Precise inputs needed. Verify letter before 'A'. 'B' is backspace. 'START' or 'END' confirms name.
*   Poison: Outside battle, -1 HP every 4 steps.
*   Pikachu Movement: Can walk through. Adjacent & not facing: 1st press turns, 2nd moves.
*   Warp Types: 1x1 instant (move off/on to re-warp). Larger warps (2x1, 1x2, e.g. building entrances) may need 2 steps (onto warp, then into boundary/direction of warp).
*   Critical Game Mechanic: ALWAYS press 'A' to clear dialogue/text BEFORE other inputs.
*   Ghost vs. Psychic: Ghost-type moves are SUPER EFFECTIVE against Psychic.
*   **Trust Game Data:** Game State Information is the *absolute* source of truth (e.g., for badge count, level caps). Do not question it.
*   Failed Interaction Loops: If an NPC/object interaction yields no progress after 2-3 varied attempts, a different trigger is likely needed.
*   Coordinate Misreads: Double-check current coordinates from game state before planning movement.
*   DV Checking Tip: Hold START while pressing A on a Pokémon's STATS screen to check DVs.
*   Notepad `replace` Action: `old_text` must be an *exact* match. `overwrite` is safer for large changes.
*   Pokémon Switching Menu: Selecting a Pokémon in the party list opens its action sub-menu. To switch: select 'SWITCH', then select the Pokémon to swap with. Pay close attention to cursor position on screen.
*   Battle Efficiency: Avoid prolonged battles with low EXP yield. Balance agent recommendations with resource cost.
*   Cautious Pathing Under Duress: Prioritize avoiding optional engagements when Pokémon are injured/poisoned.
*   Escape Mechanics: Speed-dependent. Lead with fastest Pokémon if escape is critical.
*   WKG Tool Usage: No multi-step tool chains in one turn.
*   Battle Menu Tool: If manual navigation fails, use `select_battle_option` tool for main menu.
*   Stat Drops: Account for stat changes (e.g., Growl lowering Attack) when choosing moves.
*   Goal Prioritization: Re-evaluate tertiary goals if primary/secondary goals can be advanced more directly.

## Defeated Trainers:
*   OAK'S LAB (ID 40) - (6,6) - Rival Pixel (initial battle)
*   Viridian Forest (ID 51) - (3,42) - Lass (Cool Trainer F sprite)
*   Viridian Forest (ID 51) - (28,20) - Youngster (Bug Catcher sprite, VIRIDIANFOREST_YOUNGSTER3)
*   Viridian Forest (ID 51) - (28,34) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER2)
*   Viridian Forest (ID 51) - (14,18) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER5)
*   PEWTER_GYM (ID 4) - (3,1) - Gym Leader Brock
*   PEWTER_GYM (ID 4) - (3,4) - Jr. Trainer M

## Agent Management (9 Active Agents):
*   **`battle_strategist_agent`**: Defined.
*   **`route_planner_agent`**: Defined.
*   **`level_cap_compliance_agent`**: Defined. **Note:** Use more frequently after level-ups/before bosses. Ensure `num_badges` input reflects Game State.
*   **`wild_encounter_evaluator_agent`**: Defined. Exercise judgment when its suggestions conflict with primary/secondary goals.
*   **`npc_dialogue_analyzer_agent`**: Defined. Low usage. Will review system prompt or delete after reaching next town/milestone.
*   **`optimal_training_spot_agent`**: Defined.
*   **`item_reminder_agent`**: Defined.
*   **`map_analyzer_agent`**: Defined.
*   **`team_composition_advisor_agent`**: Defined. **Note:** Test before next major gym battle.
*   **Agent Development Plan:
    *   `pokedex_progress_agent`: Idea discarded for now to keep agent slot free.
    *   Review system prompts for all code-enabled agents (`route_planner_agent`, `optimal_training_spot_agent`, `map_analyzer_agent`, `team_composition_advisor_agent`) after reaching the next town or significant game milestone to ensure optimal configuration and that they leverage auto-provided variables (`map_xml_string`, `world_knowledge_graph_json_string`) and do not define them in input schemas.

## World Knowledge Graph Notes:
*   **Critical:** Record inter-map transitions IMMEDIATELY.

## Area Notes:
### Route 22 (ID 33) - Current Area
*   **Objective:** Catch 1 more unique Pokémon for HM Flash. Proceed to Route 2 via Viridian Forest.
*   **Current Location:** (38,13) - Ground
*   **Items:** None found.
*   **Encounters:** FURYFIST (MANKEY) (Lv4, caught). SPIKE (NIDORAN♂) (Lv3, caught). BELLADONNA (NIDORAN♀) (Lv4, caught, sent to PC).
*   **Pokédex Evaluation:** Professor Oak or his aides evaluate the Pokédex in person (likely not via PC).

## AI Feedback & Action Plan (Turn 1923):
*   **Battle Tactics:** Acknowledged that THUNDERSHOCK was better than QUICK ATTACK against NIDORAN♀ after SPARKY's ATTACK was lowered by GROWL.
*   **Goal Refinement:** With NIDORAN♀ caught (Pokédex 9/10), the tertiary goal is now 'Proceed to Route 2 via Viridian Forest, seeking the final unique Pokémon encounter en route to obtain HM05 FLASH.' This is more direct than clearing all unseen tiles on Route 22.
*   **Agent Development:** Addressed `pokedex_progress_agent` decision and scheduled review of other agent prompts.
*   **Poké Ball Management:** 3 Poké Balls remaining. Be cautious.
*   **Notepad Management:** Will use `overwrite` for major refactors or when `replace` fails due to subtle `old_text` mismatches. Will be careful with Nicknaming screen inputs.