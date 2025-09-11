# I. Core Principles & Lessons Learned
1.  **Immediate Maintenance:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
2.  **Proactive Automation & Refinement:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority. If an agent or tool is suboptimal, I must prioritize refining it immediately.
3.  **Trust, But Verify:** I must trust the outputs of my agents and system data. However, if a tool's output contradicts the Game State Information, my assumption must be that the tool is wrong, and I must debug it.
4.  **Abandon Failed Hypotheses:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.
5.  **CRITICAL - Data Verification & State Tracking:** My most severe failures stem from hallucinating game state variables (location, turn count, etc.). I MUST verify my current map ID, coordinates, and all other data from the Game State Information *before* every single action and trust it over my memory.
6.  **Confirmation Bias Warning (Mt. Moon Lesson):** I incorrectly assumed I was trapped in a map partition in Mt. Moon and that my pathfinding tool was faulty. I must trust the game state data and my tools over my own intuition, and actively try to disprove my assumptions. A "no path found" result is often a correct assessment of the map.
7.  **Exhaust All Options (Mt. Moon Hiker Lesson):** A Hiker at Mt. Moon 1F (6, 7) blocked a path and was unmovable. Instead of getting stuck, I explored an alternative path via a ladder at (26, 16), which proved to be the correct way forward. This reinforces the need to explore all reachable alternatives when a path seems blocked.

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
    - `warp tiles` (e.g., ladder_up, ladder_down, hole, teleport): Cause instant map transition. Often need to step off and back on to reuse.
    - `cuttable`: Tree that can be cut with HM Cut. Becomes `ground` after cutting, but respawns on map change or after battle.
    - `water`: Crossable using HM Surf.

# III. Current Quest: The Mt. Moon Fossil
- **Objective:** Find a fossil item to give to the Rocket Grunt at Mt. Moon B2F (30, 12).
- **Key Obstacle:** The path to the fossil is blocked by the Grunt, who states: "If you find a fossil, give it to me and scram!"
- **Current Status:** After exhausting all leads in the eastern part of Mt. Moon, I discovered a new western section. However, the high encounter rate and a paralyzed lead Pokémon have forced a tactical retreat to a Pokémon Center. The party is now healed and ready to return.
- **Failed Hypotheses Log:**
    1.  Giving the *revived* fossil Pokémon (HELIX) is sufficient. (Result: Failure)
    2.  The Super Nerd at B2F (13, 9) gives a fossil after being defeated. (Result: Failure, he only gives dialogue.)
    3.  The visible items at B2F (9, 9) and (5, 9) are fossils. (Result: Failure, they are non-interactive scenery.)
    4.  The Super Nerd provides a non-fossil key item. (Result: Failure, dialogue only.)

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
- Poison is not very effective against Poison (Observed: GOLBAT's SLUDGE vs ZUBAT).

# V. Battle Strategy & Tool Usage
- **Battle Automation Flow:** Use the consolidated `battle_automator` for routine wild battles and main menu navigation. For complex trainer battles, consult `comprehensive_battle_agent` for strategic advice.
- **Navigation:** Use `automated_path_navigator` for standard point-to-point travel. For multi-floor buildings with known warp connections, use `multi_floor_navigation_agent`. For high-level exploration planning in complex, unknown areas, use `navigation_strategist_agent`.

# VI. System & Tool Notes
- **Tool Deletion Anomaly:** The `delete_tool` command consistently fails for `select_battle_option` with a 'not found' error, despite the tool being listed as available. Deprecating in practice instead of attempting further deletion.
    5.  The Super Nerd at B2F (13, 9) has new dialogue after exploring the western cave sections. (Result: Failure, dialogue is unchanged.)
5. The Super Nerd at B2F (13, 9) has new dialogue after exploring the western cave sections. (Result: Failure, dialogue is unchanged.)