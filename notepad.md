# Gem's Strategic Journal (v47 - Post-Critique Refinement)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information (reachable tiles, warps) is the source of truth. My own feeling of being "stuck" or a situation appearing to be a "dead end" is likely a hallucination if the data contradicts it. I must trust the data.
- **Agent Protocol:**
    - **Pathfinding Agent Decommissioned:** All dedicated pathfinding agents for the Rocket Hideout spinner mazes proved unreliable and have been deleted. Manual, systematic exploration is the confirmed strategy for these specific puzzles.
    - **`battle_menu_navigator` Flaw (Corrected):** This agent previously assumed the move menu was a 2x2 grid and that the party menu cursor starts on the first Pokémon. It has been corrected to reflect the vertical move list and the fact that the cursor starts on the active Pokémon.
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
1. Heal my team at the Celadon Pokémon Center.
2. Systematically explore the Rocket Hideout to find the boss.
3. The boss is likely on B4F, so I need to find a way to get there using the Lift Key.
### Hypotheses
- **Hypothesis 1 (Silph Scope):** The Silph Scope is the final reward in this hideout, likely held by the boss.
- **Hypothesis 2 (Saffron Access):** Giving a drink from the Celadon vending machines to a thirsty guard will grant access to Saffron City.

## V. Disproven Hypotheses & Failed Strategies
- **Rocket Grunt Battle (21, 13 on B2F):** Repeatedly trying to initiate this battle has failed. This interaction is either bugged or requires a specific trigger I have not yet found. This hypothesis is currently on hold.