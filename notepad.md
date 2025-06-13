# Pokémon Yellow Legacy - Hard Mode Notes - Gem

## Game Info
*   **Player Name:** Gem
*   **Rival Name:** Pixel
*   **Current Badges:** 0
*   **Current Level Cap:** 12 (0 badges)

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
*   **Path to Pewter City for Boulder Badge:** Navigate Route 2 (south section) to the Viridian Forest South Gate warp at (4,44). Traverse Viridian Forest, exploring to find its North Gate. Continue on Route 2 (north section) from there to reach Pewter City.
*   **Pokédex Completion Strategy:** Actively seek out and attempt to catch new Pokémon species in all encounter areas (grass, water, etc.). Pay close attention to NPC dialogue for hints about Pokémon locations or special encounter conditions.
*   **Pewter Gym Preparation:** Upon reaching Pewter City, identify the Gym's type specialty and the Gym Leader's Pokémon lineup and levels. Train SPARKY and any other acquired Pokémon up to the current level cap (12), prioritizing type advantages against the expected Gym opponents.

## Pokémon Party & Log:
*   **SPARKY (Pikachu):** Lv7, 466 EXP (Current cap 12). THUNDERSHOCK PP: 29/30, GROWL PP: 40/40, QUICK ATTACK PP: 29/30. Last healed at Viridian Pokémon Center (Turn 787).
*   **NADEL (Weedle):** Lv4, 64 EXP (Current cap 12). POISON STING PP: 35/35, STRING SHOT PP: 40/40. Caught in Viridian Forest (Turn 870).

## Items Obtained:
*   **OAK'S PARCEL:** Received from Viridian Mart shopkeeper. Delivered to Prof. Oak (Turn 524).
*   **POKéDEX:** Received from Prof. Oak (Turn 529).

## Lessons Learned / Hypotheses / Game Mechanics:
*   **Menu Navigation (Naming Screen):** Precise inputs needed. Verify letter before 'A'. 'B' is backspace.
*   **Poison:** Outside battle, -1 HP every 4 steps.
*   **Pikachu Movement:** Can walk through. Adjacent & not facing: 1st press turns, 2nd moves.
*   **Ledge Traversal:** One 'Down' press from above moves to Y+2.
*   **Warp Types:** 1x1 instant (move off/on to re-warp). Larger warps (2x1, 1x2) need 2 steps (onto warp, then into boundary).
*   **Critical Game Mechanic:** ALWAYS press 'A' to clear dialogue/text BEFORE other inputs.
*   **Ghost vs. Psychic:** Ghost-type moves are SUPER EFFECTIVE against Psychic. (Learned from OAKSLAB_SCIENTIST1).
*   **Trust Game Data:** Trust `Reachable Unseen Tiles` list.
*   **Failed Interaction Loops:** If an NPC/object interaction yields no progress after 2-3 varied attempts, a different trigger is likely needed. Don't repeat failed interactions. (Turn 207, reiterated for Youngster Route 1 ~350s)
*   **Coordinate Misreads:** Double-check current coordinates from game state before planning movement to avoid errors like the one with the Route 1 Youngster. (Turn 359)

## Discovered Tile Types & Properties:
*   `ground`: Walkable.
*   `impassable`: Walls, counters, etc. Not enterable.
*   `grass`: Wild encounters.
*   `ledge`: Jump down (Y+2), not up.

## Defeated Trainers:
*   (Map - Coordinates - Trainer Name)
    *   OAK'S LAB (ID 40) - (6,6) - Rival Pixel (initial battle)

## Custom Agent Notes & Usage:
*   `battle_strategist_agent`: Defined. Use for significant trainer battles.
*   `route_planner_agent`: Defined. **Observation (Turn 542):** Failed to find a path on Route 1 (a fully explored map) for intra-map routing with ledges. **Contingency:** Treat this agent as highly unreliable for complex intra-map pathfinding with obstacles like ledges. Prioritize manual pathfinding for such situations. **Future Consideration:** If failures persist, consider defining a simpler pathing agent or refining input specificity for this one.
*   `rom_hack_mechanic_analyzer_agent`: Defined. Use for deducing new mechanics.
*   `level_cap_compliance_agent`: Defined. Used on Turn 407, all okay.
*   `wild_encounter_evaluator_agent`: Defined. Purpose: Decide fight/run/catch for wild encounters based on party, map, goals. (Use at next wild encounter).
*   `npc_dialogue_analyzer_agent`: Defined. Purpose: Analyze NPC dialogue for clues.

## World Knowledge Graph Notes:
*   **Critical:** Record inter-map transitions (map boundary, warps) IMMEDIATELY using `manage_world_knowledge` upon map_id change. Do not defer.

## Past Area Notes:
*   **Route 1 (ID 12):** Connects Pallet Town (S) and Viridian City (N). Wild: Pidgey, Rattata, Spearow. Youngster (6,27) & Youngster (18,14) gave STAT EXP tips. Sign at (10,28).
*   **Viridian City Pokémon Center (ID: 41):** Used for healing.
*   **Viridian City Mart (ID: 42):** Obtained OAK'S PARCEL. Bought Poké Balls.
*   **Oaks Lab (ID: 40):** Delivered OAK'S PARCEL. Received Pokédex & mission.

## Route 1 Navigation Strategy (Post-Critique & Agent Failure)
*   The `route_planner_agent` failed to find a path on Route 1 (Turn 542). This suggests limitations with the agent for complex intra-map routing with obstacles like ledges.
*   Revised strategy for Route 1 (from south, e.g., (15,29)) to reach northern exit: Head west to find gaps in ledges (e.g., around (9,28)) rather than making wide eastern detours. Ledges are impassable from below; always look for lateral openings. Manual pathing was successful.

## Current Area Notes:
*   **Viridian City (ID: 1):** Arrived from Route 1 at (22,36). The path north to Pewter City is currently blocked. Need to find an NPC or event in Viridian City to open this path. Many reachable unseen tiles still to explore, particularly in the main city area.

## Viridian School House (ID: 43)
*   Blackboard at (4,1) teaches about Sleep (SLP) status and that the item AWAKENING can be used to wake them up. (Learned at Turn 654).
*   Cool Trainer F at (5,2) is a non-battling NPC; she advised reading the blackboard carefully. (Interaction at Turn 657).
*   This area appears fully explored. Exiting.

*   **DV Checking Tip:** Hold START while pressing A on a Pokémon's STATS screen to check its growth potential (DVs). (Learned from Old Man in Viridian City, Turn 707).

## Route 2 Notes:
*   Sign at (6,66) reads: 'ROUTE 2 VIRIDIAN CITY - PEWTER CITY'. (Turn 718)
## Viridian Forest South Gate (ID: 50)
*   Arrived from Route 2 (South Warp at (4,44) on Route 2, arriving at (5,8) here).
*   This is a gatehouse leading to Viridian Forest.
*   Need to explore north to find the exit into the forest.
*   NPCs: Girl at (9,5), Little Girl at (3,6).

## Viridian Forest Notes
*   Youngster (ID 1) at (17,44) with dialogue "I came here with some friends! They're out for POKéMON fights!" did not initiate a battle after 4+ 'A' presses (Turns 739-743). Conclusion: Likely already defeated or non-battling NPC. Moving on.

    *   Viridian Forest (ID 51) - (3,42) - Lass (Cool Trainer F sprite, battled with NIDORAN♀ Lv6, NIDORAN♂ Lv6)

*   Lass at (3,42) mentioned running into an ODDISH in Viridian Forest. (Turn 777).
*   Reminder: Check signs in Viridian Forest when exploration resumes (e.g., sign at (19,46)).
*   **SPARKY (Pikachu):** Healed to full HP (25/25). PP restored.
*   **Money:** Decreased to ¥632 due to blackout.
*   **Secondary Goal Update:** Changed from 'Heal SPARKY' to 'Find the trigger in Viridian City that opens the northern path to Pewter City.'

## Viridian City Update (Turn 795):
*   The old man previously blocking the path north to Route 2 at (20,5) is gone.
*   The path to Route 2 is now clear.
*   Secondary goal 'Find the trigger in Viridian City that opens the northern path to Pewter City' is now considered complete as the path is open.
*   New secondary goal: Travel to Pewter City.

## Agent Ideas (Post-Reflection Turn 831):
*   **Optimal Training Spot Agent:** Input: current party levels, current level cap, (optional) known encounter data for routes. Output: Suggested routes/areas for efficient EXP gain for specific Pokémon under the cap, considering type matchups if possible.
*   **HM Obstacle Identifier Agent:** Input: current map_id, player coordinates, list of HMs owned. Output: List of nearby obstacles (cuttable trees, water, boulders) on the current map and the HM needed to clear them. Could help quickly assess if I can pass new types of barriers.