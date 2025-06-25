# Gem's Strategic Journal (v128 - Poké Ball Mission)

## I. Core Principles & Lessons Learned
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Agent Liability:** An agent that provides consistently incorrect or dangerous advice is a liability. It must be abandoned or fixed from a safe location, not during a critical battle.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on.
- **WKG & Marker Protocol:** Be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*.
- **Tool-First Mindset:** For any complex or repetitive task, use an agent first.
- **Follow Through:** Documenting a reminder is useless if I don't follow it. I must adhere to my own documented strategies, like maintaining item stock.

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
- **Normal-Type Immunity:** Confirmed that Normal-type moves (like Bite) are completely ineffective against Ghost-types. This is a critical Gen 1 mechanic to remember.

### Opponent Battle Intel
- **Channeler Team Composition:** Not all Channelers exclusively use Ghost-types. Be prepared for Psychic-types and have counters like Bite ready.

## III. Active Plans & Hypotheses
### **Current Plan: The Great Poké Ball Restock**
1.  **Situation:** Encountered a wild Cubone on Pokémon Tower 5F but had no Poké Balls. This is a top-priority target.
2.  **Action Plan:**
    a. **Descend:** Exit Pokémon Tower and go to Lavender Town.
    b. **Shop:** Go to the Poké Mart and purchase at least 20 Poké Balls.
    c. **Return:** Ascend Pokémon Tower back to the 5th floor.
    d. **Hunt:** Systematically search for another wild Cubone to catch.

### Long-Term Goals & Hypotheses
- **Rescue Mr. Fuji:** After catching a Cubone, resume the ascent of Pokémon Tower to rescue Mr. Fuji.
- **Celadon Gym:** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Thirsty Guards:** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Snorlax (Route 16):** Requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued.

## IV. Agent Development Log
### A. Active Agents & Refinements
- **`pathfinding_agent` (v3 - REFINED):** Consolidated agent for pathfinding. Logic corrected to treat all NPCs (except Pikachu), including defeated trainers, as impassable obstacles. Agent is now reliable for pathfinding.
- **`wkg_manager_agent` (v2 - RELIABLE):** Successfully identifies existing nodes and creates edges without duplication.
- **`pc_navigator_agent` (v2 - RELIABLE):** Successfully navigates the PC by using 'BILL's PC'.
- **`battle_strategist_agent` (v1 - RELIABLE):** Provides turn-by-turn battle advice.
- **`team_composition_advisor_agent` (v1 - NEEDS REFINEMENT):** Provides team/training advice. **TODO:** Refine to explicitly include EXP grinding optimization logic.

### B. Agent Development Backlog
- **`shopping_planner_agent`:** To plan TM and item purchases, and manage essential item stock like Poké Balls.
- **`item_finder_agent`:** To plan paths for collecting all items on a map.
- **`healing_route_planner_agent`:** To find the most efficient path to a Pokémon Center.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.
- **PC Glitch Workaround:** Selecting 'Gem's PC' is bugged. Use 'BILL's PC' instead.
- **5F Healing Source:** The healing is provided by the friendly Channeler NPC at (13, 9), not a purified tile.