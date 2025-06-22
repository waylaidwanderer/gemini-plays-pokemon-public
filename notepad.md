# Gem's Strategic Journal (v26.0 - Post-Critique)

## I. CRITICAL LESSONS & CORRECTIONS
- **WKG Protocol:** After adding nodes for a new transition, my VERY NEXT action MUST be to add the connecting edge.
- **Verify, Don't Assume:** I must verify my `map_id` and coordinates from the Game State before every action.
- **Dead End Definition:** An area is NOT a dead end if there are `Reachable Unseen Tiles`. I must clear them before moving on.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Usage:** A fainted POKéMON can still use field moves like CUT.
- **EXP. All Mechanics:** EXP is distributed to all non-fainted party Pokémon.
- **Battle Menu Navigation:** The move selection menu *wraps around*, but the party selection menu *does not*.

## III. World Intel & Navigation
- **Route 10 Path:** The correct path to Lavender Town is south on Route 10, past the Pokémon Center and cuttable trees.
- **Route 2 Segmentation:** Diglett's Cave exit at (13, 11) leads to a small, isolated northern section.
- **Lt. Surge's Raichu (Lv. 29):** Knows Body Slam and Surf.
- **Lavender Town Intel:** A girl in the Pokémon Center saw Team Rocket kill a Cubone's mother.
- **CRITICAL WARP MECHANIC:** The warp from Mr. Fuji's House is ONE-WAY. It exits to (8, 11) in Lavender Town, not back to the entrance at (4, 14).

## IV. Agent & Tool Strategy
### Agent Refinement Protocol (MANDATORY)
1.  **Hypothesize & Isolate:** Form a specific, small hypothesis for what is failing. Test in a controlled, simple scenario.
2.  **Iterate Small:** Make small, incremental changes to the prompt. Avoid large rewrites.
3.  **Manual Unstick:** If an agent is stuck, take 1-2 manual steps to change the game state. Progress over perfection.
4.  **Validate, then Deploy:** Only use the refined agent for critical tasks after it passes a simple validation test.

### Agent Status & Refinement Plan
- **`route_navigator_agent`:** Reliable.
- **`battle_move_advisor_agent`:** Reliable.
- **`trainer_hunter_agent`:** Reliable.
- **`tm_hm_compatibility_agent`:** Reliable.
- **`switch_advisor_agent`:** Reliable.
- **`battle_menu_navigator`:** FLAWED. **PRIORITY FIX:** Refine this agent's prompt to accurately reflect that the party list does NOT wrap around, while the move list DOES.
- **Agent Idea:** A `pc_organizer_agent` could be useful. Implement or discard this idea soon.

## V. Core Gameplay Knowledge & Corrections
- **NPC Interaction Protocol:** If an NPC seems unreachable, I must attempt to interact from all adjacent, walkable tiles before assuming they cannot be engaged.
- **Input System:** The game does not allow mixing directional and action buttons in a single turn's input array.

## VI. Gameplay Protocols (MANDATORY)
- **Post-Transition Verification Protocol:** Every single time the `map_id` changes, I MUST pause and confirm my new map and coordinates from the Game State Information before taking any other action.

## VII. Current Action Plans & Hypotheses
- **IMMEDIATE GOALS (Post-Battle):**
    1. Heal the entire party at the nearest Pokémon Center.
    2. Systematically explore the 39 reachable unseen tiles on Route 8.
    3. Refine the `battle_menu_navigator` agent prompt.
- **Hypothesis:** The guard in the Route 8 Gatehouse is blocking the way to Saffron City. I may need an item to pass.

## VIII. Post-Critique Reflections
- **Risk Assessment Lesson (T18654):** The failed SUBTERRA switch against Voltorb highlighted a critical lesson. While an agent might identify a high-reward play (Ground immunity), I must weigh that against the risk (low HP, potential non-STAB coverage moves). I am the final judge of risk vs. reward.
- **Correction (T18660+):** I repeatedly hallucinated that Route 8 was fully explored and miscounted my turns. The system reported 39 reachable unseen tiles. This reveals a procedural flaw in my attention to detail. I MUST re-explore this route thoroughly after healing.