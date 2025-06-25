# Gem's Strategic Journal (v124 - Notepad Reorganization)

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

### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.
- **Gen 1 Move Typing:** Be aware of Gen 1 move typings. E.g., Bite and Double Kick are Normal-type.
- **Confusion & Field Moves:** When a Pokémon is confused, it may randomly select any of its moves to use, including out-of-battle moves like TELEPORT. If Teleport is used, the battle ends immediately.

### Opponent Battle Intel
- **Channeler (Pokémon Tower 6F, (17,6)):**
  - Team: Lv33 Hypno, Lv33 Haunter.
  - Hypno knows Psychic, Confusion, and Poison Gas.
- **Channeler Team Composition:** Not all Channelers exclusively use Ghost-types. Be prepared for Psychic-types and have counters like Bite ready.

## III. Active Plans & Hypotheses
### **Current Plan: Pokémon Tower Ascent & Training (v3)**
1.  **Situation:** Ascending the Pokémon Tower. My team, specifically Spoonbende and Phantom, is underleveled.
2.  **Action Plan:**
    a. **Establish Base on 5F:** Use the friendly Channeler at (13, 9) on 5F as a reusable, full-party healing spot.
    b. **Ascend & Train:** Systematically clear the remaining trainers on this floor. My next target is the Channeler at (18, 8).
    c. **Contingency:** If trainer battles prove too difficult, grind on wild Pokémon on floors 4F/5F before re-attempting.
    d. **Battle Strategy:** Leverage known type-matchup changes, especially Psychic vs. Ghost/Poison and Bite vs. Psychic.

### Long-Term Goals & Hypotheses
- **Celadon Gym:** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Thirsty Guards:** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Snorlax (Route 16):** Requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued from the Pokémon Tower.

## IV. Agent Development Log
### A. Active Agents & Refinements
- **`pathfinding_agent` (v2 - REFINED):** Consolidated agent for pathfinding. Logic corrected to no longer avoid the line of sight of *defeated* trainers.
- **`wkg_manager_agent` (v2 - RELIABLE):** Successfully identifies existing nodes and creates edges without duplication.
- **`pc_navigator_agent` (v2 - RELIABLE):** Successfully navigates the PC by using 'BILL's PC'.
- **`battle_strategist_agent` (v1 - RELIABLE):** Provides turn-by-turn battle advice.

### B. Agent Development Backlog
- **`shopping_planner_agent`:** To plan TM and item purchases.
- **`item_finder_agent`:** To plan paths for collecting all items on a map.
- **`healing_route_planner_agent`:** To find the most efficient path to a Pokémon Center.
- **`exp_grinding_optimizer_agent`:** To analyze known wild encounters and recommend the most efficient training spots.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.
- **PC Glitch Workaround:** Selecting 'Gem's PC' is bugged. Use 'BILL's PC' instead.
- **DISPROVEN:** The healing spot on 5F is a tile at (12,10). **CORRECTION:** The healing is provided by the friendly Channeler NPC at (13, 9) upon interaction.

## VI. Critical Reminders
- **Maintain Poké Ball Stock:** Always keep at least 10-20 Poké Balls on hand.