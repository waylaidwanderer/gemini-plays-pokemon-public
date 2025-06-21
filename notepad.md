# Gem's Strategic Journal (v10.0)

## I. Core Principles & Lessons Learned
- **Progression Over Perfection:** The critical path is key. Do not get bogged down in tool refinement if it halts game progress. A working-but-imperfect tool is better than no progress.
- **Hypothesize, Test, Pivot:** When stuck, form a hypothesis, test it, and if it fails, immediately pivot. Do not repeat failed actions.
- **Trust but Verify:** Trust agent outputs, but verify their performance with simple, non-critical tests before relying on them for major tasks.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Usage:** A fainted POKéMON can still use field moves like CUT.
- **Type Matchups (Verified):** Flying is 2x vs. Ground.
- **Move Compatibility (CRITICAL DISCOVERY):** SUBTERRA (Diglett) cannot learn HM05 Flash. PULSAR (Magnemite) can. Trust in-game 'ABLE'/'NOT ABLE' feedback.
- **Pokémon Evolutions:** ECHO (Zubat) -> Golbat at Lv. 22.
- **New Moves Learned:** ECHO (Golbat) learned Wing Attack, PULSAR (Magnemite) learned Flash, NIGHTSHADE (Gloom) learned Mega Drain.
- **EXP. All Mechanics (Verified):** EXP is distributed to all non-fainted party Pokémon.

## III. World Intel & Navigation
- **CRITICAL NAVIGATION LESSON:** Route 2 is segmented. The Diglett's Cave exit at (13, 11) leads to a small, isolated northern section.
- **Lt. Surge's Raichu (Lv. 29):** Knows Body Slam and Surf.
- **Recurring Obstacles:** Trees in Vermilion City (16,19) and Route 2 (16,23) respawn.
- **Route 11 Gatehouse Split:** West entrance leads to a small room with no access to the eastern section.
- **Item Discovery:** MOON STONE on Route 2 (south section).

## IV. Agent & Tool Strategy
- **Proactive Testing Mandate:** After defining or significantly refining an agent, I MUST devise a simple, non-critical test case to validate its functionality.
- **`battle_move_advisor_agent`:** Fixed to handle 4x weakness.
- **`trainer_hunter_agent`:** Rebuilt and tested successfully.
- **`pokemon_evolution_advisor`:** Tested successfully.
- **`tm_usage_advisor_agent`:** On hold, requires stat data.

## V. Agent Debugging Log
- **`route_navigator_agent` (Rock Tunnel 1F):** Agent repeatedly failed to find paths to reachable targets (ladder at 16,4 and unseen areas), despite system validation confirming paths exist. Hypothesized issue with XML parsing or obstacle handling in the agent's generated Python code. Refining prompt to be more explicit about map parsing and path validation.

## VI. Agent Ideas
- **Catch Advisor Agent:** Given current Pokédex and wild encounters on a map, suggest which Pokémon are new and provide a strategy for catching them.