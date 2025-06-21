# Gem's Strategic Journal (v20.0 - Post-Critique)

## I. CRITICAL LESSONS & CORRECTIONS
- **The Pokémon Tower Entrance:** The warp at (8, 10) in Lavender Town is NOT the Pokémon Tower entrance; it leads to the dead-end Mr. Fuji's House. I MUST find the real entrance.
- **Verify, Don't Assume:** My locational hallucinations were a critical failure. I MUST verify my `map_id` and coordinates from the Game State before every action. Trusting memory is unreliable.
- **Dead End Definition:** An area is NOT a dead end if there are `Reachable Unseen Tiles`. I must clear them before moving on.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Usage:** A fainted POKéMON can still use field moves like CUT.
- **Type Matchups (Verified):** Flying is 2x vs. Ground. Flying vs. Grass/Poison is a neutral 1x multiplier. Ground-type moves ARE super-effective (2x) against Rock/Ground dual-types like Geodude.
- **Move Compatibility:** SUBTERRA (Diglett) cannot learn HM05 Flash. PULSAR (Magnemite) can.
- **Pokémon Evolutions:** ECHO (Zubat) -> Golbat at Lv. 22.
- **EXP. All Mechanics:** EXP is distributed to all non-fainted party Pokémon.

## III. World Intel & Navigation
- **Route 10 Path:** The correct path to Lavender Town is south on Route 10, past the Pokémon Center and cuttable trees.
- **Route 2 Segmentation:** Diglett's Cave exit at (13, 11) leads to a small, isolated northern section.
- **Lt. Surge's Raichu (Lv. 29):** Knows Body Slam and Surf.
- **Lavender Town Intel:** A girl in the Pokémon Center saw Team Rocket kill a Cubone's mother.
- **CRITICAL WARP MECHANIC:** The warp from Mr. Fuji's House is ONE-WAY. It exits to (8, 11) in Lavender Town, not back to the entrance at (4, 14).

## IV. Agent & Tool Strategy
### Agent Refinement Protocol (MANDATORY - v2)
1.  **Hypothesize & Isolate:** Form a specific, small hypothesis for what is failing. Test in a controlled, simple scenario.
2.  **Iterate Small:** Make small, incremental changes to the prompt. Avoid large rewrites.
3.  **Manual Unstick:** If an agent is stuck, take 1-2 manual steps to change the game state. Progress over perfection.
4.  **Validate, then Deploy:** Only use the refined agent for critical tasks after it passes a simple validation test.

### Agent Status & Refinement Plan
- **`route_navigator_agent`:** Agent is reliable. My understanding was flawed. I must trust its 'path not found' errors and re-evaluate my target coordinates.
- **`battle_move_advisor_agent`:** Reliable.
- **`battle_menu_navigator`:** Reliable.
- **`trainer_hunter_agent`:** Tested successfully.
- **`tm_hm_compatibility_agent`:** Tested successfully.
- **UNUSED AGENTS:** `pokemon_evolution_advisor` and `pp_management_advisor_agent` are untested. I need to test them or delete them to free up agent slots.

## V. Core Gameplay Knowledge & Corrections
- **NPC Interaction Protocol:** If an NPC seems unreachable, I must attempt to interact from all adjacent, walkable tiles before assuming they cannot be engaged.
- **Input System:** The game does not allow mixing directional and action buttons in a single turn's input array.