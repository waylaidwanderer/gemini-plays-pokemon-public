# I. Meta-Strategy & Automation
1.  **Immediate Maintenance:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified, regardless of game state. Deferring these tasks is a critical failure.
2.  **Proactive Automation & Refinement:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority. If an agent or tool is suboptimal, I must prioritize refining it immediately.
3.  **Trust, But Verify:** I must trust the outputs of my agents and system data. However, if a tool's output contradicts the Game State Information, my assumption must be that the tool is wrong, and I must debug it.
4.  **Hypothesis-Driven Exploration:** All exploration must be guided by a clear, documented hypothesis. I must avoid wandering aimlessly and systematically test one variable at a time, documenting all results.
5.  **Warp Discipline:** After every warp, my first action must be to check and, if necessary, create/update markers on **both** the departure and arrival maps.
6.  **Mandatory Self-Assessment:** Every 50 turns, I must perform a structured self-review to ensure my strategies, documentation, and tool usage remain optimal and aligned with my core principles.
7.  **Efficiency Over Fixation:** If a simple automation tool fails during a low-stakes, repetitive task (like a wild battle), it is more efficient to complete the task manually and fix the tool later, rather than getting stuck debugging mid-task.
8.  **Confirmation Bias Awareness (Self-Assessment Finding):** I must be vigilant against confirmation bias. If a hypothesis fails multiple documented tests, I must actively pivot to a new, different hypothesis rather than repeating the failed approach. I should also formulate tests designed to *disprove* my own theories, not just confirm them. To combat this, I should use the `puzzle_solver_agent` more readily when I feel stuck on a single line of reasoning.
9.  **Strategic Agent Use:** I will make a conscious effort to use the `master_navigator_agent` for high-level exploration planning in new, complex areas (like the partitioned Celadon Dept. Store) to avoid trial-and-error pathing, especially its `detect_stuck` mode when navigation fails repeatedly.
10. **Complex Navigation:** For multi-floor or multi-map navigation puzzles (like the Celadon Dept. Store), I will use the `master_navigator_agent` in `navigate_warps` mode to generate a high-level plan instead of relying on manual floor-by-floor pathing.

# II. Quest Log
- **Current Quest: The Mt. Moon Fossil**
    - **Objective:** Find a fossil to give to the Rocket Grunt blocking the path at Mt. Moon B2F (30,12).
    - **Status:** Stalled. Actively pursuing other leads.
- **New Quest: The Copycat's Gift**
    - **Objective:** Obtain a POKé DOLL and give it to COPYCAT in Cerulean City.
    - **Source:** Super Nerd on Celadon Mart 4F at (13,6). Dialogue: "I'm getting a gift for COPYCAT in CERULEAN CITY. It's got to be a POKé DOLL. They are trendy!"
    - **Hypotheses:**
        - COPYCAT is an NPC inside one of Cerulean City's buildings.
        - COPYCAT is an overworld NPC in Cerulean City.

# III. Battle Intel
- **Type Effectiveness Chart (Verified):**
    - Water is super-effective against Rock/Ground (Observed: OMANYTE's SURF vs GEODUDE).
    - Water is not very effective against Bug/Grass (Observed: OMANYTE's BUBBLEBEAM vs PARAS).
    - Water is not very effective against Ghost/Poison (Observed: HELIX's SURF vs GASTLY).
    - Poison is not very effective against Poison/Flying (Confirmed: ECHO's SLUDGE vs ZUBAT) and Rock/Ground (Observed: ECHO's SLUDGE vs GEODUDE).
    - Flying is not very effective against Rock/Ground (Observed: ECHO's FLY vs GEODUDE).
- **Notable Trainer Rosters:**
    - **Sabrina (Saffron Gym):** MR. MIME (Lv 65 - PSYCHIC), HYPNO (Lv 64 - PSYWAVE), SLOWBRO (Lv 64 - PSYCHIC), JYNX (Lv 64 - BLIZZARD, BUBBLEBEAM, DREAM EATER, LOVELY KISS), GENGAR (Lv 64 - NIGHT SHADE, PSYCHIC), ALAKAZAM (Lv 65 - THUNDER WAVE, PSYCHIC).
    - **SMITH (Cerulean Cave):** AERODACTYL (Lv 65 - HYPER BEAM, ROCK SLIDE).
    - **Brock (Pewter Gym):** OMASTAR (Lv 64 - HYDRO PUMP, BLIZZARD), ONIX (Lv 65 - EARTHQUAKE, ROCK SLIDE), KABUTOPS (Lv 64 - SWORDS DANCE, SLASH), GOLEM (Lv 64 - ROCK SLIDE), NINETALES (Lv 64 - REFLECT), AERODACTYL (Lv 65 - FLY).
- **Wild Pokémon Locations:**
    - **Cerulean Cave:** WIGGLYTUFF (Lv 62 - LOVELY KISS, DOUBLE-EDGE, REST), SANDSLASH (Lv 63 - SWORDS DANCE, EARTHQUAKE), GOLEM (Lv 64 - EXPLOSION), LICKITUNG (Lv 61 - WRAP), CHANSEY (Lv 63 - DEFENSE CURL, MEGA PUNCH), RAICHU (Lv 64 - AGILITY).

# IV. Fossil Quest - Hypotheses Log
- **Failed Hypotheses:**
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
    - One of the ladders that leads to a dead end must be entered and exited a specific number of times (e.g., three times) to change its destination. (Result: Tested on ladder at (26,16). No change in destination after 3 cycles).
    - There is a hidden, one-way passage concealed in the western wall on 1F. (Result: The western wall from (2,3) to (2,18) has been systematically checked and yielded no results.)
    - The Escape Rope item is scripted to function differently within Mt. Moon, acting as a warp to the central B2F area instead of the cave entrance. (Result: Using an Escape Rope on Mt. Moon 1F functioned normally, warping me to the last used Pokémon Center on Route 4.)
    - A specific, seemingly mundane rock in Mt. Moon is a disguised ladder that can only be activated by having a Clefairy in the first slot of the party. (Result: Systematically checked all rocks on 1F and a portion of B1F. No results.)
    - The Hiker's line 'I'm on a break' is a literal statement of need. He is thirsty, and giving him a specific drink item will make him move. (Result: Failed. Interacting with him only produces the dialogue 'Kids like you shouldn't be here!'. No option to give him an item was presented).
    - An un-revived fossil Pokémon can be acquired by fishing in one of the small, seemingly decorative water pools inside Mt. Moon. (Status: All known water pools in Mt. Moon appear to be in unreachable map partitions).
    - The Rocket Grunt will accept a Pokémon that is thematically a 'fossil' but is not from a revived fossil item. The player's Marowak, due to its skull, might qualify, but only after undergoing a secret event. (Sub-hypothesis: Use Moon Stone on it. Result: Failed. The game displays 'NOT ABLE').
    - The Pokémon Tower is a red herring for the fossil quest. (Failed: Interacting with ghost spot and 'anemic' Channeler with Marowak in party yielded no results).
- **Active Hypotheses:**
    - The 'fossil' the Rocket Grunt wants is a fainted Pokémon.
    - Giving the Little Girl on the Celadon Mart Roof the correct drink will trigger an event that opens a path to the eastern side of 4F.
    - One of the vending machines on the Celadon Mart Roof is a secret teleporter. (Result: Interacted with all three vending machines and purchased one of each drink. No teleportation occurred.)
    - **New Hypothesis (from Overwatch):** Use the `puzzle_solver_agent` to generate new, out-of-the-box hypotheses for the Mt. Moon fossil quest.

# V. Game & World Mechanics
- **Battle Menu Anomaly:** The game appears to intentionally restrict move selection in certain wild battles to the first move slot. Strategy: For low-stakes wild battles, running is the most efficient option.
- **Party Menu 'SWITCH' Lock:** The game appears to intentionally prevent the use of the 'SWITCH' command in the party menu under certain, currently unknown, conditions. This was observed after multiple failed escape attempts in Mt. Moon.
- **Pokemon Tower 6F Healer Change:** The friendly Channeler at (13,11) is no longer a healer. Her dialogue has changed to 'I feel anemic and weak...'.
- **POKé DOLL Escape:** A POKé DOLL can be used to guarantee an escape from a wild Pokémon battle.
- **Shop Menu Navigation Anomaly:** The shop menu in the Cerulean Mart does not follow a standard 2x2 grid layout. Navigation appears to be column-based. Further testing is required to map it out for automation.

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
- **(Turn 210956):** Failed mandatory self-assessment. Misread map data. Acknowledged input drops and need to retry failed navigation.
- **(Turn 211006):** Failed to immediately fix `select_move_in_battle` tool, violating immediate maintenance directive.
- **(Turn 211057):** Failed to use `battle_anomaly_detector_agent`. Identified need to improve notepad and create new tools.
- **(Turn 211109):** Performed self-assessment. Overhauled notepad. Re-committed to immediate maintenance.
- **(Turn 211776):** Performed self-assessment. Reorganized notepad for clarity. Confirmed adherence to core principles, especially immediate maintenance and hypothesis-driven exploration.
- **(Turn 212394):** Update on Hypothesis 3: The target water pool on B2F is in a separate map partition and unreachable from the central B2F area accessed via the ladder at B1F (18,12).
- **(Turn 212415):** Update on Hypothesis 3: The ladder at B1F (14,28) leads to an isolated, elevated platform on B2F at (16,28), not the main western area with the water pool. The western B2F map is also partitioned.
- **(Turn 212438):** Update on Hypothesis 3: The ladder at B1F (22,18) also leads to an isolated platform on B2F, not the main western area. This route is also a dead end for reaching the water pool.
- **(Turn 212805):** Performed self-assessment. Identified a persistent loop/fixation on a failed hypothesis (interacting with the ghost spot). Corrected by formulating a new, different test plan (talking to the 'anemic' Channeler).
- **(Turn 213076):** Performed self-assessment. Identified a persistent failure to interact with a moving NPC and a hallucination about my position. Corrected by using the `stun_npc` tool and re-pathing from my actual location.
- **(Turn 213112):** Performed self-assessment. Refactored notepad to include new 'Tile Mechanics' and 'Automation Ideas' sections. Re-committed to using `master_navigator_agent` for complex exploration.
- **(Turn 213164):** Performed self-assessment. Refactored notepad to remove redundant quest entries. Confirmed adherence to core principles.
- **(Turn 213420):** Performed self-assessment. Updated tool/agent documentation in notepad. Confirmed adherence to core principles and flexibility in goal-setting.
- **(Turn 213573):** Performed self-assessment. Refactored notepad to integrate strategic principles. Identified a missed opportunity to use `master_navigator_agent` for complex navigation. Deleted one redundant map marker.
- **(Turn 213727):** Performed self-assessment. Identified failure to immediately fix tools (`general_menu_navigator`). Acknowledged underutilization of `master_navigator_agent` and confirmation bias regarding menu layouts. Updated notepad with new hypotheses and automation ideas.

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