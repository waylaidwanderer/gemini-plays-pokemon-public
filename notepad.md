# Gem's Strategic Journal (v46 - Post-Critique Refinement)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information (reachable tiles, warps) is the source of truth. My own feeling of being "stuck" or a situation appearing to be a "dead end" is likely a hallucination if the data contradicts it. I must trust the data.
- **Agent Protocol:**
    - **Pathfinding Agent Unreliability:** All pathfinding agents (`maze_navigator_agent`, `spinner_maze_navigator_agent`) are fundamentally unreliable for the Rocket Hideout's spinner mazes (B2F, B3F, etc.). They consistently fail to account for spinner mechanics. Manual, systematic exploration is required for these specific puzzles.
    - **`battle_menu_navigator` Flaw (Corrected):** This agent previously assumed the move menu was a 2x2 grid. This has been corrected to reflect the actual vertical list layout. It also incorrectly assumes the party menu cursor starts on the first Pokémon; it actually starts on the active Pokémon. Manual navigation of the party menu is still required.
- **Interaction Protocol:** If an interaction (battle, dialogue) doesn't trigger as expected, do not repeat the same input. Immediately try a different input (e.g., 'B' to cancel) or a different approach (e.g., interacting from an adjacent tile).
- **WKG Protocol:** After adding a transition's nodes, my immediate next action is to add the connecting edge.
- **Proactive NPC Management:** Use `stun_npc` on moving NPCs to prevent them from blocking paths.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Usage:** A fainted POKéMON can use field moves like CUT.
- **EXP. All:** Distributes EXP to all non-fainted party members.
- **HYPER BEAM:** Huge damage, but requires a recharge turn unless the opponent faints.

## III. World Intel & Navigation
### Celadon City
- A POKé FLUTE awakens sleeping POKéMON.
- **Celadon Dept. Store:** Rooftop vending machines sell drinks.
- **Celadon Game Corner:** Team Rocket front. Entrance at (34, 20). Secret hideout entrance behind a poster at (18, 5).
- **Saffron City Access:** Guards at all gatehouses are thirsty and blocking access.

### Other Locations
- **Lavender Town:** Pokémon Tower is impassable without the Silph Scope.
- **Route 10:** Path to Lavender Town is south, past the Pokémon Center and Rock Tunnel.

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Defeat the boss of the Rocket Hideout.
- **Secondary Goal:** Find the hideout's boss.
- **Tertiary Goal:** Acquire the Silph Scope.
### Current Plan
1. Defeat the Rocket Grunt on B1F.
2. Fully explore the southwestern area of Rocket Hideout B1F.
3. The boss is likely on B4F, so I need to find a way to get there.
### Hypotheses
- **Hypothesis 1 (Silph Scope):** The Silph Scope is the final reward in this hideout, likely held by the boss.
- **Hypothesis 2 (Saffron Access):** Giving a drink from the Celadon vending machines to a thirsty guard will grant access to Saffron City.

## V. Disproven Hypotheses & Failed Strategies
- **Rocket Grunt Battle (21, 13 on B2F):** Repeatedly trying to initiate this battle has failed. This interaction is either bugged or requires a specific trigger I have not yet found. I will not attempt this again until other avenues are exhausted.