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
*   **Primary:** Obtain the Boulder Badge from Pewter City Gym.
*   **Secondary:** Stock up on Poké Balls at the PokéMart in Viridian City.
*   **Tertiary (Long-term):** Complete the Pokédex for Professor Oak.
*   **Immediate Plan:** Exit Oak's Lab, travel through Pallet Town and Route 1 to Viridian City. Go to the Mart.
*   **Prepare for Pewter City Gym:** Assess Gym type and plan team accordingly (once known). Train Pokémon towards level cap if necessary.

## Pokémon Party & Log:
*   **SPARKY (Pikachu):** Lv6, 268 EXP (Current cap 12). THUNDERSHOCK PP: 29/30. Healed at Viridian Pokémon Center (Turn 438).

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
*   **WKG Diligence:** Record inter-map transitions *immediately*.
*   **Navigation Inefficiency (Route 1 Ledges):** Jumping ledges without full scouting above led to backtracking. More thorough path assessment needed. (Turn ~330-380)
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
*   `route_planner_agent`: Defined. Consider for complex multi-map or obstacle-heavy navigation.
*   `rom_hack_mechanic_analyzer_agent`: Defined. Use for deducing new mechanics.
*   `level_cap_compliance_agent`: Defined. Used on Turn 407, all okay.
*   `wild_encounter_evaluator_agent`: Defined. Purpose: Decide fight/run/catch for wild encounters based on party, map, goals. (Use at next wild encounter).
*   `npc_dialogue_analyzer_agent`: Defined. Purpose: Analyze NPC dialogue for clues.

## World Knowledge Graph Notes:
*   Record inter-map transitions (map boundary, warps) IMMEDIATELY using `manage_world_knowledge`.
*   Node for Route 1 North Exit (to Viridian) created (ID: ffa853b2-f57b-4a03-8de3-83250b175651 at (12,0)).
*   Ensure to add nodes/edges for Viridian City to Route 1 South, Viridian Pokemon Center, Viridian Mart, and Route 1 South to Pallet Town North.

## Past Area Notes:
*   **Route 1 (ID 12):** Exited at (12,1) (to Viridian) and (12,36) (to Pallet). Wild: Pidgey, Rattata. Trainers: Youngster (Sprite ID 1) at (6,27), Youngster (Sprite ID 2) at (15,14) (unfought). Sign at (10,28).
*   **Viridian City Pokémon Center (ID: 41):** Arrived (4,8). SPARKY healed (Turn 438).
*   **Viridian City Mart (ID: 42):** Arrived (4,8). Received OAK'S PARCEL from shopkeeper (scripted event moved player to (3,6)).

## Current Area Notes:
*   **Oaks Lab (ID: 40):** Player at (6,4). Task: Deliver OAK'S PARCEL to Prof. Oak at (6,3) (Completed). Received Pokédex and mission to complete it.

## Route 1 Navigation Strategy (Post-Critique & Agent Failure)
*   The `route_planner_agent` failed to find a path on Route 1 (Turn 542), despite the map being fully explored. This suggests potential limitations with the agent for complex intra-map routing with obstacles like ledges.
*   Revised strategy for Route 1 (from south, e.g., (15,29)) to reach northern exit: Head west to find gaps in ledges (e.g., around (9,28)) rather than making wide eastern detours. Ledges are impassable from below; always look for lateral openings.