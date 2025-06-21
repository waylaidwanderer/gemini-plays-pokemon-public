# Gem's Strategic Journal (v14.0)

## I. Core Principles & Lessons Learned
- **Refine, Don't Discard:** An underperforming tool needs to be fixed, not abandoned. A working-but-imperfect tool is better than no progress.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Trust, but REFINE:** Trust agent outputs as a starting point, but ALWAYS verify their performance.
- **Trust the Game State:** If `Reachable Unseen Tiles` is not empty, that is the path. Do not declare a dead end prematurely.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Usage:** A fainted POKéMON can still use field moves like CUT.
- **Type Matchups (Verified):** Flying is 2x vs. Ground.
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
- **`route_navigator_agent`:** **TOP PRIORITY REFINEMENT.** The agent currently fails to account for HMs.
    - **Plan:** Update the agent's system prompt. The new instructions will require the agent's Python code to identify HM-removable obstacles (e.g., `<Tile type="cuttable">`). If such an obstacle blocks the only path, the agent should not report `path_found: false`. Instead, it should find a path *to the tile adjacent to the obstacle* and include a new field in its JSON output, `required_hm_actions`, listing the HM needed and the coordinates of the obstacle. This will allow me to manually use the HM and then recall the agent to find the path from the new position.
- **`battle_move_advisor_agent`:** Fixed to handle 4x weakness.
- **`trainer_hunter_agent`:** Rebuilt and tested successfully.
- **`pokemon_evolution_advisor`:** Tested successfully.
- **`tm_usage_advisor_agent`:** Awaiting stat data for testing.
- **`catch_advisor_agent`:** Awaiting first test case.

## V. Future Agent Ideas
- **EXP Gain Tracker/Leveling Planner:** Could track EXP gains and suggest efficient leveling paths to reach the cap for multiple Pokémon, avoiding over-leveling.

- **TM/HM Compatibility Agent:** Given a TM/HM and my roster, it would identify all compatible Pokémon.
- **Item Usage Advisor:** Analyzes my inventory and team to suggest optimal item uses, like which TM to teach to which Pokémon.

- **`battle_menu_navigator` Expansion Idea:** Could be expanded to handle item usage or running from battles automatically.

- **`battle_menu_navigator` Expansion Idea:** Could be expanded to handle item usage or running from battles automatically.

- **`battle_move_advisor_agent`:** Fixed a critical flaw in its Gen 1 type chart knowledge (incorrectly had Ground immune to Flying). It is now reliable.
- **`battle_menu_navigator`:** Fixed a flawed assumption about the move menu layout (it's a vertical list, not a 2x2 grid). It is now reliable for move selection.
- **Trust the `route_navigator_agent`:** My manual override of the agent's path led me to a dead end. The agent's global view is more reliable than my intuition. I must trust its pathing, even if it seems to backtrack.