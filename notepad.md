# I. Core Principles & Lessons Learned
1.  **Immediate Maintenance:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified. Deferring these tasks is a critical failure.
2.  **Proactive Automation & Refinement:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority. If an agent or tool is suboptimal, I must prioritize refining it immediately.
3.  **Trust, But Verify:** I must trust the outputs of my agents and system data. However, if a tool's output contradicts the Game State Information, my assumption must be that the tool is wrong, and I must debug it.
4.  **Abandon Failed Hypotheses:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach. I must not get stuck on a single solution.
5.  **CRITICAL - Data Verification & State Tracking:** My most severe failures stem from hallucinating game state variables (location, turn count, etc.). I MUST verify my current map ID, coordinates, and all other data from the Game State Information *before* every single action and trust it over my memory.

# II. Game Mechanics & World Data
- **Trap Battles:** Certain wild encounters appear to be 'trap' battles where the 'RUN' option is disabled (Observed: Wigglytuff, KADABRA; Suspected: Ditto).

    - RAICHU (Lv 64): Moves: AGILITY

### 1. Sabrina (Saffron City Gym)
- **Roster:**
    - MR. MIME (Lv 65) - Moves: PSYCHIC
    - HYPNO (Lv 64) - Moves: PSYWAVE
    - SLOWBRO (Lv 64) - Moves: PSYCHIC
    - JYNX (Lv 64) - Moves: BLIZZARD, BUBBLEBEAM, DREAM EATER, LOVELY KISS
    - GENGAR (Lv 64) - Moves: NIGHT SHADE, PSYCHIC
    - ALAKAZAM (Lv 65) - Moves: THUNDER WAVE, PSYCHIC

### 2. SMITH (Cerulean Cave B1F)
- **Roster:**
    - AERODACTYL (Lv 65) - Moves: HYPER BEAM, ROCK SLIDE

### 3. Brock (Pewter City Gym)
- **Roster:**
    - OMASTAR (Lv 64) - Moves: HYDRO PUMP, BLIZZARD
    - ONIX (Lv 65) - Moves: EARTHQUAKE, ROCK SLIDE
    - KABUTOPS (Lv 64) - Moves: SWORDS DANCE, SLASH
    - GOLEM (Lv 64) - Moves: ROCK SLIDE
    - NINETALES (Lv 64) - Moves: REFLECT
    - AERODACTYL (Lv 65) - Moves: FLY

### 4. Cerulean Cave Wild Pokémon
- **Observed Species & Moves:**
    - WIGGLYTUFF (Lv 62) - Moves: LOVELY KISS, DOUBLE-EDGE, REST
    - SANDSLASH (Lv 63) - Moves: SWORDS DANCE, EARTHQUAKE
    - GOLEM (Lv 64) - Moves: EXPLOSION
    - LICKITUNG (Lv 61): Moves: WRAP
    - CHANSEY (Lv 63): Moves: DEFENSE CURL, MEGA PUNCH
    - RAICHU (Lv 64): Moves: AGILITY

# VI. Technical Documentation

# VII. Lessons from Tool Failures & Debugging
## A. automated_path_navigator on Mt. Moon B2F (Turn 202577)
- **Symptom:** Tool returned "No path found. Path blocked by impassable terrain." when attempting to path from (22, 18) to (30, 11).
- **Initial Hypothesis:** The tool's logic for handling `elevated_ground` and `steps` was flawed.
- **Investigation:** Manually traced the map XML. Discovered an `impassable` wall at (25, 18) that completely isolates the starting platform from the `steps` needed to reach the ground level.
- **Conclusion:** The tool was **correct**. My manual map assessment was flawed; I failed to account for a partition wall.
- **Lesson:** TRUST THE TOOL. Before debugging the tool's code, perform a rigorous manual trace of the map XML to verify that a path is *physically possible*. A "no path found" result is often an accurate reflection of a partitioned map.

## D. Agent-Generated Hypotheses (Turn 202944)
1.  **Sole Party Member:** The fossil Pokémon must be the sole member of the party, thereby forcing it into the lead position and circumventing the bugged menu.
    - Test Plan: Travel to the nearest Pokémon Center. Use the PC to deposit all Pokémon except for HELIX. With HELIX as the only Pokémon in the party, return to Mt. Moon B2F and approach the area blocked by the Rocket Grunt.
2.  **Fossil Item:** The Rocket Grunt requires the actual 'Helix Fossil' or 'Dome Fossil' item, not the revived fossil Pokémon.
    - Test Plan: Check inventory/PC for a fossil item. If none, investigate ways to re-acquire one (e.g., Pewter Museum). Return to Mt. Moon with the fossil item and check the grunt.
3.  **Cinnabar Lab Flag:** A story flag must be triggered at the Cinnabar Island Pokémon Lab before the Mt. Moon event can be resolved.
    - Test Plan: Fly to Cinnabar Island and enter the Pokémon Lab. Speak with all scientists, especially the fossil reviver. Show him HELIX. After exhausting interactions, fly back to Mt. Moon and check on the grunt.

# REFACTORING TEMPLATE (WIP)