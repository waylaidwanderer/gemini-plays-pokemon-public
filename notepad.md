# I. Core Principles & Lessons Learned
1.  **Immediate Maintenance:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
2.  **Proactive Automation & Refinement:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority. If an agent or tool is suboptimal, I must prioritize refining it immediately.
3.  **Trust, But Verify:** I must trust the outputs of my agents and system data. However, if a tool's output contradicts the Game State Information, my assumption must be that the tool is wrong, and I must debug it. I fell victim to confirmation bias by ignoring the pathfinder's correct 'no path found' result in Mt. Moon, assuming it was a tool error instead of a map partition.
4.  **Abandon Failed Hypotheses:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.
5.  **CRITICAL - Data Verification & State Tracking:** My most severe failures stem from hallucinating game state variables (location, turn count, etc.). I MUST verify my current map ID, coordinates, and all other data from the Game State Information *before* every single action and trust it over my memory.

# II. Game Mechanics & World Data
## A. Tile Mechanics
- **ground, grass:** Standard traversable tiles.
- **impassable:** Walls, counters, etc. Cannot be entered.
- **elevated_ground:** Traversable, but can only be accessed from 'steps' tiles.
- **steps:** The only tile type that allows movement between 'ground' and 'elevated_ground'.
- **ledge:** One-way traversal. Can be jumped down, but not climbed up.
- **warp tiles (ladders, holes, etc.):** Cause instant map transition. Often need to step off and back on to reuse.
- **ladder_up, ladder_down:** Specific types of warp tiles leading between floors.
- **cuttable:** Tree that can be cut with HM Cut. Becomes 'ground' after cutting, but respawns on map change or after battle.
- **water:** Crossable using HM Surf.

## B. Gameplay Mechanics
- **Trap Battles:** Certain wild encounters appear to be 'trap' battles where the 'RUN' option is disabled (Observed: Wigglytuff, KADABRA; Suspected: Ditto).
- **Fossil Regeneration:** The Cinnabar Lab has a machine to regenerate fossils.

# III. Key Puzzles & Events
- **Mt. Moon Fossil Grunt:** A Rocket Grunt at (30,12) on B2F blocks a path and requires a fossil to pass.
    - **Hypothesis 1 (Failed):** Having the revived fossil Pokémon (HELIX) in the PC is sufficient. (Result: Grunt did not react).
    - **Hypothesis 2 (Failed):** The revived fossil Pokémon (HELIX) must be the sole member of the active party. (Result: Grunt's dialogue was unchanged. He still wants a 'fossil' item, not the revived Pokémon.)
    - **Hypothesis 3 (Confirmed):** The actual 'Helix Fossil' or 'Dome Fossil' item is required, not the revived Pokémon. (Confirmed by Cinnabar Lab Scientist).
    - **Hypothesis 4:** A story flag must be triggered at the Cinnabar Island Pokémon Lab.
    - **Hypothesis 5 (Confirmed):** The Grunt's dialogue is "If you find a fossil, give it to me and scram!". This confirms he is the obstacle and the fossil item is the key.

# IV. Pokémon Data
## A. Wild Pokémon Locations & Movesets
- **Cerulean Cave:** WIGGLYTUFF (Lv 62 - LOVELY KISS, DOUBLE-EDGE, REST), SANDSLASH (Lv 63 - SWORDS DANCE, EARTHQUAKE), GOLEM (Lv 64 - EXPLOSION), LICKITUNG (Lv 61 - WRAP), CHANSEY (Lv 63 - DEFENSE CURL, MEGA PUNCH), RAICHU (Lv 64 - AGILITY).

## B. Notable Trainer Rosters
- **Sabrina (Saffron Gym):** MR. MIME (Lv 65 - PSYCHIC), HYPNO (Lv 64 - PSYWAVE), SLOWBRO (Lv 64 - PSYCHIC), JYNX (Lv 64 - BLIZZARD, BUBBLEBEAM, DREAM EATER, LOVELY KISS), GENGAR (Lv 64 - NIGHT SHADE, PSYCHIC), ALAKAZAM (Lv 65 - THUNDER WAVE, PSYCHIC).
- **SMITH (Cerulean Cave):** AERODACTYL (Lv 65 - HYPER BEAM, ROCK SLIDE).
- **Brock (Pewter Gym):** OMASTAR (Lv 64 - HYDRO PUMP, BLIZZARD), ONIX (Lv 65 - EARTHQUAKE, ROCK SLIDE), KABUTOPS (Lv 64 - SWORDS DANCE, SLASH), GOLEM (Lv 64 - ROCK SLIDE), NINETALES (Lv 64 - REFLECT), AERODACTYL (Lv 65 - FLY).

## C. Type Effectiveness Chart
- Water is super-effective against Rock/Ground (Observed: OMANYTE's SURF vs GEODUDE).

# V. Battle Strategy & Tool Usage
- **Battle Automation Flow:**
  1.  **Main Menu:** Use `select_battle_option` to choose FIGHT, PKMN, ITEM, or RUN.
  2.  **Move/PKMN Selection:** Use `menu_analyzer` to parse the screen, then `select_menu_option` to make a selection.
  3.  **Fallback:** If the above toolchain fails, call `comprehensive_battle_agent` for turn-by-turn advice.
  4.  **Last Resort:** Manual button presses should only be used if all automated systems and agents fail.
- For complex navigation puzzles (like partitioned caves), use the `navigation_strategist_agent` to devise a high-level plan.
- Water is not very effective against Bug/Grass (Observed: OMANYTE's BUBBLEBEAM vs PARAS).

# Mt. Moon 1F Hiker Puzzle
- **Hypothesis 1 (Failed):** Talking to the Hiker at (6, 7) will make him move or initiate a battle. (Attempt #2: Dialogue was 'Kids like you shouldn't be here!', no battle, no movement.)
- **New Hypothesis:** The ladder at (26, 16), previously thought to be a 'trap', is the intended path to the western partition of the cave.
6.  **Confirmation Bias Warning:** I incorrectly assumed I was trapped in a map partition in Mt. Moon and that my pathfinding tool was faulty. I must trust the game state data and my tools over my own intuition, and actively try to disprove my assumptions.

# VI. Tool Development & Maintenance
- **`battle_sequence_automator`:** This tool has failed repeatedly due to multiple bugs (incorrect status move list, nickname vs. species matching, contaminated JSON output from debug prints, KeyError). It requires a full teardown and rebuild outside of active battle. Do not attempt to use it again until it has been properly fixed.