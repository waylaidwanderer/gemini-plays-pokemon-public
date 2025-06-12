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
*   I will actively look for opportunities to deploy the defined agents (`battle_strategist_agent`, `route_planner_agent`, `rom_hack_mechanic_analyzer_agent`) to test their efficacy and integrate them into my gameplay loop.

## World Knowledge Graph Notes:
*   Record inter-map transitions (map boundary, warps) IMMEDIATELY using `manage_world_knowledge`.

## Pallet Town NPCs & Interactions:
*   **Daisy (Rival's House @ 3,4):** Told me Pixel is looking for me and went to Prof. Oak's Lab. She blocks movement on her tile.

*   **Critical Game Mechanic:** ALWAYS press 'A' to clear any on-screen dialogue or text BEFORE attempting any other input (movement, interaction, menu). Failure to do so will result in the input being ignored or only clearing the text.

## Custom Agent Notes:
*   `battle_strategist_agent` defined. Will use for next significant trainer battle.
*   `route_planner_agent` defined.
*   `rom_hack_mechanic_analyzer_agent` defined.

## Oak's Lab - Rival Battle (Resolved)
*   The rival battle with Pixel was triggered by attempting to leave Oak's Lab via the exit at (6,12) after receiving Pikachu.
*   Pixel was defeated.
*   Professor Oak then gave me the Pokédex.

## Reflection Notes (Turn 207)
*   Revisit custom agent creation soon. Currently, ideas are noted but no agents created.
*   Lesson Learned: Recognize and break out of failed interaction loops much sooner. If an NPC interaction doesn't progress after 2-3 attempts with slightly varied approaches (e.g., clearing dialogue, re-interacting), a different trigger is likely needed (e.g., talking to a different NPC, trying to leave the area, interacting with an object).

## Oak's Lab Notes (Current Map: ID 40)
*   Player at (1,6). Pikachu at (1,5).
*   Professor Oak at (6,3). Gave Pikachu and Pokédex. Dialogue now "Go to the next town."
*   Two Scientists:
    *   OAKSLAB_SCIENTIST1 at (3,11), facing right.
    *   OAKSLAB_SCIENTIST2 at (9,11), facing right.
*   Two Pokédexes on tables:
    *   OAKSLAB_POKEDEX1 at (3,2).
    *   OAKSLAB_POKEDEX2 at (4,2).

## Type Matchup Changes (Learned):
*   Ghost-type moves are SUPER EFFECTIVE against Psychic-type Pokémon. (Learned from OAKSLAB_SCIENTIST1 at (3,11) on Turn 264)

## Pallet Town Exploration Notes (Turn 291):
*   The 'Reachable Unseen Tiles' list includes tiles at X=20 (e.g., (20,3) to (20,8)). However, visual observation and map memory suggest X=20 is an impassable boundary. These tiles are likely not actually reachable by normal movement.