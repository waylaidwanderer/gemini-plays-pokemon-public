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
    - **NPC Passability:** Some NPCs, like the Super Nerd in Rock Tunnel B1F at (4,6), can be walked through.
- **Tile Mechanics (Verified):**
    - `impassable`: Solid barrier. Cannot be entered. The subject of my current fossil hunt.
    - `ground`: Standard walkable tile.
    - `elevated_ground`: Walkable ground at a different elevation. Cannot be accessed from `ground` directly.
    - `steps`: The only tile type that allows movement between `ground` and `elevated_ground`.
    - `ladder_up` / `ladder_down`: Warps that lead to different floors.

# III. Quest Log
- **Current Quest: The Mt. Moon Fossil**
    - **Objective:** Find a fossil to give to the Rocket Grunt blocking the path at Mt. Moon B2F (30,12).
    - **Hypothesis:** One of the rocks in Mt. Moon is interactable and contains a fossil.
    - **Method:** Systematically check every single 'impassable' rock tile on all floors of Mt. Moon.
    - **Progress:** All reachable rocks on Mt. Moon 1F and the first B1F platform have been checked. Now searching a new area of B1F.
    - **Next Step:** Explore the newly discovered corridor on Mt. Moon B1F.

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

# V. Future Automation Ideas
- **Full Search Automator:** A master tool that executes the entire systematic search loop. 
    - **Logic:** 1. Call `rock_checker_automator` to get a path. 2. Execute the path. 3. Automatically press 'A' to interact. 4. Automatically call `define_map_marker` to mark the spot. 5. Repeat the loop until the tool returns no more targets.
    - **Challenge:** Would require a tool that can call other tools and press buttons, which may require a more advanced system or a stateful script.

# VI. Fossil Quest - New Hypotheses (from puzzle_solver_agent)
- **Failed Hypotheses:**
    - The fossil is in an interactable rock.
    - The Hiker on 1F at (6,7) will move if shown the revived HELIX fossil Pokémon. (Result: Dialogue unchanged).
- **Hypothesis 1 (Top Priority):** The required fossil must be obtained by 'un-reviving' my current HELIX fossil Pokémon at the Cinnabar Island lab.
- **Hypothesis 2:** Presenting the revived HELIX fossil Pokémon to the Rocket Grunt on B2F will trigger a new event.