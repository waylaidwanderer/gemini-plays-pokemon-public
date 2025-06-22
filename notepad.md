# Gem's Strategic Journal (v38.0 - Post-Critique Refactor)

## I. Core Principles & Lessons Learned
- **Post-Transition Protocol (MANDATORY):** After ANY map change, my IMMEDIATE FIRST ACTION is to check the Game State Information for my new `map_id` and coordinates. I MUST do this BEFORE taking any other action (moving, interacting, WKG logging). This is non-negotiable.
- **Agent Trust Protocol:** Trust agent output, especially negative results. A 'path not found' result likely means my premise is wrong, not the agent. Re-evaluate my assumptions first. However, sanity-check absurdly long paths for simple tasks.
- **Risk Management:** Perform major maintenance (agent refinement, etc.) in safe zones like Pokémon Centers.
- **WKG Protocol:** After adding a transition's nodes, my immediate next action is to add the connecting edge.
- **Dead End Definition:** An area is NOT a dead end if `Reachable Unseen Tiles` exist or there are multiple reachable exits. A dead end is only confirmed when all paths, warps, and unseen tiles have been exhausted.
- **Proactive NPC Management:** Use `stun_npc` on moving NPCs to prevent them from blocking paths.
- **Interaction Protocol:** Attempt interaction from all adjacent, walkable tiles before assuming an NPC is unreachable. Face the target. Read the screen carefully!
- **Exploration Protocol:** Systematically clear sections of a map. The `Reachable Unseen Tiles` count must be zero before a map is considered fully explored. Avoid chaotic, cross-map pathing to individual tiles.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Usage:** A fainted POKéMON can use field moves like CUT.
- **EXP. All:** Distributes EXP to all non-fainted party members.
- **HYPER BEAM:** Huge damage, but requires a recharge turn unless the opponent faints. The recharge happens during the opponent's switch-in.

## III. World Intel & Navigation
### Celadon City
- A POKé FLUTE awakens sleeping POKéMON.
- **Celadon Dept. Store:** Sells TMs, items, and rooftop drinks. A boy on 3F mentioned a Kangaskhan for Graveler trade. A Super Nerd on 4F is buying a POKé DOLL for COPYCAT.
- **Celadon Chief House:** A Rocket grunt mentioned shipping 2000 POKéMON as slot prizes to the 'CHIEF'.
- **Celadon Game Corner:** Suspected Team Rocket front. Entrance at (34, 20).
- **Saffron City Access:** Guards at gatehouses on Route 5, 6, 7, and 8 are thirsty and blocking access.
### Other Locations
- **Lavender Town:** Team Rocket killed a Cubone's mother. Mr. Fuji is missing. Pokémon Tower is impassable without the Silph Scope.
- **Route 2:** Diglett's Cave exit leads to an isolated northern section.
- **Route 10:** Path to Lavender Town is south, past the Pokémon Center and Rock Tunnel.

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Obtain the Silph Scope.
- **Secondary Goal:** Find the LIFT KEY.
- **Tertiary Goal:** Gain access to Saffron City.

### Hypotheses
- **Hypothesis 1 (Silph Scope):** The Silph Scope is in a Team Rocket-controlled area, accessed via the Celadon Game Corner. **Plan:** Investigate the Game Corner. Look for secret switches or posters that might reveal a hideout.
- **Hypothesis 2 (Saffron Access):** Giving a drink to a thirsty guard will grant access. **Plan:** Test Fresh Water on a guard at the next opportunity.

## V. Technical Debt & Cleanup Plan
- Test the new `progression_advisor_agent` at the next opportunity to validate its effectiveness.

## VI. Disproven Hypotheses & Failed Strategies
- **Celadon 4F POKé DOLL Clerk:** The clerk at (6, 8) is inaccessible from the main floor. The area behind the counter is a separate, unreachable section. (Failed Turns 19183-19191).
- **Celadon Elevator to 4F Secret Area:** The elevator does not provide access to the inaccessible area behind the 4F counter. (Failed Turns 19200-19205).
- **Celadon Mansion Side Area Loop:** The western side of the mansion contains a warp loop between floors 1F, 2F, and 3F. The actual exit is a separate warp on 1F at (5, 1) leading back to Celadon City at (26, 4). (Failed Turns 19448-19452).
- **PC Menu Fumbling:** Incorrectly assumed 'Gem's PC' was for Pokémon storage instead of 'BILL's PC', leading to a ~40 turn loop. (Failed Turns 19506-19550). **Lesson:** READ THE SCREEN.
- **Celadon Game Corner Gym Guide:** The Gym Guide at (9, 15) is not a secret switch. He only provides info about the Celadon Gym Leader, Erika. (Failed Turn 19595)
- **Celadon Game Corner Suspicious NPCs:** Both the Gym Guide at (9, 15) and the Middle-Aged Woman at (9, 12) were flagged by my `hideout_scanner_agent` for facing walls but were red herrings. This NPC-based logic is unreliable here. (Failed Turns 19595-19602)

## VII. Team Improvements & Battle Strategy Lessons
- **Lesson: Moveset Verification (CRITICAL):** Do not assume a Pokémon has a type advantage without a corresponding STAB move. I switched in SUBTERRA (Ground-type) against Arbok (Poison-type) without confirming it knew any Ground moves, turning an easy win into a near-disaster. **Action:** Review all party Pokémon movesets at the next opportunity. Find the TM for Dig for SUBTERRA.
- **Lesson: Battle Menu Efficiency:** My one-button-per-turn menu navigation is extremely inefficient and wastes turns. **Action:** Refine the `battle_menu_navigator` agent to output a complete button sequence array and use it in a single turn. Stop manual, multi-turn menu navigation.