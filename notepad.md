# Gem's Strategic Journal (v18.0)

## I. Core Principles & Lessons Learned
- **Verify, Don't Assume:** My location hallucinations were a critical failure. I MUST verify my `map_id` and coordinates from the Game State before every action.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Focus on the Primary Objective:** Side quests and exploration are secondary to advancing the main story. The AI critique was clear: stop procrastinating.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Usage:** A fainted POKéMON can still use field moves like CUT.
- **Type Matchups (Verified):** Flying is 2x vs. Ground. Flying vs. Grass/Poison is a neutral 1x multiplier (2x vs Grass * 0.5x vs Poison).
- **Move Compatibility (CRITICAL DISCOVERY):** SUBTERRA (Diglett) cannot learn HM05 Flash. PULSAR (Magnemite) can. Trust in-game 'ABLE'/'NOT ABLE' feedback.
- **Pokémon Evolutions:** ECHO (Zubat) -> Golbat at Lv. 22.
- **EXP. All Mechanics (Verified):** EXP is distributed to all non-fainted party Pokémon.

## III. World Intel & Navigation
- **CRITICAL NAVIGATION LESSON:** The correct path to Lavender Town is south on Route 10, past the Pokémon Center and cuttable trees. My backtracking into Rock Tunnel was a major error.
- **CRITICAL NAVIGATION LESSON:** Route 2 is segmented. The Diglett's Cave exit at (13, 11) leads to a small, isolated northern section.
- **Lt. Surge's Raichu (Lv. 29):** Knows Body Slam and Surf.
- **Recurring Obstacles:** Trees in Vermilion City (16,19) and Route 2 (16,23) respawn.
- **Route 11 Gatehouse Split:** West entrance leads to a small room with no access to the eastern section.
- **Item Discovery:** MOON STONE on Route 2 (south section).
- **Lavender Town Intel:** A girl in the Pokémon Center saw Team Rocket kill a Cubone's mother.
- **CRITICAL WARP MECHANIC:** The warp from Mr. Fuji's House is ONE-WAY. It exits to (8, 11) in Lavender Town, not back to the entrance at (4, 14).

## IV. Agent & Tool Strategy
### Agent Refinement Protocol (MANDATORY - v2)
1.  **Hypothesize & Isolate:** Form a specific, small hypothesis for what is failing (e.g., "agent fails at ledges"). Test this in a controlled, simple scenario first, not a complex live one.
2.  **Iterate Small:** Make small, incremental changes to the prompt. Avoid large, complex rewrites.
3.  **Manual Unstick:** If an agent is stuck in a logic loop, take 1-2 manual steps to change the game state (e.g., reveal a new tile). This provides new input that can break the loop. Progress over perfection.
4.  **Validate, then Deploy:** Only use the refined agent for critical tasks after it passes a simple validation test.

### Agent Status & Refinement Plan
- **`route_navigator_agent`:** **UNRELIABLE.** The agent's logic for pathing to impassable targets is flawed. It must be considered a critical point of failure and requires a fundamental rewrite or deletion if it cannot be fixed soon.
- **`battle_move_advisor_agent`:** Reliable.
- **`battle_menu_navigator`:** Reliable.
- **`trainer_hunter_agent`:** Tested successfully.
- **`pokemon_evolution_advisor`:** Untested. Should be used or deleted.
- **`pp_management_advisor_agent`:** **NEW.** Created for PP conservation in dungeons. Untested.
- **`tm_hm_compatibility_agent`:** Untested. Should be used or deleted.

## V. Future Agent Ideas & Cleanup
- **Agent Review:** The `tm_hm_compatibility_agent` and `pokemon_evolution_advisor` agents are unused and should be tested or deleted to free up slots.
- **Item Advisor Agent:** An agent to suggest optimal TM/HM/item usage from inventory. **Decision:** Implement after other priorities are handled.

## VI. Core Gameplay Knowledge & Corrections
- **CRITICAL TYPE MATCHUP CORRECTION:** Ground-type moves ARE super-effective (2x) against Rock/Ground dual-types like Geodude. My assumption that the Ground typing offered resistance was incorrect and led to CRAG fainting. I must verify type matchups before switching.
- **NPC Interaction Protocol:** If an NPC seems unreachable, I must attempt to interact from all adjacent, walkable tiles before assuming they cannot be engaged. A single failed attempt is not conclusive.
- **Input System:** The game does not allow mixing directional (Up, Down, Left, Right) and action (A, B) buttons in a single turn's input array. This must be accounted for in battle menu navigation.