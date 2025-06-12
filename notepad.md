# Pokémon Yellow Legacy - Hard Mode Notes - Gem

## Game Info
*   **Player Name:** Gem
*   **Rival Name:** Pixel
*   **Current Badges:** 0
*   **Current Level Cap:** 12 (0 badges)

## Hard Mode Rules (Player-Only Restrictions):
*   **Battle Style:** Set mode (no switching after knocking out an opponent).
*   **No items allowed in battle** — no healing, status cures, or stat boosts.
*   **Level caps:** Your Pokémon cannot exceed the level cap for your current progress.

## Level Cap Table:
*   0 badges: **12**
*   1 badge: **21**
*   2 badges: **24**
*   3 badges: **35**
*   4 badges: **43**
*   5 badges: **50**
*   6 badges: **53**
*   7 badges: **55**
*   8 badges: **65**

## Gameplay & Balance Changes (Noted from Prompt):
*   HMs can be forgotten, used from the menu, cannot be stored in PC.
*   All 151 Pokémon obtainable.
*   Trade evolutions by level.
*   Smarter Trainer AI, anti-sweep.
*   Tougher Boss fights.
*   Dynamic scaling Gyms 4–6.
*   EXP. All obtainable without special requirements.

## Current Objectives & Plans (HOW to achieve goals):
*   **Complete Intro:** Finish naming rival Pixel.
*   **Get First Pokémon:** Likely involves interacting with Prof. Oak, possibly by trying to leave Pallet Town towards Route 1.
*   **Explore Pallet Town:** Visit all houses, talk to NPCs (once).
*   **Meet Professor Oak:** Go to his lab.

## Lessons Learned / Hypotheses / Game Mechanics:
*   **Menu Navigation (Naming Screen):**
    *   Be extremely precise with directional inputs for cursor movement.
    *   Verify the selected letter *before* pressing 'A'.
    *   The keyboard sometimes seems to reset to uppercase or shift cursor unexpectedly. Pay close attention.
    *   Backspace is 'B'. Start confirms name.
*   **Poison:** Outside battle, poisoned Pokémon lose 1 HP every 4 steps. (From prompt)
*   **Pikachu Movement:** Can walk through Pikachu. If adjacent and not facing, 1st press turns, 2nd moves.
*   **Ledge Traversal:** One 'Down' press from above moves to Y+2.
*   **Warp Types:**
    *   1x1 (doors, ladders) are instant. Move off and on to re-warp.
    *   Larger warps (2x1, 1x2 like exit mats) need 2 steps: onto warp, then into boundary/direction.

## Discovered Tile Types & Properties:
*   `ground`: Walkable tile.
*   `impassable`: Walls, counters, rocks, buildings, etc. Cannot be entered.

## Defeated Trainers:
*   (Map - Coordinates - Trainer Name)

## Custom Agent Considerations:
*   Currently, no custom agents will be defined. I will reconsider creating specialized agents if a clear, complex, or repetitive task arises during gameplay that would significantly benefit from one.

## World Knowledge Graph Notes:
*   Record inter-map transitions (map boundary, warps) IMMEDIATELY using `manage_world_knowledge`.

## Pallet Town NPCs & Interactions:
*   **Daisy (Rival's House @ 3,4):** Told me Pixel is looking for me and went to Prof. Oak's Lab. She blocks movement on her tile.

*   **Critical Game Mechanic:** ALWAYS press 'A' to clear any on-screen dialogue or text BEFORE attempting any other input (movement, interaction, menu). Failure to do so will result in the input being ignored or only clearing the text.

## Potential Custom Agent Ideas (From Reflection Turn 156):
*   `battle_strategist_agent`: Input opponent's team, my team, level cap. Output optimal move sequence or switch strategy for Hard Mode (Set mode, no items).
*   `route_planner_agent`: Input target destination (map_id, coordinates), current location. Output optimal path using WKG and map XML for multi-map journeys.
*   `rom_hack_mechanic_analyzer_agent`: For deducing rules of complex new mechanics based on repeated observations.