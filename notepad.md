# Pokémon Yellow Legacy - Hard Mode Notes - Gem

## Game Info
*   **Player Name:** Gem
*   **Rival Name:** Pixel
*   **Current Badges:** 0
*   **Current Level Cap:** 12 (0 badges)
*   **Pokédex:** 5/151
*   **Money:** ¥632

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
*   **Heal Critically Injured Party (COMPLETE):** Party was healed after blacking out in Viridian Forest and returning to Viridian City Pokémon Center.
*   **Pokédex Completion Strategy:** Actively seek out and attempt to catch new Pokémon species in all encounter areas. Pay close attention to NPC dialogue for hints.
*   **Pewter Gym Preparation (Paused):** Upon reaching Pewter City (after healing), identify Gym type, Leader's Pokémon/levels. Train team to cap (12), prioritizing type advantages.

## Pokémon Party & Log (Current as of Turn 1190):
*   **GOTTSAMER (CATERPIE):** Lv4 (18/18 HP, EXP: 118). TACKLE (35 PP), STRING SHOT (40 PP).
*   **NADEL (WEEDLE):** Lv4 (18/18 HP, EXP: 118). POISON STING (35 PP), STRING SHOT (40 PP).
*   **NIGHTSHADE (ODDISH):** Lv6 (23/23 HP, EXP: 179). TACKLE (35 PP), POISONPOWDER (35 PP).
*   **AEGIS (KAKUNA):** Lv7 (24/24 HP, EXP: 410). POISON STING (35 PP), STRING SHOT (40 PP), HARDEN (30 PP).
*   **SPARKY (PIKACHU):** Lv7 (25/25 HP, EXP: 466). THUNDERSHOCK (30 PP), GROWL (40 PP), QUICK ATTACK (30 PP).

## Items Obtained:
*   **POKé BALL x7**
*   **OAK'S PARCEL:** Delivered to Prof. Oak (Turn 524).
*   **POKéDEX:** Received from Prof. Oak (Turn 529).

## Discovered Tile Types & Properties:
*   `ground`: Walkable.
*   `impassable`: Walls, counters, etc. Not enterable.
*   `grass`: Wild encounters.
*   `ledge`: Jump down (Y+2), not up.

## Lessons Learned / Game Mechanics:
*   **Menu Navigation (Naming Screen):** Precise inputs needed. Verify letter before 'A'. 'B' is backspace.
*   **Poison:** Outside battle, -1 HP every 4 steps.
*   **Pikachu Movement:** Can walk through. Adjacent & not facing: 1st press turns, 2nd moves.
*   **Ledge Traversal:** One 'Down' press from above moves to Y+2.
*   **Warp Types:** 1x1 instant (move off/on to re-warp). Larger warps (2x1, 1x2) need 2 steps (onto warp, then into boundary).
*   **Critical Game Mechanic:** ALWAYS press 'A' to clear dialogue/text BEFORE other inputs.
*   **Ghost vs. Psychic:** Ghost-type moves are SUPER EFFECTIVE against Psychic.
*   **Trust Game Data:** Trust `Reachable Unseen Tiles` list. Game State is source of truth for levels, etc.
*   **Failed Interaction Loops:** If an NPC/object interaction yields no progress after 2-3 varied attempts, a different trigger is likely needed. (Youngster Route 1 ~T350s, Viridian Forest Youngster T739-743).
*   **Coordinate Misreads:** Double-check current coordinates from game state before planning movement.
*   **DV Checking Tip:** Hold START while pressing A on a Pokémon's STATS screen to check DVs. (Old Man Viridian, T707).
*   **Notepad `replace` Action:** `old_text` must be an *exact* match. If `replace` fails repeatedly, consider `overwrite` for the section or entire notepad.
*   **Pokémon Switching Menu (Corrected T1068-T1085):** Selecting a Pokémon in the party list opens its action sub-menu (STATS, SWITCH, CANCEL). To switch: select 'SWITCH', then select the Pokémon to swap with from the party list. Press 'A' on target, then 'A' on 'SWITCH', then navigate to other Pokémon and 'A' to confirm.

## Active Hypotheses / Things to Test:
*   Can the `route_planner_agent` be improved for intra-map pathing with better prompting?
*   Are there specific conditions to trigger battles with certain NPCs who initially only offer dialogue (e.g., Youngster in Viridian Forest)?

## Defeated Trainers:
*   OAK'S LAB (ID 40) - (6,6) - Rival Pixel (initial battle)
*   Viridian Forest (ID 51) - (3,42) - Lass (Cool Trainer F sprite)

## Agent Definitions & Usage Log:
*   **`battle_strategist_agent`**: Defined. Use for significant trainer battles. (Called T1109 vs Bug Catcher's Metapod).
*   **`route_planner_agent`**: Defined. **Observation (T542):** Failed intra-map on Route 1. System prompt needs refinement for limitations.
*   **`rom_hack_mechanic_analyzer_agent`**: Defined. Use for deducing new mechanics.
*   **`level_cap_compliance_agent`**: Defined. Used T407 (all okay).
*   **`wild_encounter_evaluator_agent`**: Defined. Used T929, T1012, T1031, T1037, T1063, T1065, T1067, T1069, T1088 (PIDGEY - RUN), T1090 (PIDGEY - RUN), T1092 (PIDGEY - RUN).
*   **`npc_dialogue_analyzer_agent`**: Defined. Low usage, consider more frequent application.
*   **`pokedex_tracker_agent`**: Defined. Untested.
*   **`optimal_training_spot_agent`**: Defined. Untested.
*   **`item_reminder_agent`**: Defined. Reminds about nearby uncollected items. Untested.
*   **`hm_obstacle_identifier_agent`**: DELETED (Turn 1086, unused).

## World Knowledge Graph Notes:
*   **Critical:** Record inter-map transitions IMMEDIATELY using `manage_world_knowledge` upon map_id change.

## Area Notes:
### Viridian Forest (ID 51) - Current Area
*   **Objective:** Retreat south to Viridian City Pokémon Center for healing.
*   **Key NPCs:** Youngster (17,44) - non-battling so far (marked). Lass (3,42) - defeated (marked). Youngster (31,34) - unencountered. Youngster (28,41) - unencountered. Youngster (31,20) - unencountered.
*   **Items:** Poké Ball found (2,32). Poké Ball at (13,30) - unreachable (noted from map sprites).
*   **Encounters:** Weedle, Caterpie, Kakuna, Oddish, Pidgeotto (Lv9, ran), Pidgey (Lv7, ran).
*   **Encounter Log (Turn 1088-1094):** At (26,24), encountered Lv7 PIDGEY. AEGIS led. Failed to run twice; AEGIS took 2 GUST hits (HP to 2/24). Successfully ran on 3rd attempt.
*   **Current Location:** (26,24). Immediate plan: Switch GOTTSAMER to lead, then navigate to south exit warp at (17,48).