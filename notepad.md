# Gem's Strategic Journal (v86 - Agent Cleanup)

## I. Core Principles & Lessons Learned
- **Trust the Data, Not Frustration:** Game State Information (`map_id`, `current_position`) is the absolute source of truth. My own feeling of being "stuck" is a hallucination if the data contradicts it. ALWAYS verify location after a map transition BEFORE acting.
- **Interaction Protocol:** If an interaction doesn't trigger a battle, it's a non-battling NPC or one I've already defeated. Do not repeat the interaction; mark the NPC and move on.
- **WKG & Marker Protocol (v10):**
    - After any map transition, immediately add nodes/edge to WKG and mark both sides of the warp as 'Used'.
    - **Check-Then-Add Policy:** Before adding any new node or edge, query the WKG (using `run_code`) to ensure the element doesn't already exist. My current script is buggy and needs to be fixed.
    - **Correct ID Protocol:** Follow a strict three-step process: 1. `add_node` for source, retrieve ID. 2. `add_node` for destination, retrieve ID. 3. `add_edge` using the *correct, retrieved IDs*.
- **Handling Bugs:** If a menu appears stuck on one option, test other options (like moving the cursor or selecting 'CANCEL') before assuming the game is frozen. Repeatedly trying the bugged option is inefficient.

## II. Hallucination & Correction Log
- **MAJOR (T22035-T22134): Rocket Hideout & Game Corner Hallucinations.** Repeatedly believed I had successfully changed maps (B4F -> B2F, Game Corner -> Celadon) when I had not. This led to creating incorrect WKG nodes and map markers. **Lesson:** ALWAYS verify `map_id` and `current_position` from Game State Info *after* any warp attempt.
- **CRITICAL (T22304-T22330):** System repeatedly warned of reachable unseen tiles on Pokemon Tower 2F. I was hallucinating that the floor was fully explored. I have now explored that floor.
- **Visual Bug (Confirmed):** ECHO (Golbat)'s type has been incorrectly displayed as GHOST instead of Flying/Poison in multiple battles.

## III. Game Mechanics & Battle Intel
- **Level Caps:** 0 badges: 12, 1 badge: 21, 2 badges: 24, 3 badges: 35.
- **HM Field Use:** HMs MUST be taught to a compatible Pokémon to enable their field use. FLY cannot be used indoors.
- **EXP. All:** Distributes EXP to all non-fainted party members. Pokémon at the level cap will not gain actual EXP.
- **Type Effectiveness (Confirmed):**
    - Poison-type moves are 'not very effective' against Flying/Poison types (Acid vs. Golbat).

## IV. Action Plans & Hypotheses
### Current Objectives
- **Primary Goal:** Use the Silph Scope to clear the Pokémon Tower.
- **Secondary Goal:** Find a way to heal my critically injured party.
### Current Plan (v30 - Pokémon Tower Ascent)
1.  Navigate Pokémon Tower 4F to find the stairs up.
2.  Avoid all trainer battles due to party's critical condition.
### Future Plans & Hypotheses
- **Team Composition:** I must use my `team_composition_advisor_agent` *before* major battles.
- **Hypothesis 1 (Snorlax):** The Snorlax on Route 16 requires the Poké Flute to be moved.
- **Hypothesis 2 (Celadon Gym):** The gym might be un-bugged now that the Rocket Hideout is cleared. Will investigate after Pokémon Tower.
- **Hypothesis 3 (Thirsty Guards):** Need to test if giving a guard a drink (e.g., Fresh Water) will grant passage.

## V. Completed Intel & Disproven Hypotheses
- **LIFT KEY Location:** Dropped by a non-battling Rocket Grunt at Rocket Hideout B3F (11, 23).
- **Giovanni Defeated:** Defeated Giovanni on Rocket Hideout B4F. He dropped the Silph Scope.
- **Defeat Mechanic (Rocket Hideout):** Losing a battle in a trainer in the hideout does not send you back to the Pokémon Center.
- **Spinner Maze Mapping (B2F & B3F):** All spinners on these floors have been manually mapped and solved.
- **Rival Pixel Defeated:** Defeated Pixel on Pokémon Tower 2F.

## VI. Agent Status & Refinement Log
- **`pathfinder_agent` (DELETED):** Functionality consolidated into `stealth_pathfinder_agent`.
- **`spinner_maze_solver_agent` (DELETED):** Functionality consolidated into `pathfinder_agent`.
- **`battle_advisor_agent` (OPERATIONAL - REFINED):** Successfully refined the agent to handle statefulness by adding a `previous_player_action` input. It no longer recommends switching immediately after a switch-in and provides excellent tactical advice. It is now a primary tool for all battles.
- **`team_composition_advisor_agent` (UNDERUTILIZED):** Must be used before major battles. Acknowledged miss on the Rival battle.

## VII. AI Feedback & Action Items (T22291, T22320, T22380)
- **Agent Consolidation:** `spinner_maze_solver_agent` is now redundant and has been deleted.
- **Agent Usage:** I failed to use the `team_composition_advisor_agent` before my last Rival battle. I must use it for all future major encounters.
- **Map Markers:** I have been inconsistent. I need to maintain my protocol of marking both sides of a transition immediately.
- **WKG Scripting:** My WKG check script is buggy. I need to fix it before adding new connections.

### Agent Development Plan
- **New Agent: `stealth_pathfinder_agent`**: My current `pathfinder_agent` is flawed as it doesn't account for trainer line of sight. I will create a new agent that takes start/end coordinates, the map XML, and a list of trainer coordinates with their facing directions. The agent's code will need to calculate the line of sight for each trainer (a straight line of tiles in the direction they are facing) and treat those tiles as impassable walls in its pathfinding algorithm. This will allow for true stealth navigation.

- **`define_map_marker` Tool Rule:** The `map_id` argument requires a numeric string (e.g., "4"), not the map's name string (e.g., "LAVENDER_TOWN"). I keep forgetting this.

- **Hallucination (T22477):** Believed Pokémon Tower 3F was mostly explored with only 2 unseen tiles. System corrected me that there were actually 5 (now 6). This reveals a significant unexplored area in the northeast I must now investigate.