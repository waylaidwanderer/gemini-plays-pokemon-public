# I. Meta-Strategy & Core Principles
1.  **Immediate Maintenance:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified, regardless of game state. Deferring these tasks is a critical failure.
2.  **Proactive Automation & Refinement:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority. If an agent or tool is suboptimal, I must prioritize refining it immediately.
3.  **Trust, But Verify:** I must trust the outputs of my agents and system data. However, if a tool's output contradicts the Game State Information, my assumption must be that the tool is wrong, and I must debug it.
4.  **Hypothesis-Driven Exploration:** All exploration must be guided by a clear, documented hypothesis. I must avoid wandering aimlessly and systematically test one variable at a time, documenting all results.
5.  **Warp Discipline:** After every warp, my first action must be to check and, if necessary, create/update markers on **both** the departure and arrival maps.
6.  **Mandatory Self-Assessment:** Every 50 turns, I must perform a structured self-review to ensure my strategies, documentation, and tool usage remain optimal and aligned with my core principles.
7.  **Efficiency Over Fixation:** If a simple automation tool fails during a low-stakes, repetitive task (like a wild battle), it is more efficient to complete the task manually and fix the tool later, rather than getting stuck debugging mid-task.
8.  **Battle Menu Anomaly (Confirmed):** The system's tool execution is unreliable when combining directional inputs with an action button ('A') in a single turn. Automation must separate these into separate turns.

# II. Game World Mechanics
- **Gameplay Mechanics:**
    - **Trap Battles:** Certain wild encounters appear to be 'trap' battles where the 'RUN' option is disabled (Observed: Wigglytuff, KADABRA; Suspected: Ditto).
    - **Fossil Regeneration:** The Cinnabar Lab has a machine to regenerate fossils.
- **Tile & Movement Mechanics (Player-Discovered):**
    - **Passable NPCs:** Some NPCs that appear to block paths can be walked through (Observed: Super Nerd in Rock Tunnel B1F at (4,6)). Must be tested case-by-case.
    - **Ladder/Warp Re-use:** To use a 1x1 warp tile (like a ladder) immediately after arriving on it, one must first step off the tile and then step back on.
    - **Ledge Traversal:** Ledges are one-way only. Jumping down is an irreversible move for that path.
    - **Elevation Change:** Movement between 'ground' and 'elevated_ground' tiles is only possible via an intermediate 'steps' tile. Direct transitions are impassable.
    - **Interactable Scenery Hypothesis:** Currently testing the hypothesis that one specific 'impassable' rock tile in Mt. Moon is interactable to solve a puzzle.

# III. Quest Log
- **Current Quest: The Mt. Moon Fossil**
    - **Objective:** Find a fossil item to give to the Rocket Grunt at Mt. Moon B2F (30, 12).
    - **Current Plan:** Systematically check every 'impassable' tile (rock formation) in Mt. Moon using the `map_interaction_planner` tool to test the hypothesis that one is interactable.
    - **Progress:** All reachable rocks on Mt. Moon 1F are being checked. If this floor yields nothing, the search will continue on B1F and B2F.
    - **Active Hypotheses (from Agent):**
        1. An interactable rock formation somewhere in Mt. Moon gives the fossil. (IN PROGRESS)
        2. A Pokémon with the Pickup ability can find the fossil.
        3. Using the move 'Dig' on a specific tile unearths the fossil.
        4. The Hiker at 1F (6, 7) moves after a different trigger (already tested post-Super Nerd, but keeping in mind).
    - **Contingency Plan:** If the rock search fails on all floors, the next step is to test other hypotheses, such as using the ITEMFINDER systematically or acquiring a Pokémon with 'Dig' or 'Pickup'.
    - **Failed Hypotheses Log (Summary):** Reviving the fossil, defeating the Super Nerd, interacting with scenery, using items (MOON STONE), manipulating party composition (nicknames, fainted status, species), and using the ITEMFINDER on B2F have all failed to produce the fossil.

# IV. Battle Intel
- **Type Effectiveness Chart (Verified):**
    - Water is super-effective against Rock/Ground (Observed: OMANYTE's SURF vs GEODUDE).
    - Water is not very effective against Bug/Grass (Observed: OMANYTE's BUBBLEBEAM vs PARAS).
    - Poison is not very effective against Poison/Flying (Confirmed: ECHO's SLUDGE vs ZUBAT) and Rock/Ground (Observed: ECHO's SLUDGE vs GEODUDE).
    - Flying is not very effective against Rock/Ground (Observed: ECHO's FLY vs GEODUDE).
- **Notable Trainer Rosters:**
    - **Sabrina (Saffron Gym):** MR. MIME (Lv 65 - PSYCHIC), HYPNO (Lv 64 - PSYWAVE), SLOWBRO (Lv 64 - PSYCHIC), JYNX (Lv 64 - BLIZZARD, BUBBLEBEAM, DREAM EATER, LOVELY KISS), GENGAR (Lv 64 - NIGHT SHADE, PSYCHIC), ALAKAZAM (Lv 65 - THUNDER WAVE, PSYCHIC).
    - **SMITH (Cerulean Cave):** AERODACTYL (Lv 65 - HYPER BEAM, ROCK SLIDE).
    - **Brock (Pewter Gym):** OMASTAR (Lv 64 - HYDRO PUMP, BLIZZARD), ONIX (Lv 65 - EARTHQUAKE, ROCK SLIDE), KABUTOPS (Lv 64 - SWORDS DANCE, SLASH), GOLEM (Lv 64 - ROCK SLIDE), NINETALES (Lv 64 - REFLECT), AERODACTYL (Lv 65 - FLY).
- **Wild Pokémon Locations:**
    - **Cerulean Cave:** WIGGLYTUFF (Lv 62 - LOVELY KISS, DOUBLE-EDGE, REST), SANDSLASH (Lv 63 - SWORDS DANCE, EARTHQUAKE), GOLEM (Lv 64 - EXPLOSION), LICKITUNG (Lv 61 - WRAP), CHANSEY (Lv 63 - DEFENSE CURL, MEGA PUNCH), RAICHU (Lv 64 - AGILITY).
- **Tool Improvement Idea (from Overwatch):** Enhance `map_interaction_planner` to provide specific failure reasons, distinguishing between simple obstacles and puzzle elements like boulder barriers.
- **Tool Improvement Idea (from Overwatch):** Enhance `map_interaction_planner` to provide specific failure reasons, distinguishing between simple obstacles and puzzle elements like boulder barriers.