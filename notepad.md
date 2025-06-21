# Gem's Strategic Journal (v16.0)

## I. Core Principles & Lessons Learned
- **Refine, Don't Discard:** An underperforming tool needs to be fixed, not abandoned. A working-but-imperfect tool is better than no progress.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Trust the Game State:** If `Reachable Unseen Tiles` is not empty, that is the path. Do not declare a dead end prematurely.
- **Correct Your Own Assumptions:** Do not blame a tool for a failure that stems from your own misunderstanding of game mechanics. Verify the facts before refining a tool.
- **Execute Agent Plans Fully:** Trust agents like `battle_menu_navigator` to provide complete, correct action sequences. Execute the full sequence in a single turn for maximum efficiency.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Usage:** A fainted POKéMON can still use field moves like CUT.
- **Type Matchups (Verified):** Flying is 2x vs. Ground. Flying vs. Grass/Poison is a neutral 1x multiplier (2x vs Grass * 0.5x vs Poison).
- **Move Compatibility (CRITICAL DISCOVERY):** SUBTERRA (Diglett) cannot learn HM05 Flash. PULSAR (Magnemite) can. Trust in-game 'ABLE'/'NOT ABLE' feedback.
- **Pokémon Evolutions:** ECHO (Zubat) -> Golbat at Lv. 22.
- **New Moves Learned:** ECHO (Golbat) learned Wing Attack, PULSAR (Magnemite) learned Flash, NIGHTSHADE (Gloom) learned Mega Drain.
- **EXP. All Mechanics (Verified):** EXP is distributed to all non-fainted party Pokémon.

## III. World Intel & Navigation
- **CRITICAL NAVIGATION LESSON:** The correct path to Lavender Town is south on Route 10, past the Pokémon Center and cuttable trees. My backtracking into Rock Tunnel was a major error based on a flawed assumption.
- **CRITICAL NAVIGATION LESSON:** Route 2 is segmented. The Diglett's Cave exit at (13, 11) leads to a small, isolated northern section.
- **Lt. Surge's Raichu (Lv. 29):** Knows Body Slam and Surf.
- **Recurring Obstacles:** Trees in Vermilion City (16,19) and Route 2 (16,23) respawn.
- **Route 11 Gatehouse Split:** West entrance leads to a small room with no access to the eastern section.
- **Item Discovery:** MOON STONE on Route 2 (south section).

## IV. Agent & Tool Strategy
### Agent Refinement Protocol (MANDATORY - v2)
1.  **Hypothesize & Isolate:** Form a specific, small hypothesis for what is failing (e.g., "agent fails at ledges"). Test this in a controlled, simple scenario first, not a complex live one.
2.  **Iterate Small:** Make small, incremental changes to the prompt. Avoid large, complex rewrites.
3.  **Manual Unstick:** If an agent is stuck in a logic loop, take 1-2 manual steps to change the game state (e.g., reveal a new tile). This provides new input that can break the loop. Progress over perfection.
4.  **Validate, then Deploy:** Only use the refined agent for critical tasks after it passes a simple validation test.

### Agent Status & Refinement Plan
- **`route_navigator_agent`:** **PRIORITY REFINEMENT.** The agent has pathfinding flaws. Current hypothesis: It misinterprets impassable walls or elevation rules. **Plan:** After the current battle and exploration of Route 10, I will create a simple, controlled test case (e.g., a small room with a single wall) to isolate and fix the logic flaw. I will not abandon this tool.
- **`battle_move_advisor_agent`:** Reliable.
- **`battle_menu_navigator`:** Reliable. I must execute its full button sequences.
- **`trainer_hunter_agent`:** Tested successfully.
- **`pokemon_evolution_advisor`:** Tested successfully.

## V. Old/Incorrect Notes (for reference)
- ~~`battle_move_advisor_agent` fixed to handle 4x weakness~~ (This was based on my own misunderstanding).
- ~~Trust the `route_navigator_agent`~~ (The agent has a confirmed flaw with elevation and must be fixed before being trusted).