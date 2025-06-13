## Game Info
*   **Player Name:** Gem
*   **Rival Name:** Pixel
*   **Current Badges:** 0 (Game State is Source of Truth)
*   **Current Level Cap:** 12 (0 badges - Game State is Source of Truth)
*   **Pokédex:** 7/151 (Nidoran♂ will make it 8 if caught)
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
*   **Pokédex Completion Strategy:** Actively seek out and attempt to catch new Pokémon species in all encounter areas. Pay close attention to NPC dialogue for hints.
*   **HM05 FLASH Acquisition:** Catch Nidoran♂ (current battle), then 1 more unique Pokémon species (total 10 in Pokédex). Then, travel to Route 2 (North of Viridian City, through Viridian Forest) to find Professor Oak's Aide who gives HM05 FLASH. Explore Route 22 for potential new catches.
*   **Agent Testing Plan:** Test `team_composition_advisor_agent` before next major gym battle. Consider defining `pokedex_progress_agent` or removing the idea from notepad.

## Pokémon Party & Log (Current as of Turn 1770):
*   **GOTTSAMER (METAPOD):** Lv7 (17/25 HP, EXP: 412). ATK 10, DEF 11, SPD 11, SPC 9. TACKLE (35 PP), STRING SHOT (40 PP), HARDEN (30 PP)
*   **NADEL (WEEDLE):** Lv4 (18/18 HP, EXP: 118). POISON STING (35 PP), STRING SHOT (40 PP)
*   **NIGHTSHADE (ODDISH):** Lv8 (28/28 HP, EXP: 397). TACKLE (35 PP), POISONPOWDER (35 PP), LEECH SEED (10 PP)
*   **AEGIS (KAKUNA):** Lv7 (24/24 HP, EXP: 462). POISON STING (35 PP), STRING SHOT (40 PP), HARDEN (30 PP)
*   **SPARKY (PIKACHU):** Lv8 (27/27 HP, EXP: 594). THUNDERSHOCK (30 PP), GROWL (40 PP), QUICK ATTACK (30 PP), THUNDER WAVE (19 PP)
*   **FURYFIST (MANKEY):** Lv4 (17/17 HP, EXP: 64). SCRATCH (35 PP), LEER (30 PP)

## Items Obtained:
*   **POKé BALL x5**
*   **OAK'S PARCEL:** Delivered to Prof. Oak (Turn 524).
*   **POKéDEX:** Received from Prof. Oak (Turn 529).

## Discovered Tile Types & Properties:
*   `ground`: Walkable.
*   `impassable`: Walls, counters, etc. Not enterable.
*   `grass`: Wild encounters.
*   `ledge`: Jump down (Y+2 from above the ledge tile), not up. Impassable from below (when player is at Y+1 relative to ledge tile at Y).

## Lessons Learned / Game Mechanics:
*   **Battle Menu Navigation (2x2 Layout):** FIGHT (top-left), PKMN (top-right), ITEM (bottom-left), RUN (bottom-right). Navigate with appropriate directional inputs. Pay close attention to screen text for current cursor position.
*   Menu Navigation (Naming Screen): Precise inputs needed. Verify letter before 'A'. 'B' is backspace. 'START' confirms name.
*   Poison: Outside battle, -1 HP every 4 steps.
*   Pikachu Movement: Can walk through. Adjacent & not facing: 1st press turns, 2nd moves.
*   Warp Types: 1x1 instant (move off/on to re-warp). Larger warps (2x1, 1x2, e.g. building entrances) may need 2 steps (onto warp, then into boundary/direction of warp).
*   Critical Game Mechanic: ALWAYS press 'A' to clear dialogue/text BEFORE other inputs.
*   Ghost vs. Psychic: Ghost-type moves are SUPER EFFECTIVE against Psychic.
*   **Trust Game Data:** Game State Information is the *absolute* source of truth (e.g., for badge count, level caps). Do not question it.
*   Failed Interaction Loops: If an NPC/object interaction yields no progress after 2-3 varied attempts, a different trigger is likely needed.
*   Coordinate Misreads: Double-check current coordinates from game state before planning movement.
*   DV Checking Tip: Hold START while pressing A on a Pokémon's STATS screen to check DVs.
*   Notepad `replace` Action: `old_text` must be an *exact* match.
*   Pokémon Switching Menu: Selecting a Pokémon in the party list opens its action sub-menu. To switch: select 'SWITCH', then select the Pokémon to swap with.
*   Battle Efficiency: Avoid prolonged battles with low EXP yield. Balance agent recommendations with resource cost.
*   Cautious Pathing Under Duress: Prioritize avoiding optional engagements when Pokémon are injured/poisoned.
*   Escape Mechanics: Speed-dependent. Lead with fastest Pokémon if escape is critical.
*   WKG Tool Usage: No multi-step tool chains in one turn.
*   Battle Menu Tool: If manual navigation fails, use `select_battle_option` tool for main menu.

## Defeated Trainers:
*   OAK'S LAB (ID 40) - (6,6) - Rival Pixel (initial battle)
*   Viridian Forest (ID 51) - (3,42) - Lass (Cool Trainer F sprite)
*   Viridian Forest (ID 51) - (28,20) - Youngster (Bug Catcher sprite, VIRIDIANFOREST_YOUNGSTER3)
*   Viridian Forest (ID 51) - (28,34) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER2)
*   Viridian Forest (ID 51) - (14,18) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER5)
*   PEWTER_GYM (ID 4) - (3,1) - Gym Leader Brock
*   PEWTER_GYM (ID 4) - (3,4) - Jr. Trainer M

## Agent Definitions & Usage Log (9 Active Agents):
*   **`battle_strategist_agent`**: Defined.
*   **`route_planner_agent`**: Defined.
*   **`level_cap_compliance_agent`**: Defined. **Note:** Use more frequently after level-ups/before bosses, especially now that cap is 12.
*   **`wild_encounter_evaluator_agent`**: Defined.
*   **`npc_dialogue_analyzer_agent`**: Defined. Low usage. Re-evaluate utility.
*   **`optimal_training_spot_agent`**: Defined.
*   **`item_reminder_agent`**: Defined.
*   **`map_analyzer_agent`**: Defined.
*   **`team_composition_advisor_agent`**: Defined. **Note:** Test before next major gym battle.
*   **Agent Review Note:** Periodically review all agents. Consider defining `pokedex_progress_agent` or removing the idea.

## World Knowledge Graph Notes:
*   **Critical:** Record inter-map transitions IMMEDIATELY.

## Area Notes:
### Route 22 (ID 33) - Current Area
*   **Objective:** Catch Nidoran♂, then 1 more unique Pokémon. Explore.
*   **Current Location:** (34,10) (In battle with Nidoran♂)
*   **Items:** None found.
*   **Encounters:** FURYFIST (MANKEY) (Lv4, caught). NIDORAN♂ (Lv3, current battle).
*   **Pokédex Evaluation:** Contact PROF.OAK via PC (Sign in Viridian Forest).

## Game State Discrepancies (RESOLVED):
*   Notepad previously incorrectly stated 1 badge. Game State shows 0 badges, which is the source of truth. Level cap is 12.

## New Agent Ideas (From Reflection T1715):
*   **HM Usage Advisor:** (Idea)
*   **Pokédex Progress Agent:** (Idea - consider defining)
*   **Shopping List Agent:** (Idea)

## Agent Development & Review (Post-Reflection T1818):
*   **New Agent Idea:** Define `pokedex_progress_agent` soon. This agent could help identify missing Pokémon in the current area by taking current map, caught list, and potentially known encounter data as input.
*   **Agent Prompts Review:** Review system prompts for all code-enabled agents (`route_planner_agent`, `optimal_training_spot_agent`, `map_analyzer_agent`, `team_composition_advisor_agent`) before next use to ensure they clearly instruct the agent to leverage auto-provided variables like `map_xml_string` and `world_knowledge_graph_json_string`.