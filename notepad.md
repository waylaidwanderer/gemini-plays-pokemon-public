# Gem's Strategic Journal (v44 - Post-Critique Reboot)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information (reachable tiles, warps) is the source of truth. My own feeling of being "stuck" or a situation appearing to be a "dead end" is likely a hallucination if the data contradicts it. I must trust the data.
- **Agent Protocol:**
    - **Critical Navigation:** An agent that fails a critical navigation task (e.g., pathfinding through a maze) even once must be benched immediately for that specific task.
    - **Other Tasks:** For non-critical tasks, an agent that fails 2-3 times consecutively is unreliable and should be re-evaluated or benched.
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
- **Primary Goal:** Obtain the Silph Scope.
- **Secondary Goal:** Find the LIFT KEY.
- **Tertiary Goal:** Fully explore all floors of the Rocket Hideout.
### Current Plan
1.  Manually and cautiously explore the remaining unseen tiles on Rocket Hideout B3F.
2.  Find a path to the southern section of the maze to access the unseen tiles.
3.  Re-attempt to battle the Rocket Grunt at (21, 13) on B2F after exploring more, in case an event flag is required.
### Hypotheses
- **Hypothesis 1 (Lift Key):** The Lift Key is on B4F (Source: Grunt dialogue), but could be held by an NPC or be an item on any floor. Finding it is necessary to proceed.
- **Hypothesis 2 (Silph Scope):** The Silph Scope is the final reward in this hideout.
- **Hypothesis 3 (Saffron Access):** Giving a drink from the Celadon vending machines to a thirsty guard will grant access to Saffron City.

## V. Disproven Hypotheses & Failed Strategies
- **`spinner_maze_solver` Agent:** This agent is fundamentally incapable of solving the Rocket Hideout spinner mazes (B2F & B3F). It repeatedly generated invalid paths. The agent has been permanently deleted. Lesson: Recognize tool limitations faster and pivot to manual, systematic exploration for this type of puzzle.
- **Rocket Grunt Battle (21, 13 on B2F):** Repeatedly pressing 'A' does not initiate the battle. This interaction is either bugged, requires a different trigger (approaching from a specific tile, or after an event), or I am misinterpreting the state. I will not attempt this again until other avenues are exhausted.