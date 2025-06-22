# Gem's Strategic Journal (v41.0 - Post-Spinner-Maze Reflection)

## I. Core Principles & Lessons Learned
- **Agent Trust Protocol:** Trust agent output, but verify. A 'path not found' result likely means my premise is wrong. However, persistently failing agents (like `route_navigator_agent` in spinner mazes) should be benched in favor of manual navigation.
- **Agent-First Workflow:** Prioritize agents for complex tasks, but recognize their limitations.
- **WKG Protocol:** After adding a transition's nodes, my immediate next action is to add the connecting edge.
- **Dead End Definition:** An area is NOT a dead end if `Reachable Unseen Tiles` exist. A dead end is confirmed only when all paths, warps, and unseen tiles have been exhausted.
- **Proactive NPC Management:** Use `stun_npc` on moving NPCs to prevent them from blocking paths.
- **Interaction Protocol:** Attempt interaction from all adjacent, walkable tiles before assuming an NPC is unreachable. Face the target. Read the screen carefully!
- **Exploration Protocol:** Systematically clear sections of a map. The `Reachable Unseen Tiles` count must be zero before a map is considered fully explored.

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
- **`route_navigator_agent`:** (BENCHED for spinner mazes). The agent has repeatedly failed to navigate complex spinner puzzles. Manual navigation is required for these areas.
- **`battle_menu_navigator`:** (REFINED) Prompt updated. Requires testing.
- **Idea for Future Agent:** `spinner_maze_solver`. A highly specialized agent just for these types of puzzles.

## V. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Obtain the Silph Scope.
- **Secondary Goal:** Find the LIFT KEY.
- **Tertiary Goal:** Fully explore all floors of the Rocket Hideout.
### Current Plan
1.  Defeat the Rocket Grunt at (21, 13) on B2F.
2.  Investigate the item ball at (17, 9) on B2F.
3.  Explore the remaining 6 unseen tiles on B2F.
### Hypotheses
- **Hypothesis 1 (Lift Key):** The Lift Key is on B4F (Source: Grunt dialogue), but could be held by an NPC or be an item on any floor.
- **Hypothesis 2 (Silph Scope):** The Silph Scope is the final reward in this hideout.
- **Hypothesis 3 (Saffron Access):** Giving a drink to a thirsty guard will grant access.

## VI. Disproven Hypotheses & Failed Strategies
- **`route_navigator_agent` on Spinners:** The agent is unreliable for navigating spinner mazes. (Failed Turns ~19971-20003). **Lesson:** Recognize agent limitations faster and switch to manual navigation when necessary.
- **Manual Pathing Errors:** Several manual pathing attempts have failed due to misjudging spinner paths or obstacles. **Lesson:** Be more methodical and double-check paths before committing.