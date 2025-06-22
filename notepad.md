# Gem's Strategic Journal (v43 - Post-Critique Reboot)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information (reachable tiles, warps) is the source of truth. My own feeling of being "stuck" or a situation appearing to be a "dead end" is likely a hallucination if the data contradicts it. I must trust the data.
- **Agent Protocol:** An agent that fails the same specific task 2-3 times consecutively is unreliable for that task. It must be benched immediately in favor of a different strategy, usually careful manual execution. Do not fall into a sunk-cost fallacy of endlessly refining a broken tool.
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
1.  Manually and cautiously explore the remaining unseen tiles on Rocket Hideout B2F.
2.  Find a path to the southern section of the maze to access the unseen tiles.
3.  Re-attempt to battle the Rocket Grunt at (21, 13) after exploring more, in case an event flag is required.
### Hypotheses
- **Hypothesis 1 (Lift Key):** The Lift Key is on B4F (Source: Grunt dialogue), but could be held by an NPC or be an item on any floor. Finding it is necessary to proceed.
- **Hypothesis 2 (Silph Scope):** The Silph Scope is the final reward in this hideout.
- **Hypothesis 3 (Saffron Access):** Giving a drink from the Celadon vending machines to a thirsty guard will grant access to Saffron City.

## V. Disproven Hypotheses & Failed Strategies
- **`spinner_maze_solver` Agent:** This agent is fundamentally incapable of solving the Rocket Hideout B2F spinner maze. It repeatedly generated invalid, non-continuous, or impossible paths, leading to dozens of wasted turns. It has been permanently benched for this type of puzzle. Lesson: Recognize tool limitations faster and pivot to manual strategies.
- **Hallucination (Turn ~20018):** I incorrectly concluded that the NW corner of B2F was a one-way trap and the entire floor was a dead end. This was a major hallucination caused by frustration with the failing agent. The game state data clearly indicated there were reachable unseen tiles and warps. Lesson: I must trust the game state data over my own frustration-fueled conclusions.
- **Rocket Grunt Battle (21, 13):** Repeatedly pressing 'A' does not initiate the battle. This interaction is either bugged, requires a different trigger (approaching from a specific tile, or after an event), or I am misinterpreting the state. I will not attempt this again until other avenues are exhausted.

## VI. Future Agent Ideas
- **Item Usage Advisor:** An agent that takes my inventory and Pokémon stats to recommend the optimal use of stat-boosting items like HP UP for long-term benefit.