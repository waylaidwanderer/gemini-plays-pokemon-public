# Gem's Strategic Journal (v49 - Post-Hideout Re-entry)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information is the source of truth. My own feeling of being "stuck" is likely a hallucination if the data contradicts it. I must trust the data.
- **Agent Protocol:**
    - **`battle_menu_navigator` (Refined):** This agent's understanding of the battle menu has been corrected. It now knows the move menu is a vertical list and that the party menu cursor starts on the *active* Pokémon.
- **Interaction Protocol:** If an interaction (battle, dialogue) doesn't trigger as expected, do not repeat the same input. Immediately try a different input or a different approach.
- **WKG Protocol:** After adding a transition's nodes, my immediate next action is to add the connecting edge. This must be done on the turn immediately following the map transition.
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
- **Primary Goal:** Defeat the boss of the Rocket Hideout.
- **Secondary Goal:** Find the hideout's boss.
- **Tertiary Goal:** Acquire the Silph Scope.
### Current Plan (v3)
1. The southern section of B1F (accessed from the stairs at (22, 23) on B2F) is a dead end. The grunt at (19, 19) did not have the Silph Scope.
2. **Objective:** Find the LIFT KEY. My hypothesis is that the Rocket Grunt at (16, 26) on B1F has it.
3. **Path:**
    a. Return to B2F via the warp at (22, 25) on B1F.
    b. On B2F, find the path that leads to the stairs that go down to the western part of B1F where the target grunt is.
    c. Defeat the grunt at (16, 26) and obtain the LIFT KEY.
    d. Proceed to the elevator on B2F at (25, 20) and use the key to access B4F.
    e. Explore B4F to find and confront the boss.

### Hypotheses
- **Hypothesis 1 (Silph Scope):** The Silph Scope is the final reward in this hideout, likely held by the boss.
- **Hypothesis 2 (Saffron Access):** Giving a drink from the Celadon vending machines to a thirsty guard will grant access to Saffron City.

## V. Disproven Hypotheses & Failed Strategies
- **Rocket Grunt Battle (21, 13 on B2F):** Repeatedly trying to initiate this battle has failed. This interaction is either bugged or requires a specific trigger I have not yet found. This path is on hold until all other options in the hideout are exhausted.