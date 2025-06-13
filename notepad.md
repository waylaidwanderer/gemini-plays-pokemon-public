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
*   **Arrived in Viridian City!** Current position (22,31).
*   **Explore Viridian City:**
    *   Locate Pokémon Center, PokéMart, Gym.
    *   Talk to NPCs (once each).
    *   Heal SPARKY if needed.
    *   Stock up on Poké Balls if possible.
*   **Prepare for Pewter City Gym:**
    *   Assess Gym type and plan team accordingly (once known).
    *   Train Pokémon towards level cap if necessary.

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
    *   OAK'S LAB (ID 40) - (6,12) - Rival Pixel (initial battle)

## Pokémon Log:
*   SPARKY (Pikachu): Lv6, 253 EXP. (Current cap 12). Last EXP gain: +31 vs Wild Pidgey Lv4 (Route 1, (11,8), Turn 406).

## Custom Agent Notes & Usage:
*   `battle_strategist_agent`: Defined. Use for significant trainer battles.
*   `route_planner_agent`: Defined. Consider for complex multi-map or obstacle-heavy navigation.
*   `rom_hack_mechanic_analyzer_agent`: Defined. Use for deducing new mechanics.
*   `level_cap_compliance_agent`: Defined. Used on Turn 407, all okay.
*   `wild_encounter_evaluator_agent`: Defined. Purpose: Decide fight/run/catch for wild encounters based on party, map, goals. (Use at next wild encounter).

## World Knowledge Graph Notes:
*   Record inter-map transitions (map boundary, warps) IMMEDIATELY using `manage_world_knowledge`.
*   Node for Route 1 North Exit (to Viridian) created (ID: ffa853b2-f57b-4a03-8de3-83250b175651 at (12,0)).

## Past Area Notes:
*   **Route 1 (ID 12):**
    *   Exited at (12,1), facing Up. North exit to Viridian City.
    *   Pikachu was at (12,2).
    *   Wild Encounters: Pidgey (Lv3, Lv4), Rattata.
    *   Trainers: Youngster (Sprite ID 1) at (6,27), Youngster (Sprite ID 2) at (15,14). (Neither battled yet).
    *   Sign at (10,28): 'ROUTE 1 PALLET TOWN - VIRIDIAN CITY'.
    *   All reachable unseen tiles explored before leaving.

## Current Area Notes:
*   **Viridian City (ID: 1):**
    *   Player at (36,27), facing Right.
    *   Pikachu at (35,27).
    *   Immediate plan: Find the PokéMart, Gym, and interact with NPCs to find a way north to Pewter City. Rely on live Game State for Reachable Unseen Tiles.
    *   Note: Path north to Route 2 (Pewter City) is currently 'Undiscovered' and 'Reachable: No'. Must find trigger.

## Viridian City Pokémon Center (ID: 41)
*   Arrived at (4,8). Current position (4,4).
*   SPARKY healed (Turn 438)! All HP/PP restored.
*   Next: Explore remaining unseen tiles in Poké Center, then exit and find PokéMart in Viridian City.

## Pokémon Log (Updates)
*   SPARKY (Pikachu): Healed at Viridian Pokémon Center (Turn 438). All HP/PP restored.