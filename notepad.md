# Gem's Strategic Journal (v40.0 - Post-Critique Refactor)

## I. Core Principles & Lessons Learned
- **Agent Trust Protocol:** Trust agent output, especially negative results. A 'path not found' result likely means my premise is wrong, not the agent. Re-evaluate my assumptions first. However, sanity-check absurdly long paths for simple tasks.
- **Agent-First Workflow:** Before any complex reasoning, calculation, or repetitive task, first consider if an agent can perform it. Prioritize creating agents to automate tasks.
- **WKG Protocol:** After adding a transition's nodes, my immediate next action is to add the connecting edge.
- **Dead End Definition:** An area is NOT a dead end if `Reachable Unseen Tiles` exist or there are multiple reachable exits. A dead end is only confirmed when all paths, warps, and unseen tiles have been exhausted.
- **Proactive NPC Management:** Use `stun_npc` on moving NPCs to prevent them from blocking paths.
- **Interaction Protocol:** Attempt interaction from all adjacent, walkable tiles before assuming an NPC is unreachable. Face the target. Read the screen carefully!
- **Exploration Protocol:** Systematically clear sections of a map. The `Reachable Unseen Tiles` count must be zero before a map is considered fully explored. Rely on `route_navigator_agent` for all pathing to avoid manual errors.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Usage:** A fainted POKéMON can use field moves like CUT.
- **EXP. All:** Distributes EXP to all non-fainted party members.
- **HYPER BEAM:** Huge damage, but requires a recharge turn unless the opponent faints. The recharge happens during the opponent's switch-in.
- **Unseen Tile Count:** Double-check this number from the game state before making exploration decisions. Miscounting is a critical error.

## III. World Intel & Navigation
### Celadon City
- A POKé FLUTE awakens sleeping POKéMON.
- **Celadon Dept. Store:** Sells TMs, items, and rooftop drinks. A boy on 3F mentioned a Kangaskhan for Graveler trade. A Super Nerd on 4F is buying a POKé DOLL for COPYCAT.
- **Celadon Chief House:** A Rocket grunt mentioned shipping 2000 POKéMON as slot prizes to the 'CHIEF'.
- **Celadon Game Corner:** Suspected Team Rocket front. Entrance at (34, 20). Secret hideout entrance behind a poster at (18, 5).
- **Saffron City Access:** Guards at gatehouses on Route 5, 6, 7, and 8 are thirsty and blocking access.
### Other Locations
- **Lavender Town:** Pokémon Tower is impassable without the Silph Scope.
- **Route 10:** Path to Lavender Town is south, past the Pokémon Center and Rock Tunnel.

## IV. Agent Development & Testing Pipeline
- **`battle_menu_navigator`:** (REFINED) Prompt updated to enforce a complete, single-turn button sequence. Must be tested in the next battle.
- **`progression_advisor_agent`:** (UNTESTED) Needs testing to determine value.
- **`battle_tactic_advisor_agent`:** (UNTESTED) Needs testing to determine value.
- **`trainer_hunter_agent`:** (NEW) Scans map for undefeated trainers. Needs to be defined and tested.

## V. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Obtain the Silph Scope.
- **Secondary Goal:** Find the LIFT KEY.
- **Tertiary Goal:** Fully explore all floors of the Rocket Hideout for items and trainers.
### Hypotheses
- **Hypothesis 1 (Lift Key):** The Lift Key is on B4F. (Source: Grunt dialogue). *Assumption:* The grunt was truthful and accurate. It could be on any floor.
- **Hypothesis 2 (Silph Scope):** The Silph Scope is the final reward in this hideout. *Assumption:* This follows standard game logic, but could be different in this ROM hack.
- **Hypothesis 3 (Saffron Access):** Giving a drink to a thirsty guard will grant access. *Plan:* Test Fresh Water on a guard at the next opportunity.

## VI. Disproven Hypotheses & Failed Strategies
- **Inefficient Battle Navigation:** Taking multiple turns to select a single move. (Failed Turns ~19875-19885). **Lesson:** The `battle_menu_navigator` must be used to generate a complete button sequence for a single turn. Manual, multi-turn navigation is a critical error.
- **Manual Pathing Errors:** Attempting to path directly to an item at (12, 15) failed due to an unseen obstacle. (Failed Turn 19890). **Lesson:** Use `route_navigator_agent` for all pathing, even for short distances, to avoid errors.
- **Celadon Mansion Side Area Loop:** The western side of the mansion contains a warp loop between floors 1F, 2F, and 3F. The actual exit is a separate warp on 1F at (5, 1) leading back to Celadon City at (26, 4). (Failed Turns 19448-19452).
- **PC Menu Fumbling:** Incorrectly assumed 'Gem's PC' was for Pokémon storage instead of 'BILL's PC', leading to a ~40 turn loop. (Failed Turns 19506-19550). **Lesson:** READ THE SCREEN.