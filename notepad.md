# Gem's Strategic Journal (v126 - Post-Blockage Update)

## I. Core Principles & Lessons Learned
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Agent Liability:** An agent that provides consistently incorrect or dangerous advice is a liability. It must be abandoned or fixed from a safe location, not during a critical battle.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on.
- **WKG & Marker Protocol:** Be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*.
- **Tool-First Mindset:** For any complex or repetitive task, use an agent first.

## II. Game Mechanics & Battle Intel
### Confirmed ROM Hack Changes
- **Type Matchups:**
  - Psychic is SUPER-EFFECTIVE against Ghost/Poison.
  - Ghost is SUPER-EFFECTIVE against Psychic.
  - Bite (Normal) is SUPER-EFFECTIVE against Psychic.
  - Normal is NOT-VERY-EFFECTIVE against Psychic.

### Navigation & Traversal Rules
- **Defeated Trainers as Obstacles:** Defeated trainers act as impassable walls and must be navigated around. This was confirmed on Pokémon Tower 5F when a path was blocked by a defeated Channeler at (18, 8).

### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.
- **Gen 1 Move Typing:** Be aware of Gen 1 move typings. E.g., Bite and Double Kick are Normal-type.
- **Confusion & Field Moves:** When a Pokémon is confused, it may randomly select any of its moves to use, including out-of-battle moves like TELEPORT. If Teleport is used, the battle ends immediately.

### Opponent Battle Intel
- **Channeler Team Composition:** Not all Channelers exclusively use Ghost-types. Be prepared for Psychic-types and have counters like Bite ready.

## III. Active Plans & Hypotheses
### **Current Plan: Pokémon Tower Ascent & Final Floor**
1.  **Situation:** Reached the 6th floor of the Pokémon Tower.
2.  **Action Plan:**
    a. **Explore:** Systematically explore the 6th floor, clearing all trainers and collecting any items.
    b. **Heal:** Use the friendly Channeler on 5F as a free healing station between battles by descending the stairs if necessary.
    c. **Ascend:** Find the stairs to the 7th floor to confront Team Rocket and rescue Mr. Fuji.

### Long-Term Goals & Hypotheses
- **Celadon Gym:** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Thirsty Guards:** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Snorlax (Route 16):** Requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued from the Pokémon Tower.

## IV. Agent Development Log
### A. Active Agents & Refinements
- **`pathfinding_agent` (v3 - REFINED):** Consolidated agent for pathfinding. **REFINEMENT COMPLETE: Logic corrected to treat all NPCs (except Pikachu), including defeated trainers, as impassable obstacles. Agent is now reliable for pathfinding.**
- **`wkg_manager_agent` (v2 - RELIABLE):** Successfully identifies existing nodes and creates edges without duplication.
- **`pc_navigator_agent` (v2 - RELIABLE):** Successfully navigates the PC by using 'BILL's PC'.
- **`battle_strategist_agent` (v1 - RELIABLE):** Provides turn-by-turn battle advice.
- **`team_composition_advisor_agent` (v1 - NEEDS REFINEMENT):** Provides team/training advice. **TODO:** Refine to explicitly include EXP grinding optimization logic.

### B. Agent Development Backlog
- **`shopping_planner_agent`:** To plan TM and item purchases.
- **`item_finder_agent`:** To plan paths for collecting all items on a map.
- **`healing_route_planner_agent`:** To find the most efficient path to a Pokémon Center.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.
- **PC Glitch Workaround:** Selecting 'Gem's PC' is bugged. Use 'BILL's PC' instead.
- **5F Healing Source:** The healing is provided by the friendly Channeler NPC at (13, 9), not a purified tile.

## VI. Critical Reminders
- **Maintain Poké Ball Stock:** Always keep at least 10-20 Poké Balls on hand.

### Battle Intel Update
- **Normal-Type Immunity:** Confirmed that Normal-type moves (like Bite) are completely ineffective against Ghost-types. This is a critical Gen 1 mechanic to remember.