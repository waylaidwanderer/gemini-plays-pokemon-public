# I. Core Principles & Lessons Learned
1.  **Immediate Maintenance:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified, regardless of game state (including during battle).
2.  **Proactive Automation & Refinement:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority. If an agent or tool is suboptimal, I must prioritize refining it immediately.
3.  **Trust, But Verify:** I must trust the outputs of my agents and system data. However, if a tool's output contradicts the Game State Information, my assumption must be that the tool is wrong, and I must debug it.
4.  **Confirmation Bias Warning (Route 2 Lesson):** I incorrectly assumed the Route 2 Gatehouse was a viable shortcut. I must trust my pathfinding tool's 'no path found' results and investigate the reason for the failure rather than assuming the tool is wrong.
5.  **Exhaust All Options (Mt. Moon Hiker Lesson):** A Hiker at Mt. Moon 1F (6, 7) blocked a path. Instead of getting stuck, I explored an alternative path via a ladder at (26, 16), which was the correct way forward. This reinforces the need to explore all reachable alternatives when a path seems blocked.
6.  **Warp Discipline:** After every warp, my first action must be to check and, if necessary, create/update markers on **both** the departure and arrival maps.

# II. Game Mechanics & World Data
- **Gameplay Mechanics:**
    - **Trap Battles:** Certain wild encounters appear to be 'trap' battles where the 'RUN' option is disabled (Observed: Wigglytuff, KADABRA; Suspected: Ditto).
    - **Fossil Regeneration:** The Cinnabar Lab has a machine to regenerate fossils.
- **Tile Mechanics:**
    - `ground`, `grass`: Standard traversable tiles.
    - `impassable`: Walls, counters, etc. Cannot be entered.
    - `elevated_ground`: Traversable, but can only be accessed from 'steps' tiles.
    - `steps`: The only tile type that allows movement between 'ground' and 'elevated_ground'.
    - `ledge`: One-way traversal. Can be jumped down, but not climbed up.
    - `warp tiles` (e.g., ladder_up, ladder_down, hole, teleport): Cause instant map transition. Often need to step off and back on to reuse. `ladder_up` specifically takes you to a higher floor.
    - `cuttable`: Tree that can be cut with HM Cut. Becomes `ground` after cutting, but respawns on map change or after battle.
    - `water`: Crossable using HM Surf.

# III. Current Quest: The Mt. Moon Fossil
- **Objective:** Find a fossil item to give to the Rocket Grunt at Mt. Moon B2F (30, 12).
- **Current Plan:** Retrieve the ITEMFINDER from the PC and return to Mt. Moon to search for a hidden fossil.
- **Failed Hypotheses Log:**
    1.  Giving the *revived* fossil Pokémon (HELIX) is sufficient. (Result: Failure)
    2.  The Super Nerd at B2F (13, 9) gives a fossil after being defeated. (Result: Failure)
    3.  The visible items at B2F (9, 9) and (5, 9) are fossils. (Result: Failure, non-interactive scenery.)
    4.  The Super Nerd provides a non-fossil key item. (Result: Failure, dialogue only.)
    5.  The Rocket Grunt will accept a fainted Omanyte. (Result: Failure, could not get Omanyte to faint.)
    6.  Using a MOON STONE from the inventory has an effect. (Result: Failure, opens Pokémon menu.)
    7.  The Cinnabar Lab can 'de-revive' a Pokémon back into a fossil. (Result: Failure, scientist only revives fossils.)
    8.  A Pokémon nicknamed 'FOSSIL' will satisfy the Grunt. (Result: Failure, dialogue unchanged.)

# IV. Pokémon & Battle Data
## A. Type Effectiveness Chart (Verified)
- Water is super-effective against Rock/Ground (Observed: OMANYTE's SURF vs GEODUDE).
- Water is not very effective against Bug/Grass (Observed: OMANYTE's BUBBLEBEAM vs PARAS).
- Poison is not very effective against Poison/Flying (Confirmed: ECHO's SLUDGE vs ZUBAT) and Rock/Ground (Observed: ECHO's SLUDGE vs GEODUDE).
- Flying is not very effective against Rock/Ground (Observed: ECHO's FLY vs GEODUDE).

## B. Notable Trainer Rosters
- **Sabrina (Saffron Gym):** MR. MIME (Lv 65 - PSYCHIC), HYPNO (Lv 64 - PSYWAVE), SLOWBRO (Lv 64 - PSYCHIC), JYNX (Lv 64 - BLIZZARD, BUBBLEBEAM, DREAM EATER, LOVELY KISS), GENGAR (Lv 64 - NIGHT SHADE, PSYCHIC), ALAKAZAM (Lv 65 - THUNDER WAVE, PSYCHIC).
- **SMITH (Cerulean Cave):** AERODACTYL (Lv 65 - HYPER BEAM, ROCK SLIDE).
- **Brock (Pewter Gym):** OMASTAR (Lv 64 - HYDRO PUMP, BLIZZARD), ONIX (Lv 65 - EARTHQUAKE, ROCK SLIDE), KABUTOPS (Lv 64 - SWORDS DANCE, SLASH), GOLEM (Lv 64 - ROCK SLIDE), NINETALES (Lv 64 - REFLECT), AERODACTYL (Lv 65 - FLY).

## C. Wild Pokémon Locations
- **Cerulean Cave:** WIGGLYTUFF (Lv 62 - LOVELY KISS, DOUBLE-EDGE, REST), SANDSLASH (Lv 63 - SWORDS DANCE, EARTHQUAKE), GOLEM (Lv 64 - EXPLOSION), LICKITUNG (Lv 61 - WRAP), CHANSEY (Lv 63 - DEFENSE CURL, MEGA PUNCH), RAICHU (Lv 64 - AGILITY).

# V. System & Tool Notes
- **Tool Deletion Anomaly:** The `delete_tool` command consistently fails for `select_battle_option` with a 'not found' error, despite the tool being listed as available. Deprecating in practice instead of attempting further deletion.
- **PP Management for Stalling:** When planning to stall in a battle (e.g., to faint a Pokémon intentionally), always check the PP of non-damaging moves beforehand. Running out of PP can force an attack and ruin the strategy.
- **Battle Menu Anomaly (Inconclusive):** A test suggested the move selection menu resets if confirmation is delayed, but a second identical test contradicted this. The exact mechanic is unknown and requires further investigation. All battle automation must now combine directional inputs and the 'A' press into a single turn's action.
- **Master Navigator Agent Lesson:** For complex, multi-floor navigation puzzles like Mt. Moon, I should use the `master_navigator_agent` instead of relying on manual pathfinding and the simpler `automated_path_navigator`. This will be more efficient and less prone to error.
- **Future Tool Improvement:** Upgrade `battle_automator` to incorporate type effectiveness logic for move selection, making it a more intelligent combat tool.
7.  **Mandatory Self-Assessment:** Periodically, I must perform a structured self-review to ensure my strategies, documentation, and tool usage remain optimal and aligned with my core principles. This prevents strategic drift and corrects bad habits before they become ingrained.