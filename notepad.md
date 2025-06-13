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
*   **Path to Pewter City for Boulder Badge:** Navigate Viridian Forest, exploring to find its North Gate. Continue on Route 2 (north section) from there to reach Pewter City.
*   **Pokédex Completion Strategy:** Actively seek out and attempt to catch new Pokémon species in all encounter areas. Pay close attention to NPC dialogue for hints.
*   **Pewter Gym Preparation:** Upon reaching Pewter City, identify Gym type, Leader's Pokémon/levels. Train team to cap (12), prioritizing type advantages.

## Pokémon Party & Log (Current as of Turn 1055):
*   **SPARKY (PIKACHU):** Lv7 (8/25 HP, EXP: 466). THUNDERSHOCK (29 PP), GROWL (40 PP), QUICK ATTACK (27 PP).
*   **NADEL (WEEDLE):** Lv4 (7/18 HP, EXP: 64). POISON STING (32 PP), STRING SHOT (40 PP). (Caught Viridian Forest, T870).
*   **NIGHTSHADE (ODDISH):** Lv6 (12/23 HP, EXP: 179). TACKLE (35 PP), POISONPOWDER (35 PP). (Caught Viridian Forest, T922).
*   **GOTTSAMER (CATERPIE):** Lv4 (18/18 HP, EXP: 64). TACKLE (35 PP), STRING SHOT (40 PP). (Caught Viridian Forest, T931).
*   **AEGIS (KAKUNA):** Lv7 (24/24 HP, EXP: 343). POISON STING (35 PP), STRING SHOT (40 PP), HARDEN (30 PP). (Caught Viridian Forest, T1014).

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
*   **Trust Game Data:** Trust `Reachable Unseen Tiles` list.
*   **Failed Interaction Loops:** If an NPC/object interaction yields no progress after 2-3 varied attempts, a different trigger is likely needed. (Youngster Route 1 ~T350s, Viridian Forest Youngster T739-743).
*   **Coordinate Misreads:** Double-check current coordinates from game state before planning movement.
*   **DV Checking Tip:** Hold START while pressing A on a Pokémon's STATS screen to check DVs. (Old Man Viridian, T707).
*   **Notepad `replace` Action:** `old_text` must be an *exact* match. Multiple failures (T996-1026) due to slight mismatches. If `replace` fails repeatedly, consider `overwrite` for the section or entire notepad.

## Active Hypotheses / Things to Test:
*   Can the `route_planner_agent` be improved for intra-map pathing with better prompting?
*   Are there specific conditions to trigger battles with certain NPCs who initially only offer dialogue (e.g., Youngster in Viridian Forest)?

## Defeated Trainers:
*   OAK'S LAB (ID 40) - (6,6) - Rival Pixel (initial battle)
*   Viridian Forest (ID 51) - (3,42) - Lass (Cool Trainer F sprite)

## Agent Definitions & Usage Log:
*   **`battle_strategist_agent`**: Defined. Use for significant trainer battles.
*   **`route_planner_agent`**: Defined. **Observation (T542):** Failed intra-map on Route 1. **(T1038 Update):** System prompt needs refinement for limitations.
*   **`rom_hack_mechanic_analyzer_agent`**: Defined. Use for deducing new mechanics.
*   **`level_cap_compliance_agent`**: Defined. Used T407 (all okay).
*   **`wild_encounter_evaluator_agent`**: Defined. Used T929 (Caterpie - CATCH), T1012 (Kakuna - CATCH), T1031 (Pidgeotto - RUN), T1037 (Kakuna - FIGHT).
*   **`npc_dialogue_analyzer_agent`**: Defined. Low usage, consider more frequent application.
*   **`pokedex_tracker_agent`**: Defined. Untested.
*   **`hm_obstacle_identifier_agent`**: Defined. Untested.
*   **`optimal_training_spot_agent`**: Defined. Untested.
*   **(T1038 New) `exploration_optimizer_agent`**: To be defined. Suggests next exploration target.
*   **(T1038 New) `item_reminder_agent`**: To be defined. Reminds about nearby uncollected items.

## World Knowledge Graph Notes:
*   **Critical:** Record inter-map transitions IMMEDIATELY using `manage_world_knowledge` upon map_id change.

## Area Notes:
### Viridian Forest (ID 51) - Current Area
*   **Objective:** Find North Gate to Route 2 (North).
*   **Key NPCs:** Youngster (17,44) - non-battling so far. Lass (3,42) - defeated.
*   **Items:** Poké Ball found (2,32).
*   **Encounters:** Weedle, Caterpie, Kakuna, Oddish, Pidgeotto (Lv9, ran).
*   **Pathing Issues:** Difficulty navigating around Youngster at (17,44) and impassable tile (17,43). Impassable tree at (22,40).
*   **Current Location (Pre-Battle):** (23,41). Exploring towards unseen tiles in NE (e.g., (26,36)).

### Past Areas (Summary)
*   **Pallet Town (ID 0, etc.):** Started, got Pikachu.
*   **Route 1 (ID 12):** Traversed.
*   **Viridian City (ID 1, etc.):** Got Parcel, Pokédex. Path North to Route 2 opened (T795).
*   **Route 2 (South) (ID 13) / Viridian Forest South Gate (ID 50):** Entry point to Viridian Forest.