# I. Core Principles & Lessons Learned
1.  **Immediate Maintenance:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified, regardless of game state (including during battle).
2.  **Proactive Automation & Refinement:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority. If an agent or tool is suboptimal, I must prioritize refining it immediately.
3.  **Trust, But Verify:** I must trust the outputs of my agents and system data. However, if a tool's output contradicts the Game State Information, my assumption must be that the tool is wrong, and I must debug it.
4.  **Confirmation Bias Warning (Route 2 Lesson):** I incorrectly assumed the Route 2 Gatehouse was a viable shortcut. I must trust my pathfinding tool's 'no path found' results and investigate the reason for the failure rather than assuming the tool is wrong.
5.  **Exhaust All Options (Mt. Moon Hiker Lesson):** A Hiker at Mt. Moon 1F (6, 7) blocked a path. Instead of getting stuck, I explored an alternative path via a ladder at (26, 16), which was the correct way forward. This reinforces the need to explore all reachable alternatives when a path seems blocked.
6. **Warp Discipline:** After every warp, my first action must be to check and, if necessary, create/update markers on **both** the departure and arrival maps.

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
- **Objective:** Find a way to get past the Rocket Grunt at Mt. Moon B2F (30, 12).
- **Current Plan:** Pursuing the top hypothesis from `puzzle_solver_agent`: travel to Cinnabar Island to attempt to 'de-revive' HELIX into a fossil item at the Pokémon Lab.
- **Current Roadblock:** Path on Route 2 is blocked by a `cuttable` tree. I must backtrack to Pewter City PC to get a Pokémon that can learn Cut.
- **Failed Hypotheses Log:**
    1.  Giving the *revived* fossil Pokémon (HELIX) is sufficient. (Result: Failure)
    2.  The Super Nerd at B2F (13, 9) gives a fossil after being defeated. (Result: Failure)
    3.  The visible items at B2F (9, 9) and (5, 9) are fossils. (Result: Failure, non-interactive scenery.)
    4.  The Super Nerd provides a non-fossil key item. (Result: Failure, dialogue only.)
    5.  The Rocket Grunt will accept a fainted Omanyte. (Result: Failure, could not get Omanyte to faint.)
    6.  Using a MOON STONE from the inventory has an effect. (Result: Failure, opens Pokémon menu.)
- **Untested Assumptions Log:**
    1.  **Assumption:** The Cinnabar Lab can 'de-revive' a Pokémon.
    2.  **Assumption:** A Pokémon in my PC can learn Cut.

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
- Flying is not very effective against Rock/Ground (Observed: ECHO's FLY vs GEODUDE).

# V. Battle Strategy & Tool Usage
- **Battle Automation Flow:** Use the consolidated `battle_automator` for all in-battle menu navigation. For complex trainer battles, consult `comprehensive_battle_agent` for high-level strategic advice.
- **Navigation:** Use `automated_path_navigator` for standard point-to-point travel. For complex navigation involving multiple floors or unknown layouts, use `master_navigator_agent`.

# VI. System & Tool Notes
- **Tool Deletion Anomaly:** The `delete_tool` command consistently fails for `select_battle_option` with a 'not found' error, despite the tool being listed as available. Deprecating in practice instead of attempting further deletion.
- **PP Management for Stalling:** When planning to stall in a battle (e.g., to faint a Pokémon intentionally), always check the PP of non-damaging moves beforehand. Running out of PP can force an attack and ruin the strategy.
- **Tool Refinement Needed (`battle_automator`):** The current zero-PP check is a temporary fix. A more robust solution is needed, such as parsing PP from the screen or creating an internal model of move states.
- **Tool Refinement Needed (`automated_path_navigator`):** The tool must be enhanced to provide specific reasons for pathing failures (e.g., 'blocked by NPC', 'unreachable partition') to improve diagnostics.

# VII. Confirmed Mechanics & Resolved Experiments
- **Battle Menu Anomaly (Inconclusive):** A test suggested the move selection menu resets if confirmation is delayed, but a second identical test contradicted this. The exact mechanic is unknown and requires further investigation.
  - **Test 1 (vs Sandshrew):** Selected SLUDGE, delayed confirmation -> FLY was used.
  - **Test 2 (vs Geodude):** Selected SLUDGE, delayed confirmation -> SLUDGE was used.
  - **Conclusion:** Hypothesis of a simple reset is **disproven**. The trigger for this behavior is unknown. All battle automation must now combine directional inputs and the 'A' press into a single turn's action.

# VIII. Future Plans & System Development Ideas
- **New Agent/Tool Idea:** Create a 'Team Composition Advisor' to suggest optimal parties for specific areas or gyms, based on known wild/trainer Pokémon.
- **New Agent/Tool Idea:** Create a 'Battle Staller Agent' that can take a battle objective (e.g., 'survive X turns', 'get Pokémon Y to faint') and output an optimal sequence of non-damaging or strategic moves.
- **New Agent/Tool Idea:** An agent to analyze discrepancies between intended actions and battle outcomes to hypothesize hidden mechanics.
- **NPC Re-check:** After resolving the Mt. Moon fossil quest, re-interact with the Hiker at Mt. Moon 1F (6, 7) to see if he has moved.