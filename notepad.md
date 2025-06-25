# Gem's Strategic Journal (v132 - Post-Tower Triumph)

## I. Core Principles & Lessons Learned
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it. I must cross-reference my perceived location with the game state data before acting.
- **Verify Assumptions:** Do not record intel as "completed" or "confirmed" until it has been empirically verified. Premature conclusions lead to flawed strategies.
- **Agent Liability:** An agent that provides consistently incorrect or dangerous advice is a liability. It must be abandoned or fixed from a safe location, not during a critical battle.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on.
- **WKG & Marker Protocol:** Be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*. Consolidate markers on single tiles for clarity.
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
- **Ghost-Type Immunity:** Confirmed that Ghost-type moves (like Lick) are completely ineffective against Normal-types.
- **Inventory Limit:** The displayed inventory limit (e.g., 28/20) is a visual bug. The actual limit is higher. Confirmed by purchasing 20 Poké Balls while at 28/20 items.

### Opponent Battle Intel
- **Channeler Team Composition:** Not all Channelers exclusively use Ghost-types. Be prepared for Psychic-types and have counters like Bite ready.

## III. Active Plans & Goals
### **Current Plan: Explore Post-Tower World**
1.  **Situation:** I have rescued Mr. Fuji and received the POKé FLUTE. My party is fully healed.
2.  **Primary Goal:** Defeat the next available Gym Leader.
3.  **Secondary Goal:** Wake up the Snorlax on Route 12 using the POKé FLUTE.
4.  **Tertiary Goal:** Investigate Celadon City Gym to see if it's unblocked.

### Long-Term Goals
- **Thirsty Guards:** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.

## IV. Agent Development Log
### A. Active Agents & Refinements
- **`pathfinding_agent` (v3):** Reliable for on-map pathfinding.
- **`wkg_manager_agent` (v3):** Refined to handle null destination_entry_point values correctly.
- **`pc_navigator_agent` (v2):** Reliable for PC navigation.
- **`battle_strategist_agent` (v2):** Refined to better differentiate between wild/trainer battles and handle low-HP scenarios.
- **`team_composition_advisor_agent` (v2):** Refined to include EXP grinding optimization logic.

### B. Agent Development Backlog
- **`item_finder_agent`:** Plan efficient routes to collect all items on a map.
- **`healing_route_planner_agent`:** Find the most efficient path to a Pokémon Center using the WKG.

## V. Completed Intel & Disproven Hypotheses
- **Poké Ball Mission:** Completed. Purchased 20 Poké Balls.
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.
- **PC Glitch Workaround:** Selecting 'Gem's PC' is bugged. Use 'BILL's PC' instead.
- **Inventory Limit is Visual Bug:** Confirmed the inventory can hold more than the displayed limit.
- **Mr. Fuji Rescued:** Rescued from Team Rocket at the top of Pokémon Tower. Received POKé FLUTE as a reward.
- **Celadon Gym:** The gym might be un-bugged now that the Rocket Hideout is cleared. (Moved to Active Plans for investigation)
- **Thirsty Guards:** Need to test if giving a guard a drink will grant passage. (Moved to Long-Term Goals for investigation)

### Pokémon Evolutions
- CRAG (Geodude) -> Graveler at Lv. 25 in Pokémon Tower 4F.