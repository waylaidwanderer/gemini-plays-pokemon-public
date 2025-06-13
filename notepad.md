# Pokémon Yellow Legacy - Hard Mode Notes - Gem

## Game Info
*   **Player Name:** Gem
*   **Rival Name:** Pixel
*   **Current Badges:** 0
*   **Current Level Cap:** 12 (0 badges)
*   **Pokédex:** 6/151
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
*   **Pewter Gym Preparation:** Upon reaching Pewter City, identify Gym type, Leader's Pokémon/levels. Train team to cap (12) by battling trainers on Route 2 (North) and Diglett's Cave if accessible/appropriate. Prioritize type advantages.
*   **Agent Testing Plan:** After healing the party in Viridian City, systematically test `map_analyzer_agent`, `item_reminder_agent`, and `optimal_training_spot_agent` in Viridian City or on Route 2.

## Pokémon Party & Log (Current as of Turn 1591):
*   **GOTTSAMER (METAPOD):** Lv7 (0/25 HP, FNT, EXP: 412). ATK 10, DEF 11, SPD 11, SPC 9. TACKLE (14 PP), STRING SHOT (40 PP), HARDEN (30 PP).
*   **NADEL (WEEDLE):** Lv4 (18/18 HP, EXP: 118). POISON STING (35 PP), STRING SHOT (40 PP).
*   **NIGHTSHADE (ODDISH):** Lv8 (12/28 HP, EXP: 397). TACKLE (22 PP), POISONPOWDER (33 PP), LEECH SEED (9 PP).
*   **AEGIS (KAKUNA):** Lv7 (9/24 HP, EXP: 462). POISON STING (25 PP), STRING SHOT (40 PP), HARDEN (30 PP).
*   **SPARKY (PIKACHU):** Lv8 (0/27 HP, FNT, EXP: 594). THUNDERSHOCK (23 PP), GROWL (40 PP), QUICK ATTACK (30 PP), THUNDER WAVE (20 PP).

## Items Obtained:
*   **POKé BALL x7**
*   **OAK'S PARCEL:** Delivered to Prof. Oak (Turn 524).
*   **POKéDEX:** Received from Prof. Oak (Turn 529).

## Discovered Tile Types & Properties:
*   `ground`: Walkable.
*   `impassable`: Walls, counters, etc. Not enterable.
*   `grass`: Wild encounters.
*   `ledge`: Jump down (Y+2 from above the ledge tile), not up. Impassable from below (when player is at Y+1 relative to ledge tile at Y).

## Lessons Learned / Game Mechanics:
*   **Menu Navigation (Naming Screen):** Precise inputs needed. Verify letter before 'A'. 'B' is backspace.
*   **Poison:** Outside battle, -1 HP every 4 steps.
*   **Pikachu Movement:** Can walk through. Adjacent & not facing: 1st press turns, 2nd moves.
*   **Warp Types:** 1x1 instant (move off/on to re-warp). Larger warps (2x1, 1x2, e.g. building entrances) may need 2 steps (onto warp, then into boundary/direction of warp).
*   **Critical Game Mechanic:** ALWAYS press 'A' to clear dialogue/text BEFORE other inputs.
*   **Ghost vs. Psychic:** Ghost-type moves are SUPER EFFECTIVE against Psychic.
*   **Trust Game Data:** Trust `Reachable Unseen Tiles` list. Game State is source of truth for levels, etc.
*   **Failed Interaction Loops:** If an NPC/object interaction yields no progress after 2-3 varied attempts, a different trigger is likely needed. (Youngster Route 1 ~T350s, Viridian Forest Youngster T739-743).
*   **Coordinate Misreads:** Double-check current coordinates from game state before planning movement. (Corrected T1581).
*   **DV Checking Tip:** Hold START while pressing A on a Pokémon's STATS screen to check DVs. (Old Man Viridian, T707).
*   **Notepad `replace` Action:** `old_text` must be an *exact* match. If `replace` fails repeatedly, consider `overwrite` for the section or entire notepad.
*   **Pokémon Switching Menu (Corrected T1068-T1085):** Selecting a Pokémon in the party list opens its action sub-menu (STATS, SWITCH, CANCEL). To switch: select 'SWITCH', then select the Pokémon to swap with from the party list. Press 'A' on target, then 'A' on 'SWITCH', then navigate to other Pokémon and 'A' to confirm.
*   **Battle Efficiency (Critique T1231 & T1260):** Avoid prolonged battles with highly defensive Pokémon (e.g., Harden-spamming Metapod) or very low-level Pokémon if they offer low EXP for the time/PP invested. Balance agent recommendations (like `wild_encounter_evaluator_agent`) with own judgment on resource cost and battle efficiency. Prioritize trainer battles for EXP.
*   **Cautious Pathing Under Duress (Critique T1535 & T1540):** When a Pokémon is critically injured and poisoned, pathing decisions must prioritize avoiding all optional engagements, even if it means a slightly longer route. The risk of being forced into a battle outweighs the minor time save of a more direct, but dangerous, path. (Failed to avoid VIRIDIANFOREST_YOUNGSTER5 at (14,18) on Turn 1519).
*   **Escape Mechanics (Learned T1553-1555, T1573-1579):** Escape chance depends on lead Pokémon's Speed vs. wild's Speed. If Speed >= wild's, escape is guaranteed. If lower, chance increases with attempts. If escape is critical, lead with fastest available Pokémon that can survive a hit.
*   **WKG Tool Usage:** Multi-step tool chains requiring output from a previous tool in the *same turn* (e.g., `tools_results.0.node_id`) are not supported. Break these into sequential, single operations per turn. (Learned T1584-1588).

## Defeated Trainers:
*   OAK'S LAB (ID 40) - (6,6) - Rival Pixel (initial battle)
*   Viridian Forest (ID 51) - (3,42) - Lass (Cool Trainer F sprite)
*   Viridian Forest (ID 51) - (28,20) - Youngster (Bug Catcher sprite, VIRIDIANFOREST_YOUNGSTER3)
*   Viridian Forest (ID 51) - (28,34) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER2)
*   Viridian Forest (ID 51) - (14,18) - Bug Catcher (Youngster sprite, VIRIDIANFOREST_YOUNGSTER5) - Defeated Lv6 CATERPIE & Lv6 METAPOD.

## Agent Definitions & Usage Log (9 Active Agents):
*   **`battle_strategist_agent`**: Defined. Use for significant trainer battles.
*   **`route_planner_agent`**: Defined. Observation (T542): Failed intra-map on Route 1. System prompt needs refinement for limitations. (Used frequently for Viridian Forest exit T1582).
*   **`level_cap_compliance_agent`**: Defined. Used T407. **Note:** Use more frequently after level-ups/before bosses.
*   **`wild_encounter_evaluator_agent`**: Defined. Used frequently. Note: Balance its EXP recommendations with battle efficiency and resource cost.
*   **`npc_dialogue_analyzer_agent`**: Defined. Low usage. **Note:** Evaluate utility further; consider deletion if not useful.
*   **`optimal_training_spot_agent`**: Defined. Untested.
*   **`item_reminder_agent`**: Defined. Reminds about nearby uncollected items. Untested.
*   **`map_analyzer_agent`**: Defined (T1261). Untested. **Plan:** Test after healing party in Viridian City.
*   **`team_composition_advisor_agent`**: Defined (T1561). Recommends team for major battles.
*   **Agent Review Note:** Periodically review all agents for relevance and potential improvements.

## World Knowledge Graph Notes:
*   **Critical:** Record inter-map transitions IMMEDIATELY using `manage_world_knowledge` upon map_id change.

## Area Notes:
### Route 2 (ID 13) - Current Area
*   **Objective:** Reach Viridian City to heal party.
*   **Current Location:** (4,61) (Turn 1591).
*   **Items:** Poké Ball at (14,55) - unreachable. Poké Ball at (14,46) - unreachable.
*   **Encounters:** Vulpix (Lv5, ran T700). PIDGEY (Lv8, ran T1572). PIDGEY (Lv7, ran T1580).

### Viridian Forest (ID 51) - Previously Explored
*   **Objective:** Exited south to heal party.
*   **Key NPCs (Non-Battling):** Youngster (17,44), Youngster (28,41) - Tip: Carry extra Poké Balls.
*   **Items:** Poké Ball at (13,30) - unreachable. POTION x1 at (26,12) (Turn 1366) - Used.
*   **Encounters:** ODDISH (Lv6, ran T1564).
*   **Pokédex Evaluation:** Contact PROF.OAK via PC to get your POKéDEX evaluated (Sign in Viridian Forest at (27,18)).

## Interaction Attempts & NPC Behavior
*   **VIRIDIANCITY_YOUNGSTER1 (T1632):** Attempted interaction at (15,20). NPC moved to (13,20) as 'A' was pressed. (1st fail with this specific Youngster).