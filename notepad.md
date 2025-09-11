# I. Core Principles & Lessons Learned
1.  **Immediate Maintenance:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
2.  **Proactive Automation & Refinement:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority. If an agent or tool is suboptimal, I must prioritize refining it immediately.
3.  **Trust, But Verify:** I must trust the outputs of my agents and system data. However, if a tool's output contradicts the Game State Information, my assumption must be that the tool is wrong, and I must debug it.
4.  **Abandon Failed Hypotheses:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.
5.  **CRITICAL - Data Verification & State Tracking:** My most severe failures stem from hallucinating game state variables (location, turn count, etc.). I MUST verify my current map ID, coordinates, and all other data from the Game State Information *before* every single action and trust it over my memory.
6.  **Confirmation Bias Warning (Mt. Moon Lesson):** I incorrectly assumed I was trapped in a map partition in Mt. Moon and that my pathfinding tool was faulty. I must trust the game state data and my tools over my own intuition, and actively try to disprove my assumptions. A "no path found" result is often a correct assessment of the map.
7.  **Exhaust All Options (Mt. Moon Hiker Lesson):** A Hiker at Mt. Moon 1F (6, 7) blocked a path and was unmovable. Instead of getting stuck, I explored an alternative path via a ladder at (26, 16), which proved to be the correct way forward. This reinforces the need to explore all reachable alternatives when a path seems blocked.

# II. Game Mechanics & World Data
- **Tile Mechanics:**
    - `ground`, `grass`: Standard traversable tiles.
    - `impassable`: Walls, counters, etc. Cannot be entered.
    - `elevated_ground`: Traversable, but can only be accessed from 'steps' tiles.
    - `steps`: The only tile type that allows movement between 'ground' and 'elevated_ground'.
    - `ledge`: One-way traversal. Can be jumped down, but not climbed up.
    - `warp tiles` (e.g., ladder_up, ladder_down, hole, teleport): Cause instant map transition. Often need to step off and back on to reuse.
    - `cuttable`: Tree that can be cut with HM Cut. Becomes `ground` after cutting, but respawns on map change or after battle.
    - `water`: Crossable using HM Surf.
- **Gameplay Mechanics:**
    - **Trap Battles:** Certain wild encounters appear to be 'trap' battles where the 'RUN' option is disabled (Observed: Wigglytuff, KADABRA; Suspected: Ditto).
    - **Fossil Regeneration:** The Cinnabar Lab has a machine to regenerate fossils.

# III. Key Puzzles & Events
- **Mt. Moon Fossil Grunt:** A Rocket Grunt at (30,12) on B2F blocks a path. Requires a fossil item to pass.
    - **Dialogue:** "If you find a fossil, give it to me and scram!"
    - **Hypothesis 1 (Failed):** Giving the *revived* fossil Pokémon (HELIX) is sufficient.
        - Test 1: HELIX in PC. Result: Failure.
        - Test 2: HELIX as sole party member. Result: Failure.
    - **Hypothesis 2 (Confirmed):** An actual 'Helix Fossil' or 'Dome Fossil' *item* is required. (Confirmed by Cinnabar Lab Scientist dialogue).

# IV. Pokémon Data
## A. Wild Pokémon Locations & Movesets
- **Cerulean Cave:** WIGGLYTUFF (Lv 62 - LOVELY KISS, DOUBLE-EDGE, REST), SANDSLASH (Lv 63 - SWORDS DANCE, EARTHQUAKE), GOLEM (Lv 64 - EXPLOSION), LICKITUNG (Lv 61 - WRAP), CHANSEY (Lv 63 - DEFENSE CURL, MEGA PUNCH), RAICHU (Lv 64 - AGILITY).

## B. Notable Trainer Rosters
- **Sabrina (Saffron Gym):** MR. MIME (Lv 65 - PSYCHIC), HYPNO (Lv 64 - PSYWAVE), SLOWBRO (Lv 64 - PSYCHIC), JYNX (Lv 64 - BLIZZARD, BUBBLEBEAM, DREAM EATER, LOVELY KISS), GENGAR (Lv 64 - NIGHT SHADE, PSYCHIC), ALAKAZAM (Lv 65 - THUNDER WAVE, PSYCHIC).
- **SMITH (Cerulean Cave):** AERODACTYL (Lv 65 - HYPER BEAM, ROCK SLIDE).
- **Brock (Pewter Gym):** OMASTAR (Lv 64 - HYDRO PUMP, BLIZZARD), ONIX (Lv 65 - EARTHQUAKE, ROCK SLIDE), KABUTOPS (Lv 64 - SWORDS DANCE, SLASH), GOLEM (Lv 64 - ROCK SLIDE), NINETALES (Lv 64 - REFLECT), AERODACTYL (Lv 65 - FLY).

## C. Type Effectiveness Chart
- Water is super-effective against Rock/Ground (Observed: OMANYTE's SURF vs GEODUDE).
- Water is not very effective against Bug/Grass (Observed: OMANYTE's BUBBLEBEAM vs PARAS).

# V. Battle Strategy & Tool Usage
- **Battle Automation Flow:** Use `battle_sequence_automator` for routine wild battles to select the best damaging move. Note: This tool only outputs directional presses; the final 'A' confirmation is manual. For trainer battles, use `comprehensive_battle_agent` for strategic advice.
- **Navigation:** Use `automated_path_navigator` for standard point-to-point travel. For complex exploration or puzzles, use `navigation_strategist_agent`.

# VI. Tool Development & Maintenance
- **`battle_sequence_automator`:** This tool has a history of failures but has been significantly improved. Recent fixes include adding menu state detection (to distinguish the main battle menu from the move menu) and correcting the logic for matching a Pokémon's nickname. It should be tested further in low-stakes battles.

# VII. Current Mt. Moon Puzzle State
- **Objective:** Find a fossil item to give to the Rocket Grunt at B2F (30, 12).
- **Summary of Exploration:** All previously known paths on 1F, B1F, and B2F have been fully explored and lead to dead ends or the fossil-blocking Grunt. No fossil has been found.
- **Hypothesis (Denied):** The Super Nerd at (13, 9) on B2F will give the player a choice of fossil after being defeated.
    - **Test:** Spoke to the Super Nerd after defeating him.
    - **Result:** He only provided dialogue about the Cinnabar Lab. No fossil was given.
- **Hypothesis (Denied):** The visible item at (9, 9) is a fossil.
    - **Hypothesis (Denied):** The visible item at (9, 9) is a fossil.
    - **Test:** Navigated to (10, 9), adjacent to the item. Attempted to interact twice.
    - **Result:** Failure. The item is non-interactive background scenery.
- **Hypothesis (Denied):** The second visible item at (5, 9) is the fossil.
    - **Test:** Navigated to (5, 9) and (6, 9), adjacent to the item. Attempted to interact twice.
    - **Result:** Failure. The item is non-interactive background scenery.
- **Current State:** All exploration paths and hypotheses within Mt. Moon have been exhausted. I am currently stuck.
- **Next Step:** Analyze new hypotheses from the `puzzle_solver_agent`.

# VIII. Current Mt. Moon Puzzle - New Hypotheses (from Agent)
1.  **Hypothesis: Defeating the Super Nerd at B2F (13, 9) is a prerequisite that makes the previously unobtainable items at (9, 9) and (5, 9) collectible as fossils.**
    -   *Test Plan:* Re-confirm Super Nerd is defeated, then immediately interact with the items at (9, 9) and (5, 9).
    -   *Reasoning:* Classic RPG sequential trigger. The actions might need to be performed in a specific order.
    -   **Result (Item at 9, 9):** Failure. After confirming the Super Nerd's post-battle dialogue, interacting with the item at (9, 9) from the adjacent tile (10, 9) yielded no result. The item is non-interactive.
2.  **Hypothesis: A hidden switch or interactive object exists in the immediate vicinity of the Super Nerd and the two visible items.**
    -   *Test Plan:* Systematically press the action button on all adjacent walls and objects around (13, 9), (9, 9), and (5, 9).
    -   *Reasoning:* A new path might need to be created via a hidden environmental trigger.
3.  **Hypothesis: The Super Nerd's dialogue about Cinnabar is a misdirection, and he provides a different, non-fossil key item that will satisfy the Rocket Grunt.**
    -   *Test Plan:* After interacting with the Super Nerd, check the Key Items pocket for any new items and present them to the Grunt.
    -   *Reasoning:* Subverts the stated goal; the true objective is to pass the Grunt, not necessarily with a fossil.