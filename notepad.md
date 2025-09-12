# I. Core Principles & Lessons Learned
1.  **Immediate Maintenance:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified, regardless of game state.
2.  **Proactive Automation & Refinement:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority. If an agent or tool is suboptimal, I must prioritize refining it immediately.
3.  **Trust, But Verify:** I must trust the outputs of my agents and system data. However, if a tool's output contradicts the Game State Information, my assumption must be that the tool is wrong, and I must debug it.
4.  **Confirmation Bias Warning (Route 2 Lesson):** I incorrectly assumed the Route 2 Gatehouse was a viable shortcut. I must trust my pathfinding tool's 'no path found' results and investigate the reason for the failure rather than assuming the tool is wrong.
5.  **Exhaust All Options (Mt. Moon Hiker Lesson):** A Hiker at Mt. Moon 1F (6, 7) blocked a path. Instead of getting stuck, I explored an alternative path via a ladder at (26, 16), which was the correct way forward. This reinforces the need to explore all reachable alternatives when a path seems blocked.
6.  **Warp Discipline:** After every warp, my first action must be to check and, if necessary, create/update markers on **both** the departure and arrival maps.
7.  **Mandatory Self-Assessment:** Periodically, I must perform a structured self-review to ensure my strategies, documentation, and tool usage remain optimal and aligned with my core principles.
8.  **Map Partition Awareness (Mt. Moon B1F Lesson):** I hallucinated reachable warps by failing to recognize the map was partitioned into disconnected areas. I must always verify path connectivity between my current position and any target, not just assume all tiles on a map are connected.
9.  **Efficiency Over Fixation (Wild Battle Lesson):** If a simple automation tool fails during a low-stakes, repetitive task (like a wild battle), it is more efficient to complete the task manually and fix the tool later, rather than getting stuck debugging mid-task. High-level strategic agents can provide a better alternative than faulty simple automation.

# II. Game Mechanics & World Data
- **Gameplay Mechanics:**
    - **Trap Battles:** Certain wild encounters appear to be 'trap' battles where the 'RUN' option is disabled (Observed: Wigglytuff, KADABRA; Suspected: Ditto).
    - **Fossil Regeneration:** The Cinnabar Lab has a machine to regenerate fossils.
- **Tile Mechanics Glossary:**
    - **ground**: Standard walkable tile.
    - **impassable**: Walls, rocks, cannot be entered.
    - **elevated_ground**: Walkable ground at a different height, requires 'steps' to access.
    - **steps**: Allows movement between 'ground' and 'elevated_ground'.
    - **ladder_up / ladder_down**: Warps between floors.
    - **cuttable**: Tree that can be cut with HM Cut.
    - **ledge**: Can be jumped down, but not climbed up.
    - **grass**: Tall grass for wild Pokémon encounters.
    - **water**: Crossable using HM Surf.

# III. Current Quest: The Mt. Moon Fossil
- **Objective:** Find a fossil item to give to the Rocket Grunt at Mt. Moon B2F (30, 12).
- **Current Plan:** Test new hypotheses from the puzzle_solver_agent, starting with having a thematic Pokémon (HELIX) lead the party when talking to the Rocket Grunt.
- **New Hypotheses (from Agent):**
    1. A Pokémon with the Pickup ability can find the fossil.
    2. The Hiker at 1F (6, 7) moves after a different trigger (already tested post-Super Nerd, but keeping in mind).
    3. An interactable rock formation somewhere in Mt. Moon gives the fossil.
    4. Using the move 'Dig' on a specific tile unearths the fossil.
    5. A thematically related Pokémon (e.g., Cubone, Geodude, Omanyte) in the party's lead slot triggers new dialogue.
- **Failed Hypotheses Log:**
    1.  Giving the *revived* fossil Pokémon (HELIX) is sufficient. (Result: Failure)
    2.  The Super Nerd at B2F (13, 9) gives a fossil after being defeated. (Result: Failure)
    3.  The visible items at B2F (9, 9) and (5, 9) are fossils. (Result: Failure, non-interactive scenery.)
    4.  The Super Nerd provides a non-fossil key item. (Result: Failure, dialogue only.)
    5.  The Rocket Grunt will accept a fainted Omanyte. (Result: Failure, could not get Omanyte to faint.)
    6.  Using a MOON STONE from the inventory has an effect. (Result: Failure, opens Pokémon menu.)
    7.  The Cinnabar Lab can 'de-revive' a Pokémon back into a fossil. (Result: Failure, scientist only revives fossils.)
    8.  A Pokémon nicknamed 'FOSSIL' will satisfy the Grunt. (Result: Failure, dialogue unchanged.)
    9. The fossil is a hidden item on Mt. Moon B2F. (Result: Failure, ITEMFINDER search yielded only an ETHER).
    10. The Super Nerd's dialogue might change if spoken to with a revived fossil Pokémon (HELIX the Omanyte) in the party. (Result: Failure, dialogue unchanged).
    11. The Hiker at 1F (6, 7) is passable like some NPCs in Rock Tunnel. (Result: Failure, movement was blocked).

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
- **Battle Menu Anomaly (Confirmed):** The system's tool execution pipeline is unreliable when a tool's output combines directional inputs (Up/Down/Left/Right) with an action button ('A') in a single turn. This was observed during a battle where the `battle_automator` failed to execute `['Down', 'Down', 'A']` but manual, separate inputs of `['Down', 'Down']` and then `['A']` worked. All future automation must account for this by separating directional movements from action confirmations into separate turns.
- **Master Navigator Agent Lesson:** For complex, multi-floor, partitioned navigation puzzles like Mt. Moon, I should use the `master_navigator_agent` instead of relying on manual pathfinding and the simpler `automated_path_navigator` to avoid hallucinations.
- **Leverage Strategic Agents:** When simple automation tools fail or become inefficient (e.g., `battle_automator` in a complex fight), I should pivot to using high-level strategic agents like `comprehensive_battle_agent` for advice, then execute the recommended actions manually.