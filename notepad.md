# Gem's Strategic Journal (v31.0 - Post-Reflection)

## I. Core Principles & Lessons Learned
- **Agent Trust Protocol:** Trust agent output, especially negative results. A 'path not found' result likely means my premise is wrong, not the agent. Re-evaluate my assumptions first.
- **Risk Management:** Perform major maintenance (agent refinement, etc.) in safe zones like Pokémon Centers.
- **WKG Protocol:** After adding a transition's nodes, my immediate next action is to add the connecting edge.
- **Dead End Definition:** An area is NOT a dead end if `Reachable Unseen Tiles` exist. Explore them before concluding a path is blocked. The elevator map is a confirmed dead end (1 exit).
- **Proactive NPC Management:** Use `stun_npc` on moving NPCs to prevent them from blocking paths.
- **Interaction Protocol:** Attempt interaction from all adjacent, walkable tiles before assuming an NPC is unreachable. Face the target.
- **Post-Transition Verification:** After every map change, I MUST pause and confirm my new location from Game State Information before acting.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Usage:** A fainted POKéMON can use field moves like CUT.
- **EXP. All:** Distributes EXP to all non-fainted party members.

## III. World Intel & Navigation
- **Route 2:** Diglett's Cave exit leads to an isolated northern section.
- **Route 10:** Path to Lavender Town is south, past the Pokémon Center and cuttable trees.
- **Mr. Fuji's House Warp:** This is a ONE-WAY exit to Lavender Town at (8, 11).
- **Celadon Dept. Store:** Vending machines on the roof sell Fresh Water, Soda Pop, and Lemonade.
- **Celadon Mart 3F:** A boy will trade a Kangaskhan for a Graveler. This is a hint for trade evolutions.
- **Lavender Town:** Team Rocket killed a Cubone's mother.
- **Celadon City:** A POKé FLUTE awakens sleeping POKéMON.

## IV. Agent & Tool Strategy
### Agent Refinement Protocol
1.  **Hypothesize & Isolate:** Form a small, testable hypothesis for the failure.
2.  **Iterate Small:** Make small, incremental changes to the prompt.
3.  **Manual Unstick:** Take 1-2 manual steps to change the game state if an agent is stuck.
4.  **Validate, then Deploy:** Test refined agents in simple scenarios before critical use.

### Agent Status & Plans
- **`route_navigator_agent` (REFINED):** Now more robust at finding paths around obstacles.
- **`battle_menu_navigator` (OK):** Working well.
- **`inventory_manager_agent` (MONITOR):** Gave one faulty tip. Will monitor its performance.
- **`exploration_agent` (REFINED):** Correctly paths to tiles *adjacent* to unseen areas. My primary exploration tool.

### New Agent Ideas
- **`trade_tracker_agent`:** To log trade opportunities (NPC, location, Pokémon wanted/offered).
- **`hm_advisor_agent`:** To check which of my Pokémon can learn a given HM.

## V. Current Action Plans & Hypotheses
- **Primary Goal:** Obtain the Silph Scope.
- **Secondary Goal:** Gain access to Saffron City.
- **Tertiary Goal:** Explore the Celadon Department Store.

- **Hypothesis 1 (Celadon/Silph Scope):** The Silph Scope is likely in a Team Rocket-controlled area within Celadon City, possibly the Game Corner.
- **Hypothesis 2 (Saffron Access):** Giving a drink (Fresh Water, Soda Pop, or Lemonade) to a thirsty guard will grant access. I will test Fresh Water first.