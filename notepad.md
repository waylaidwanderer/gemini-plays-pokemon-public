# Gem's Strategic Journal (v33.0 - Post-Critique)

## I. Core Principles & Lessons Learned
- **Post-Transition Protocol:** After ANY map change, I MUST first confirm my new `map_id` and coordinates from Game State Information before taking any other action. This prevents WKG errors.
- **Agent Trust Protocol:** Trust agent output, especially negative results. A 'path not found' result likely means my premise is wrong, not the agent. Re-evaluate my assumptions first.
- **Risk Management:** Perform major maintenance (agent refinement, etc.) in safe zones like Pokémon Centers.
- **WKG Protocol:** After adding a transition's nodes, my immediate next action is to add the connecting edge.
- **Dead End Definition:** An area is NOT a dead end if `Reachable Unseen Tiles` exist or there are multiple reachable exits. The elevator map is a confirmed dead end (1 exit).
- **Proactive NPC Management:** Use `stun_npc` on moving NPCs to prevent them from blocking paths.
- **Interaction Protocol:** Attempt interaction from all adjacent, walkable tiles before assuming an NPC is unreachable. Face the target.
- **Elevator Mechanics:** Select floor with panel at (4,1), then step on warp pads at (2,4) or (3,4) to travel.

## II. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Usage:** A fainted POKéMON can use field moves like CUT.
- **EXP. All:** Distributes EXP to all non-fainted party members.

## III. World Intel & Navigation
### Celadon Dept. Store Notes
- **2F Clerks:** Sell TMs and general items (Potions, Repels). No drinks.
- **3F Game Corner Boys:** Mention a Kangaskhan for Graveler trade, a hint for trade evolutions.
- **Roof Vending Machines:** Sell Fresh Water, Soda Pop, and Lemonade.

### Other Locations
- **Route 2:** Diglett's Cave exit leads to an isolated northern section.
- **Route 10:** Path to Lavender Town is south, past the Pokémon Center and cuttable trees.
- **Mr. Fuji's House Warp:** This is a ONE-WAY exit to Lavender Town at (8, 11).
- **Lavender Town:** Team Rocket killed a Cubone's mother.
- **Celadon City:** A POKé FLUTE awakens sleeping POKéMON.

## IV. Agent & Tool Strategy
### Agent Refinement Protocol
1.  **Hypothesize & Isolate:** Form a small, testable hypothesis for the failure.
2.  **Iterate Small:** Make small, incremental changes to the prompt.
3.  **Manual Unstick:** Take 1-2 manual steps to change the game state if an agent is stuck.
4.  **Validate, then Deploy:** Test refined agents in simple scenarios before critical use.

### Agent Status & Plans
- **`route_navigator_agent` (REFINED):** More robust at finding paths around obstacles.
- **`exploration_agent` (REFINED):** Now has improved traversal logic.
- **`battle_menu_navigator` (OK):** Working well.
- **`hm_advisor_agent` (NEW):** Checks which of my Pokémon can learn a given HM.
- **`trade_tracker_agent` (NEW):** To log trade opportunities (NPC, location, Pokémon wanted/offered).

## V. Current Action Plans & Hypotheses
- **Primary Goal:** Obtain the Silph Scope.
- **Secondary Goal:** Gain access to Saffron City.
- **Tertiary Goal:** Acquire a POKé DOLL for the COPYCAT quest.

- **Hypothesis 1 (Celadon/Silph Scope):** The Silph Scope is likely in a Team Rocket-controlled area within Celadon City, possibly the Game Corner.
- **Hypothesis 2 (Saffron Access):** Giving a drink (Fresh Water, Soda Pop, or Lemonade) to a thirsty guard will grant access. I will test Fresh Water first.

- **Item Hint:** A Super Nerd on 4F is buying a POKé DOLL for COPYCAT in Cerulean City. This might be a key item for a trade or quest.
- **Reminder:** Unstun Super Nerd (sprite ID 2) on Celadon Mart 4F before leaving.

- **4F Clerk Interaction:** Clerk at (6, 8) is not a standard vendor. Interaction from directly in front at (6,6) and (5,6) yields generic text. The Super Nerd's hint about the POKé DOLL suggests an item is sold here. Will test interacting from different adjacent tiles.

## VI. Disproven Hypotheses & Failed Strategies
- **Celadon 4F POKé DOLL Clerk:**
    - Hypothesis: The clerk at (6, 8) sells the POKé DOLL and is reachable.
    - Attempts:
        - Interaction from (6, 6) failed (Turn 19183).
        - Interaction from (5, 6) failed (Turn 19184).
        - Interaction from (7, 6) failed (Turn 19187).
        - Pathfinding to adjacent tile (7, 8) failed; area is physically separated (Turn 19191).
    - Conclusion: The area behind the counter is inaccessible from the main floor. The clerk cannot be interacted with directly.
- **Celadon Elevator to 4F Secret Area:**
    - Hypothesis: Using the elevator to go to 4F will lead to the inaccessible area behind the counter.
    - Attempts:
        - Took elevator to 4F (Turn 19200-19205).
    - Conclusion: This returned me to the standard 4F elevator arrival point at (2, 3). The elevator does not provide access to the area behind the counter. Hypothesis disproven.

## VII. Technical Debt & Cleanup
- **WKG - Celadon Dept. Store Escalators:** The nodes and edges for the escalators are incorrect or incomplete. Need to revisit, delete the bad entries, and re-add them systematically (add node, get ID, add next node, get ID, add edge).
- **`exploration_agent` (Suboptimal):** Fails to find paths to all reachable unseen tiles in a single run, requiring multiple calls. Needs to be refined for comprehensive, one-shot pathing.

- **`exploration_agent` (Suboptimal):** Fails to find paths to all reachable unseen tiles in a single run, requiring multiple calls. Needs to be refined for comprehensive, one-shot pathing.