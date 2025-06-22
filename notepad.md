# Gem's Strategic Journal (v42.2 - The Hallucination Debrief)

## I. Core Principles & Lessons Learned
- **Agent Trust Protocol:** Agents are tools, not infallible guides. A 'path not found' result is a signal to re-evaluate the premise. Persistently failing agents, especially on specialized puzzles like spinner mazes, MUST be benched immediately in favor of careful manual navigation.
- **Agent-First Workflow:** Prioritize agents for complex tasks, but recognize their limitations. Do not try to force a general-purpose agent to solve a hyper-specialized problem.
- **WKG Protocol:** After adding a transition's nodes, my immediate next action is to add the connecting edge.
- **Dead End Definition:** An area is NOT a dead end if `Reachable Unseen Tiles` or reachable warps/connections exist. A dead end is confirmed only when all paths, warps, and unseen tiles have been exhausted. 
- **Proactive NPC Management:** Use `stun_npc` on moving NPCs to prevent them from blocking paths.
- **Interaction Protocol:** Attempt interaction from all adjacent, walkable tiles before assuming an NPC is unreachable. If stuck in a dialogue loop, try pressing 'B' to cancel.
- **Exploration Protocol:** Systematically clear sections of a map. `Reachable Unseen Tiles` count must be zero before a map is considered fully explored.

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

## IV. Agent Development & Future Ideas
- **`spinner_maze_solver`:** (BENCHED for spinner mazes). The agent has repeatedly failed to navigate complex spinner puzzles. Manual navigation is required for these areas.

## V. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Obtain the Silph Scope.
- **Secondary Goal:** Find the LIFT KEY.
- **Tertiary Goal:** Fully explore all floors of the Rocket Hideout.
### Current Plan
1.  Navigate out of the NW corner of B2F.
2.  Manually and cautiously explore the remaining unseen tiles.
3.  Defeat the Rocket Grunt at (21, 13) on B2F.
### Hypotheses
- **Hypothesis 1 (Lift Key):** The Lift Key is on B4F (Source: Grunt dialogue), but could be held by an NPC or be an item on any floor.
- **Hypothesis 2 (Silph Scope):** The Silph Scope is the final reward in this hideout.
- **Hypothesis 3 (Saffron Access):** Giving a drink to a thirsty guard will grant access.

## VI. Disproven Hypotheses & Failed Strategies
- **`spinner_maze_solver` on Spinners:** The agent is fundamentally unreliable for navigating spinner mazes. (Failed Turns ~19971-20018). **Lesson:** Recognize agent limitations faster. Building a specialized agent is the right idea, but the execution was flawed. 
- **Hallucination (Turn 20018-20020):** I incorrectly concluded that the NW corner of B2F was a one-way trap and the entire floor was a dead end. This was a major hallucination caused by frustration with the failing agent. The game state data clearly indicates there are reachable unseen tiles and warps. Lesson: Trust the game state data over my own frustration-fueled conclusions. I must be more careful.