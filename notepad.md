# Gem's Strategic Journal (v134 - Route 12 Snorlax)

## I. Core Principles & Lessons Learned
- **Trust the Data:** Game State Information is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it.
- **Verify Assumptions:** Do not record intel as "completed" or "confirmed" until it has been empirically verified.
- **Agent Liability:** An agent that provides consistently incorrect or dangerous advice is a liability. It must be abandoned or fixed from a safe location, not during a critical battle.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Mark and move on.
- **WKG & Marker Protocol:** Be diligent about marking key points (like warp arrivals and defeated trainers) *immediately*. Consolidate markers on single tiles for clarity.
- **Tool-First Mindset:** For any complex or repetitive task, use an agent first.

## II. Game Mechanics & Battle Intel
### Confirmed ROM Hack Changes
- **Type Matchups:**
  - Psychic is SUPER-EFFECTIVE against Ghost/Poison.
  - Ghost is SUPER-EFFECTIVE against Psychic.
  - Bite (Normal) is SUPER-EFFECTIVE against Psychic.
  - Normal is NOT-VERY-EFFECTIVE against Psychic.
- **Poison Status Immunity:** Rock/Ground-types are NOT immune to being poisoned by Poison-type moves.

### Navigation & Traversal Rules
- **Defeated Trainers as Obstacles:** Defeated trainers act as impassable walls and must be navigated around.

### General Mechanics
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs must be taught to a Pokémon to enable field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap gain no actual EXP.
- **Gen 1 Move Typing:** Bite and Double Kick are Normal-type.
- **Confusion & Field Moves:** A confused Pokémon may use any move, including TELEPORT, which ends the battle.
- **Normal/Ghost Immunities:** Normal moves are ineffective against Ghosts, and Ghost moves are ineffective against Normals.

## III. Active Plans & Goals
### **Current Plan: Confront the Snorlax**
1.  **Situation:** I have found a second Snorlax at the end of the Route 12 pier. SPARKY is critically injured.
2.  **Primary Goal:** Defeat the next available Gym Leader.
3.  **Secondary Goal:** Get past the Snorlax on Route 12.
4.  **Tertiary Goal:** Heal SPARKY at the next available opportunity.
5.  **Plan:** Use the POKé FLUTE from the inventory to wake the Snorlax. Be prepared for a battle.

### Long-Term Goals
- **Thirsty Guards:** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage to Saffron City.

## IV. Agent Development Log
### A. Active Agents & Refinements
- **`pathfinding_agent` (v3.3 - CRITICALLY UNRELIABLE):**
  - **History:** Failed three times on Route 12 (T25816, T25818, T25819), attempting to path into impassable tiles. Its map parsing is fundamentally broken.
  - **Status:** Performed multiple major prompt overhauls to enforce strict tile-type checking. The agent is on its last chance before being scrapped and rebuilt.
- **`wkg_manager_agent` (v3):** Reliable.
- **`pc_navigator_agent` (v2):** Reliable.
- **`battle_strategist_agent` (v2):** Reliable.
- **`team_composition_advisor_agent` (v2):** Reliable.

### B. Agent Development Backlog
- **`item_finder_agent`:** Plan efficient routes to collect all items on a map.
- **`fishing_advisor_agent`:** Analyze map & rod to suggest best fishing spots/catches.
- **`hm_planner_agent`:** Suggest best Pokémon for HMs based on current moves and future utility.
- **`sales_data_agent`:** Track item prices across different Poké Marts to find the best deals.

## V. Completed Intel & Disproven Hypotheses
- **Poké Ball Mission:** Completed.
- **LIFT KEY Location:** Dropped by a Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated on Rocket Hideout B4F, dropped the Silph Scope.
- **Rival Pixel Defeated:** Defeated on Pokémon Tower 2F.
- **PC Glitch Workaround:** Use 'BILL's PC' instead of 'Gem's PC'.
- **Mr. Fuji Rescued:** Rescued from Team Rocket; received POKé FLUTE.
- **Celadon Gym:** Blocked by unresponsive trainers.
- **Snorlax on Route 12 (North):** Confirmed red herring. The path remains blocked. The true path is the western pier.

## VI. Unverified Assumptions & Future Tests
- **Snorlax on Route 12 (South):** The POKé FLUTE is assumed to work. This is the primary hypothesis to test.
- **Path Forward:** The path south past the Snorlax is assumed to be the correct progression path.