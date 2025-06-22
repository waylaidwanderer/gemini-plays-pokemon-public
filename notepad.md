# Gem's Strategic Journal (v34.0 - Post-Critique)

## I. Core Principles & Lessons Learned
- **Post-Transition Protocol (MANDATORY):** After ANY map change, my IMMEDIATE FIRST ACTION is to check the Game State Information for my new `map_id` and coordinates. I MUST do this BEFORE taking any other action (moving, interacting, WKG logging). This is non-negotiable.
- **Agent Trust Protocol:** Trust agent output, especially negative results. A 'path not found' result likely means my premise is wrong, not the agent. Re-evaluate my assumptions first.
- **Risk Management:** Perform major maintenance (agent refinement, etc.) in safe zones like Pokémon Centers.
- **WKG Protocol:** After adding a transition's nodes, my immediate next action is to add the connecting edge.
- **Dead End Definition:** An area is NOT a dead end if `Reachable Unseen Tiles` exist or there are multiple reachable exits. The elevator map is a confirmed dead end (1 exit).
- **Proactive NPC Management:** Use `stun_npc` on moving NPCs to prevent them from blocking paths. It may not be permanent.
- **Interaction Protocol:** Attempt interaction from all adjacent, walkable tiles before assuming an NPC is unreachable. Face the target.
- **Exploration Protocol:** The `Reachable Unseen Tiles` count is the source of truth. The count must be zero before proceeding to a new major objective on a map.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Usage:** A fainted POKéMON can use field moves like CUT.
- **EXP. All:** Distributes EXP to all non-fainted party members.

## III. World Intel & Navigation
### Celadon City
- A POKé FLUTE awakens sleeping POKéMON.
- **Celadon Dept. Store:**
    - 2F: Sells TMs and general items (Potions, Repels). No drinks.
    - 3F: A boy mentions a Kangaskhan for Graveler trade hint.
    - 4F: A Super Nerd is buying a POKé DOLL for COPYCAT in Cerulean City.
    - Roof: Vending Machines sell Fresh Water, Soda Pop, and Lemonade.
- **Celadon Chief House:** A Rocket grunt mentions shipping 2000 POKéMON as slot prizes to the 'CHIEF'.
- **Celadon Game Corner:** Suspected Team Rocket front.

### Other Locations
- **Lavender Town:** Team Rocket killed a Cubone's mother. Mr. Fuji's House warp is a one-way exit.
- **Route 2:** Diglett's Cave exit leads to an isolated northern section.
- **Route 10:** Path to Lavender Town is south, past the Pokémon Center and cuttable trees.

## IV. Action Plans & Hypotheses
- **Primary Goal:** Obtain the Silph Scope.
- **Secondary Goal:** Fully explore Celadon City.
- **Tertiary Goal:** Gain access to Saffron City.

- **Hypothesis 1 (Silph Scope):** The Silph Scope is in a Team Rocket-controlled area, likely accessed via the Celadon Game Corner.
- **Hypothesis 2 (Saffron Access):** Giving a drink to a thirsty guard will grant access. Will test Fresh Water first.

## V. Disproven Hypotheses & Failed Strategies
- **Celadon 4F POKé DOLL Clerk:** The clerk at (6, 8) is inaccessible from the main floor. The area behind the counter is a separate, unreachable section. (Failed Turns 19183-19191).
- **Celadon Elevator to 4F Secret Area:** The elevator does not provide access to the inaccessible area behind the 4F counter. It leads to the standard elevator arrival point. (Failed Turns 19200-19205).

## VI. Technical Debt & Cleanup
- **WKG - Celadon Dept. Store Escalators:** The nodes and edges for the escalators are incorrect or incomplete. Need to revisit, delete the bad entries, and re-add them systematically.
- **`route_navigator_agent` (CRITICAL):** Fundamentally flawed. Fails in complex indoor areas and gives bizarre paths. Requires a complete logic overhaul.
- **`exploration_agent` (Suboptimal):** Fails to find paths to all reachable unseen tiles in a single run, requiring multiple calls. Needs to be refined for comprehensive, one-shot pathing.

## VII. Agent Ideas
- **Progression Advisor Agent:** To analyze badges, level cap, party, and known locations to suggest the next logical major objective (e.g., next gym). This would help with long-term strategic planning.