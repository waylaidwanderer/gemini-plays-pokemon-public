# Gem's Strategic Journal (v51 - Pre-Giovanni)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information is the source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it. I must trust the data.
- **Check Key Items:** After significant events or acquiring items, always check the Key Items pocket in the inventory. I wasted significant time searching for the LIFT KEY when I already had it.
- **Agent Protocol:**
    - `battle_menu_navigator` (Refined): This agent's understanding of the battle menu has been corrected. It now knows the move menu is a vertical list and that the party menu cursor starts on the *active* Pokémon.
    - `map_explorer_agent`: A new agent to identify all items and undefeated trainers on a map. Needs refinement to correctly ignore defeated trainers on *other* maps.
- **Interaction Protocol:** If an interaction (battle, dialogue) doesn't trigger as expected, do not repeat the same input. Immediately try a different input or a different approach.
- **WKG Protocol:** After adding a transition's nodes, my immediate next action is to add the connecting edge. I must verify my `map_id` *before* calling the tool.
- **Proactive NPC Management:** Be mindful of moving NPCs that can block paths.

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

### Other Locations
- **Lavender Town:** Pokémon Tower is impassable without the Silph Scope.
- **Route 10:** Path to Lavender Town is south, past the Pokémon Center and Rock Tunnel.

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Defeat the boss of the Rocket Hideout.
- **Secondary Goal:** Acquire the Silph Scope.

### Current Plan (v5)
1. **Objective:** Confront the boss, Giovanni, on B4F.
2. **Path:** Navigate the final corridor on B4F to reach Giovanni at (26, 4).
3. **Action:** Initiate battle and defeat him to acquire the Silph Scope.

### Hypotheses
- **Hypothesis 1 (Silph Scope):** The Silph Scope is the final reward in this hideout, held by Giovanni.
- **Hypothesis 2 (Saffron Access):** Giving a drink from the Celadon vending machines to a thirsty guard at one of the Saffron City gatehouses will grant access.

## V. Disproven Hypotheses & Failed Strategies
- **Rocket Grunt Battle (21, 13 on B2F):** Repeatedly trying to initiate this battle has failed. This interaction is either bugged or requires a specific trigger I have not yet found. This path is on hold.
- **Lift Key Location:** The Lift Key was not held by a specific grunt. I discovered I already possessed it.
- **B4F Items:** The `map_explorer_agent` confirmed there are no more item balls on this floor.