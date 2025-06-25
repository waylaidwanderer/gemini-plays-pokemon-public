# Gem's Strategic Journal (v130 - Pokémon Tower Reflection)

## I. Core Principles & Lessons Learned
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it. I must cross-reference my perceived location with the game state data before acting.
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
- **Poison Status Immunity:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves (e.g., SMOG). Confirmed when CRAG was poisoned.

### Navigation & Traversal Rules
- **Defeated Trainers as Obstacles:** Defeated trainers act as impassable walls and must be navigated around. Confirmed on Pokémon Tower 5F.

### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.
- **Gen 1 Move Typing:** Be aware of Gen 1 move typings. E.g., Bite and Double Kick are Normal-type.
- **Confusion & Field Moves:** When a Pokémon is confused, it may randomly select any of its moves to use, including out-of-battle moves like TELEPORT. If Teleport is used, the battle ends immediately.
- **Normal-Type Immunity:** Confirmed that Normal-type moves (like Bite) are completely ineffective against Ghost-types.
- **Inventory Limit:** The displayed inventory limit (e.g., 28/20) is a visual bug. The actual limit is higher. Confirmed by purchasing 20 Poké Balls while at 28/20 items.

### Opponent Battle Intel
- **Channeler Team Composition:** Not all Channelers exclusively use Ghost-types. Be prepared for Psychic-types and have counters like Bite ready.

## III. Active Plans & Goals
### **Current Plan: Rescue Mr. Fuji**
1.  **Situation:** I have Poké Balls and have re-entered the Pokémon Tower.
2.  **Primary Goal:** Ascend the Pokémon Tower to find and rescue Mr. Fuji.
3.  **Secondary Goal:** Find and catch a wild Cubone on the way up.

### Long-Term Goals
- **Celadon Gym:** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Thirsty Guards:** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.
- **Snorlax (Route 16):** Requires the Poké Flute. Mr. Fuji is the most likely source after he is rescued.

## IV. Unverified Assumptions (To Be Tested)
- **Tower Layout:** Is the path from 6F to the top linear, or is it a maze?
- **Final Ghost:** Is the ghost that blocked the stairs to 7F gone for good?
- **Progression Trigger:** Is defeating all Channelers the only way to progress, or is there a puzzle?
- **Wild Encounters:** Are there other rare Pokémon besides Gastly and Cubone on higher floors?
- **Healing Locations:** Is the 5F healer the only one in the tower?
- **Mr. Fuji's Location:** Is Mr. Fuji at the very top, or on a lower floor?

## V. Agent Development Log
### A. Active Agents & Refinements
- **`pathfinding_agent` (v3):** Reliable for on-map pathfinding.
- **`wkg_manager_agent` (v2):** Reliable for WKG updates.
- **`pc_navigator_agent` (v2):** Reliable for PC navigation.
- **`battle_strategist_agent` (v1):** Reliable for battle advice.
- **`team_composition_advisor_agent` (v2):** Refined to include EXP grinding optimization logic.

### B. Agent Development Backlog
- **`item_finder_agent`:** Plan efficient routes to collect all items on a map.
- **`healing_route_planner_agent`:** Find the most efficient path to a Pokémon Center using the WKG.

## VI. Completed Intel & Disproven Hypotheses
- **Poké Ball Mission:** Completed. Purchased 20 Poké Balls.
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.
- **PC Glitch Workaround:** Selecting 'Gem's PC' is bugged. Use 'BILL's PC' instead.
- **Inventory Limit is Visual Bug:** Confirmed the inventory can hold more than the displayed limit.
- **5F Healing Source:** The friendly Channeler at (13, 9) is a permanent, reusable healing spot.

### Pokémon Evolutions
- CRAG (Geodude) -> Graveler at Lv. 25 in Pokémon Tower 4F.