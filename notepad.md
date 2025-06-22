# Gem's Strategic Journal (v29.0 - Post-Critique)

## I. CRITICAL LESSONS & CORRECTIONS
- **Agent Trust Protocol:** I MUST treat agent output, especially negative results like 'path not found', as valuable data that may invalidate my own assumptions. An agent reporting no path doesn't mean it's broken; it means I might be wrong about the destination or route. I will re-evaluate my premise first.
- **Risk Management Protocol:** Major strategic maintenance (agent refinement, notepad overhauls) MUST be performed in safe locations like Pokémon Centers, NOT in hostile territory with a weakened party. Safety first!
- **WKG Protocol:** After adding nodes for a new transition, my VERY NEXT action MUST be to add the connecting edge.
- **Dead End Definition:** An area is NOT a dead end if there are `Reachable Unseen Tiles`. I must clear them before moving on.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Usage:** A fainted POKéMON can still use field moves like CUT.
- **EXP. All Mechanics:** EXP is distributed to all non-fainted party Pokémon.

## III. World Intel & Navigation
- **Route 10 Path:** The correct path to Lavender Town is south on Route 10, past the Pokémon Center and cuttable trees.
- **Route 2 Segmentation:** Diglett's Cave exit at (13, 11) leads to a small, isolated northern section.
- **Lt. Surge's Raichu (Lv. 29):** Knows Body Slam and Surf.
- **Lavender Town Intel:** A girl in the Pokémon Center saw Team Rocket kill a Cubone's mother.
- **Celadon City Intel:** A Gentleman in the Pokémon Center mentioned that a POKé FLUTE can awaken sleeping POKéMON.
- **CRITICAL WARP MECHANIC:** The warp from Mr. Fuji's House is ONE-WAY. It exits to (8, 11) in Lavender Town, not back to the entrance at (4, 14).

## IV. Agent & Tool Strategy
### Agent Refinement Protocol (MANDATORY)
1.  **Hypothesize & Isolate:** Form a specific, small hypothesis for what is failing. Test in a controlled, simple scenario.
2.  **Iterate Small:** Make small, incremental changes to the prompt. Avoid large rewrites.
3.  **Manual Unstick:** If an agent is stuck, take 1-2 manual steps to change the game state. Progress over perfection.
4.  **Validate, then Deploy:** Only use the refined agent for critical tasks after it passes a simple validation test.

### Agent Status & Refinement Plan
- **`route_navigator_agent`:** REFINED (T18811). Added reinforced ledge traversal logic to prompt. Will monitor.
- **`battle_menu_navigator`:** REFINED (T18811). Corrected prompt to specify party list does not wrap. Will test.
- **`pc_organizer_agent`:** Created. Will test at the next opportunity.
- **`inventory_manager_agent`:** Created (T18811). Will use to optimize inventory before major dungeons or city visits.
- **`pokedex_completionist_agent`:** Created (T18811). Will use to guide catching efforts in new areas to efficiently complete the Pokédex.

## V. Core Gameplay Knowledge & Corrections
- **NPC Interaction Protocol:** If an NPC seems unreachable, I must attempt to interact from all adjacent, walkable tiles before assuming they cannot be engaged.
- **Input System:** The game does not allow mixing directional and action buttons in a single turn's input array. I must execute agent-provided sequences fully.

## VI. Gameplay Protocols (MANDATORY)
- **Post-Transition Verification Protocol:** Every single time the `map_id` changes, I MUST pause and confirm my new map and coordinates from the Game State Information before taking any other action.

## VII. Current Action Plans & Hypotheses
- **IMMEDIATE GOALS:**
    1. Explore Celadon Mansion for clues or items.
    2. Find the Celadon Department Store.
    3. Find a drink for the thirsty guards.
- **Hypothesis:** The Department Store will sell a drink that can be given to the guards.