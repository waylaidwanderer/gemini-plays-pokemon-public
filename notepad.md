# I. Core Principles & Meta-Strategy
1.  **Immediate Maintenance:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
2.  **Proactive Automation:** Before any complex or repetitive task, consider automating it. If a tool is suboptimal, refine it immediately.
3.  **Trust, But Verify:** Trust agent/system outputs. If a tool contradicts game state, the tool is wrong and must be debugged.
4.  **Hypothesis-Driven Exploration:** All exploration must be guided by a clear, documented hypothesis. Systematically test one variable at a time.
5.  **Confirmation Bias Awareness:** If a hypothesis repeatedly fails, pivot to a new one. Use the `puzzle_solver_agent` to generate new lines of reasoning when stuck.

# II. Quest Log
- **Current Quest: The Mt. Moon Fossil**
    - **Objective:** Find a fossil to give to the Rocket Grunt blocking the path at Mt. Moon B2F (30,12), or find a way past the Hiker at 1F (6,7).
    - **Status:** Active. Currently pursuing an agent-generated hypothesis that requires visiting the 'Old Man' in Viridian City.
- **Stalled Quest: The Copycat's Gift**
    - **Objective:** Obtain a POKé DOLL and give it to COPYCAT.
    - **Status:** Stalled. All leads in Cerulean City have been exhausted. Suspect COPYCAT is not in a currently accessible area.

# III. Battle Intelligence
- **Type Effectiveness Chart (Verified):**
    - Water > Rock/Ground
    - Water is not very effective against Bug/Grass, Ghost/Poison
    - Poison is not very effective against Poison/Flying, Rock/Ground
    - Flying is not very effective against Rock/Ground
- **Notable Trainer Rosters:**
    - **Sabrina (Saffron Gym):** MR. MIME (Lv 65), HYPNO (Lv 64), SLOWBRO (Lv 64), JYNX (Lv 64), GENGAR (Lv 64), ALAKAZAM (Lv 65).
    - **SMITH (Cerulean Cave):** AERODACTYL (Lv 65).
    - **Brock (Pewter Gym):** OMASTAR (Lv 64), ONIX (Lv 65), KABUTOPS (Lv 64), GOLEM (Lv 64), NINETALES (Lv 64), AERODACTYL (Lv 65).
- **Wild Pokémon Locations:**
    - **Cerulean Cave:** WIGGLYTUFF (Lv 62), SANDSLASH (Lv 63), GOLEM (Lv 64), LICKITUNG (Lv 61), CHANSEY (Lv 63), RAICHU (Lv 64).

# IV. Fossil Quest - Hypotheses Log
- **Active Hypotheses (Ranked by Agent):**
    1.  **POKé DOLL as Fossil:** The Rocket Grunt on B2F will accept the POKé DOLL as the 'fossil'.
    2.  **POKé DOLL and the Hiker:** Getting rid of the POKé DOLL (by giving it to the Grunt) will make the Hiker on 1F move because the player is no longer a 'kid' with a toy.
    3.  **Fainted Fossil:** The Grunt wants a revived fossil Pokémon that has fainted.
    4.  **No Starter in Party:** The Hiker will move if the player's starter Pokémon is in the PC.
    5.  **Silph Scope Ghost:** The Silph Scope will reveal a ghost in Mt. Moon that needs to be captured and shown to the Grunt.
- **Failed Hypotheses:**
    - The Hiker will only move for an 'adult', a status temporarily gained by interacting with the 'Old Man' in Viridian City. (Result: Failed. Hiker's dialogue was unchanged.)
    - The fossil is in an interactable rock.
    - The Hiker on 1F at (6,7) will move if shown the revived HELIX fossil Pokémon.
    - The scientist in the Cinnabar Lab Fossil Room can 'un-revive' a fossil Pokémon.
    - Presenting the revived HELIX fossil Pokémon to the Rocket Grunt on B2F will trigger a new event.
    - The 'fossil' the Rocket Grunt wants is the MOON STONE.
    - A specific, non-fossil Pokémon from Mt. Moon (e.g., Geodude) will satisfy the Grunt.
    - The Hiker on Mt. Moon 1F at (6,7) is part of a chained quest.
    - The 'fossil' the Grunt wants must be stolen from the Pewter City Museum of Science.
    - The move 'Dig' must be used on a specific, unmarked tile within Mt. Moon to unearth the other fossil.
    - The Rocket Grunt will accept a Pokémon nicknamed 'fossil'.
    - The Hiker on Mt. Moon 1F at (6,7) will trade you for your revived fossil Pokémon.
    - A ladder's destination can be changed by entering and exiting it multiple times.
    - There is a hidden, one-way passage concealed in the western wall on 1F.
    - The Escape Rope item functions differently within Mt. Moon.
    - A rock is a disguised ladder that requires a Clefairy in the party.
    - The Hiker is thirsty and needs a drink item.
    - An un-revived fossil can be acquired by fishing inside Mt. Moon.
    - The Rocket Grunt will accept a thematically 'fossil' Pokémon like Marowak.
    - The Pokémon Tower is a red herring for the fossil quest.

# V. Game & World Mechanics
- **Battle Menu Anomaly:** The game appears to intentionally restrict move selection in certain wild battles to the first move slot. Strategy: For low-stakes wild battles, running is the most efficient option.
- **Party Menu 'SWITCH' Lock:** The game appears to intentionally prevent the use of the 'SWITCH' command in the party menu under certain, currently unknown, conditions. This was observed after multiple failed escape attempts in Mt. Moon.
- **Pokemon Tower 6F Healer Change:** The friendly Channeler at (13,11) is no longer a healer. Her dialogue has changed to 'I feel anemic and weak...'.
- **POKé DOLL Escape:** A POKé DOLL can be used to guarantee an escape from a wild Pokémon battle.
- **Shop Menu Navigation Anomaly:** The shop menu in the Cerulean Mart does not follow a standard grid layout. Manual testing showed 'Down' moves from 'BUY' to 'SELL', but 'Right' does nothing from either position. The menu must be exited with the 'B' button.
- **Unreliable Automation:** The `use_field_move` tool's single-sequence design was unreliable. It has been refactored into a multi-stage process for improved stability.

# VI. Tile Mechanics
- **ground / grass:** Standard walkable tiles.
- **impassable:** Walls, counters, and other solid objects. Cannot be entered.
- **ledge:** Can only be jumped down (from Y-1 to Y+2 in one move). Acts as a wall from all other directions.
- **steps:** The only way to transition between `ground` and `elevated_ground`.
- **elevated_ground:** Walkable, but at a different height. Cannot be accessed directly from `ground`.
- **cuttable:** A tree that can be cut with HM Cut. Becomes `ground` but respawns on map change.
- **water:** Requires HM Surf to cross.
- **Warp Tiles (ladders, doors, etc.):** Tiles that transport the player to another map or location.
- **Impassable Decorative Grass:** The small grass patches inside the Celadon Department Store are purely decorative and act as impassable walls.
- **trashcan:** Found in Cerulean Badge House at (8,8). Properties unknown, likely impassable. (Hypothesis: Test interaction upon next visit.)

# VII. Self-Assessment Log
- **(Turn 213727):** Performed self-assessment. Identified failure to immediately fix tools (`general_menu_navigator`). Acknowledged underutilization of `master_navigator_agent` and confirmation bias regarding menu layouts. Updated notepad with new hypotheses and automation ideas.
- **(Turn 213778):** Performed self-assessment. Acknowledged inefficient debugging methods (guessing instead of data-gathering) and failure to use agents when stuck. Re-committed to a more scientific approach to problem-solving. Pivoted goals due to stalled quest.

# VIII. Defined Agents & Tools
- **Agents:**
    - `puzzle_solver_agent`: Analyzes a complex puzzle to generate new hypotheses.
    - `comprehensive_battle_agent`: Provides pre-battle and in-battle strategic advice.
    - `battle_anomaly_detector_agent`: Detects non-random battle outcomes.
    - `master_navigator_agent`: High-level navigation expert.
- **Tools:**
    - `automated_path_navigator`: Finds the shortest path between two points on the current map.
    - `menu_analyzer`: Parses menu screen text to identify options and cursor position.
    - `select_move_in_battle`: Automates selecting a specific move in battle.
    - `use_field_move`: Automates using a field move from the party menu.
    - `general_menu_navigator`: Takes the output of menu_analyzer and a target option, then generates the required button presses to navigate to and select it.

# IX. Automation Ideas
- **Menu Navigation Mapper Agent:** An agent that takes a series of manual inputs and observed cursor movements to deduce the layout and control scheme of an unknown menu, then generates a navigation map for the `general_menu_navigator` tool.

# X. Future Tasks & Reminders
- **Map Marker Cleanup:** Consolidate redundant rock markers on Mt. Moon 1F into a single summary marker upon next visit.
- **Encounter Rate Analyst Agent:** Consider creating an agent to analyze encounter rates in different areas to find optimal paths for travel vs. grinding.
- **Mt. Moon High Encounter Rate:** The western section of Mt. Moon 1F (and likely B1F) has a deliberately high, near-100% encounter rate per step. This is a suspected 'trap' mechanic. Strategy: Running from all non-essential wild battles is the most efficient way to navigate this area.